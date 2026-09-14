# Aurex Android APK

Proyecto listo para subir a GitHub y compilar Aurex como APK usando GitHub Actions + Capacitor.

## Cómo obtener el APK desde GitHub

1. Crea un repositorio nuevo en GitHub.
2. Sube **todo el contenido de esta carpeta** conservando las carpetas `.github` y `www`.
3. En GitHub abre la pestaña **Actions**.
4. Abre **Build Aurex APK**.
5. Pulsa **Run workflow**.
6. Cuando termine, entra al resultado del workflow y descarga el artefacto **Aurex-debug-apk**.
7. Dentro estará `Aurex-debug.apk`.

El workflow también se ejecuta automáticamente al hacer push a `main` o `master`.

## Datos de la app

- Nombre: Aurex
- App ID: `com.aurex.controlgastos`
- Web principal: `www/index.html`
- Capacitor: 8.5.2

## Nota importante

Este build genera un **APK de depuración (debug)** que se puede instalar manualmente en Android. Para publicar en Google Play hace falta configurar firma de release/AAB.
