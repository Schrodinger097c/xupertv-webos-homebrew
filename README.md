# XuperMH 2.32.5 para LG webOS

Este repositorio Homebrew, mantenido por **Schrodinger**, distribuye actualmente **XuperMH 2.32.5** para televisores LG webOS.

La IPK identifica la aplicación como **XuperMH**, desarrollada por **AarónMH** y descrita en sus metadatos como una modificación derivada del port de XuperTV para LG webOS de **CristiancoDEV (webosflux)**, bajo licencia MIT.

## Instalación desde Homebrew Channel

En Homebrew Channel, entra a **Settings → Add repository** y agrega:

```text
https://raw.githubusercontent.com/Schrodinger097c/xupertv-webos-homebrew/main/repository.json
```

Actualiza el catálogo, busca **XuperMH** y selecciona **Install**. La instalación está sujeta a los permisos del televisor.

## Versión activa

- **Aplicación:** XuperMH
- **Versión:** 2.32.5
- **App ID:** `com.webosflux.xuptertv.fidelity`
- **Resolución declarada:** 1280 × 720
- **Paquete:** `XuperMH-v2.32.5-720-CORREGIDA.ipk`
- **Tamaño:** 22.641.218 bytes
- **SHA-256:** `52ec7f491c6e92f0a6cad41153aa67588b73e836796040df598da4a1c55fed13`
- **Descarga:** [Release v.2.0](https://github.com/Schrodinger097c/xupertv-webos-homebrew/releases/tag/v.2.0)

## Corrección de instalación (9 de noviembre de 2026)

La IPK anterior tenía fechas de 1970 en los encabezados y entradas TAR. Esto podía provocar el mensaje `-5: ipk verified failed` al instalar desde Homebrew Channel. Reempaquetamos el archivo con fechas válidas, preservando los 230 archivos originales de la aplicación sin modificar su contenido. El manifiesto apunta ahora exclusivamente a la versión `CORREGIDA`.

Si ya agregaste el repositorio, actualiza el catálogo de Homebrew Channel y vuelve a intentar **Install**. Esta reparación pasó validación de integridad y formato, pero aún requiere confirmación en un televisor real.

## Cambio respecto a XuperTV WebOS 1.7.0

Antes, el repositorio publicaba **XuperTV WebOS 1.7.0** con identificador `com.schrodinger.xupertv.webos`. La nueva IPK tiene un **ID diferente**: no se instala como una actualización de la aplicación anterior. Ambas pueden aparecer instaladas por separado, según los permisos de webOS.

La versión histórica se conserva en [Releases v1.7.0](https://github.com/Schrodinger097c/xupertv-webos-homebrew/releases/tag/v1.7.0) para restauración si es necesario.

## Aviso

La disponibilidad de contenido y sus derechos dependen de las fuentes y autorizaciones correspondientes. Este repositorio y la aplicación no están afiliados a LG Electronics.
