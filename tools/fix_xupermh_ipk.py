#!/usr/bin/env python3
"""Repair legacy 1970 timestamps in an IPK without editing its application files."""
from pathlib import Path
import io
import sys
import time
import tarfile
import gzip
import hashlib

STAMP = 1794182400  # 2026-11-09 00:00:00 UTC
PARTS = ("debian-binary", "control.tar.gz", "data.tar.gz")

def read_ar(filename):
    data = Path(filename).read_bytes()
    if not data.startswith(b"!<arch>\n"):
        raise ValueError("Not an ar/IPK file")
    pos = 8
    result = {}
    while pos < len(data):
        header = data[pos:pos + 60]
        if len(header) != 60 or header[58:60] != b"`\n":
            raise ValueError("Invalid ar header")
        name = header[:16].decode("ascii").strip().rstrip("/")
        length = int(header[48:58].decode("ascii").strip())
        start = pos + 60
        result[name] = data[start:start + length]
        if len(result[name]) != length:
            raise ValueError("Truncated ar member")
        pos = start + length + length % 2
    if tuple(result) != PARTS or result["debian-binary"] != b"2.0\n":
        raise ValueError("Unexpected IPK contents")
    return result

def update_tar(raw):
    source = tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz")
    output = io.BytesIO()
    with gzip.GzipFile(fileobj=output, mode="wb", filename="", mtime=STAMP, compresslevel=6) as gz:
        with tarfile.open(fileobj=gz, mode="w|", format=tarfile.GNU_FORMAT) as target:
            for info in source:
                info.mtime = STAMP
                info.uid = info.gid = 0
                info.uname = info.gname = ""
                info.pax_headers = {}
                target.addfile(info, source.extractfile(info) if info.isfile() else None)
    source.close()
    return output.getvalue()

def make_ar(parts, outname):
    raw = bytearray(b"!<arch>\n")
    for name in PARTS:
        content = parts[name]
        header = (f"{name}/".ljust(16) + str(STAMP).ljust(12) +
                  "0".ljust(6) + "0".ljust(6) + "100644".ljust(8) +
                  str(len(content)).ljust(10) + "`\n").encode("ascii")
        assert len(header) == 60
        raw.extend(header)
        raw.extend(content)
        if len(content) % 2:
            raw.extend(b"\n")
    Path(outname).write_bytes(raw)

def verify(old, new):
    for part in ("control.tar.gz", "data.tar.gz"):
        src = tarfile.open(fileobj=io.BytesIO(old[part]), mode="r:gz")
        dst = tarfile.open(fileobj=io.BytesIO(new[part]), mode="r:gz")
        old_entries, new_entries = src.getmembers(), dst.getmembers()
        assert len(old_entries) == len(new_entries)
        for a, b in zip(old_entries, new_entries):
            assert (a.name, a.type, a.mode, a.linkname, a.size) == (b.name, b.type, b.mode, b.linkname, b.size)
            assert b.mtime == STAMP
            if a.isfile():
                assert src.extractfile(a).read() == dst.extractfile(b).read()
        print(part, len(new_entries), "entries verified, identical file contents")
        src.close()
        dst.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python fix_xupermh_ipk.py ORIGINAL.ipk CORRECTED.ipk")
    old = read_ar(sys.argv[1])
    updated = old.copy()
    updated["control.tar.gz"] = update_tar(old["control.tar.gz"])
    updated["data.tar.gz"] = update_tar(old["data.tar.gz"])
    make_ar(updated, sys.argv[2])
    verify(old, read_ar(sys.argv[2]))
    print("Corrected:", sys.argv[2], Path(sys.argv[2]).stat().st_size,
          hashlib.sha256(Path(sys.argv[2]).read_bytes()).hexdigest())
