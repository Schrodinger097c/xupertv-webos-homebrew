# XuperTV WebOS — Homebrew de Schrodinger

- Autor: **Schrodinger**
- Cuenta GitHub: **[Santiago097c](https://github.com/Santiago097c)**
- App ID: `com.schrodinger.xupertv.webos`
- Versión: `1.7.0`
- IPK incluida: `com.schrodinger.xupertv.webos_1.7.0_all.ipk`
- Hash SHA-256: `f1c926dbf5df348bc7f8c68c165d1b4e114a511128eafda2828a13f5912fc1fa`

## Estado

Este ZIP está **preparado para publicarse**. **No significa que el repositorio ni el Release existan ya en GitHub**. Tampoco incluye una publicación automática.

## Publicar sin consola

1. Accede a `https://github.com/new` con tu usuario `Santiago097c` y crea un repositorio **público** llamado **`xupertv-webos-homebrew`**, con rama `main`.
2. En la raíz del repositorio, sube con **Add file → Upload files** los cuatro archivos que vienen en la raíz de este ZIP: `repository.json`, `manifest.json`, `icon.png` y `README.md`. También puedes subir los scripts opcionales, pero **no necesitas subir `release/` como carpeta del repositorio**.
3. En GitHub, ve a **Releases → Draft a new release** y crea la etiqueta **`v1.7.0`**. Adjunta desde la carpeta `release/` el archivo `com.schrodinger.xupertv.webos_1.7.0_all.ipk`. Pulsa **Publish release**.
4. Comprueba que se abran estos tres enlaces públicos:
   - Catálogo: https://raw.githubusercontent.com/Santiago097c/xupertv-webos-homebrew/main/repository.json
   - Manifiesto: https://raw.githubusercontent.com/Santiago097c/xupertv-webos-homebrew/main/manifest.json
   - IPK: https://github.com/Santiago097c/xupertv-webos-homebrew/releases/download/v1.7.0/com.schrodinger.xupertv.webos_1.7.0_all.ipk
5. En **Homebrew Channel → Settings → Add repository**, pega esta URL exacta:

   `https://raw.githubusercontent.com/Santiago097c/xupertv-webos-homebrew/main/repository.json`

6. Busca **XuperTV WebOS** y elige **Install**. El proceso depende de los permisos disponibles en tu Homebrew Channel y dispositivo. Esta vía no garantiza instalación en televisores sin los permisos adecuados.

## Actualizaciones

Para otra versión, conserva el App ID `com.schrodinger.xupertv.webos`, actualiza el número en `manifest.json`, la URL de la IPK, `ipkSize` y `ipkHash.sha256`, sube los JSON nuevos al repositorio y crea otro GitHub Release con la IPK correspondiente.

## Integridad

- SHA-256: `f1c926dbf5df348bc7f8c68c165d1b4e114a511128eafda2828a13f5912fc1fa`
- Tamaño: `24509056` bytes

**Importante:** este material conserva byte por byte la IPK 1.7.0 compartida anteriormente. No sustituye derechos de distribución de código y contenidos de terceros. Antes de subirla a un repositorio público, revisa dependencias y licencias y confirma que no existan tokens o credenciales privadas dentro del paquete.

Referencia Homebrew Channel: https://github.com/webosbrew/webos-homebrew-channel
