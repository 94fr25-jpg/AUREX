# AUREX — Proyecto limpio para APK

Este repositorio ya contiene todo lo necesario para compilar Aurex como APK Android mediante GitHub Actions.

## IMPORTANTE

No mezcles archivos de repositorios anteriores.

Crea un repositorio NUEVO y sube exactamente el contenido de esta carpeta.

La estructura debe quedar así:

```text
AUREX/
├── .github/
│   └── workflows/
│       └── build-apk.yml
├── assets/
│   └── aurex-icon.png
├── scripts/
│   └── install_android_icon.py
├── www/
│   └── index.html
├── .gitignore
├── capacitor.config.json
├── package.json
└── README.md
```

## Crear la APK

1. Crea un repositorio nuevo en GitHub.
2. Sube todos los archivos y carpetas anteriores.
3. En GitHub abre `Actions`.
4. Selecciona `Build Aurex APK`.
5. Pulsa `Run workflow`.
6. Espera a que termine en verde.
7. Abre la ejecución terminada.
8. En `Artifacts`, descarga `Aurex-APK`.
9. Descomprime el archivo descargado.
10. Dentro estará `Aurex.apk`.

## Icono

El workflow crea Android desde cero, elimina los iconos genéricos de Capacitor y luego instala `assets/aurex-icon.png` en todas las densidades Android antes de compilar.

Esto evita que el instalador vuelva a mostrar el icono de Capacitor.

## Datos técnicos

- App: Aurex
- Application ID: `com.aurex.controlgastos`
- Capacitor: 8.5.2
- Node.js: 22
- Java: 21
- Salida: APK debug instalable directamente en Android
