# 📥 Descargador de Videos Mejorado v2.0

Sistema profesional para descargar videos de múltiples plataformas, con soporte especial y optimizado para Facebook.

## 🎯 Características Principales

### ✨ Lo que hace especial a este descargador:

- **🎯 Detección automática de plataforma** - Reconoce Facebook, Instagram, TikTok, YouTube y más
- **🔄 6 métodos de descarga** - Si uno falla, prueba automáticamente con otros
- **🍪 Gestión inteligente de cookies** - Para videos privados de Facebook
- **📊 Descarga masiva** - Procesa múltiples videos desde un archivo
- **⚠️ Manejo robusto de errores** - Mensajes claros y soluciones sugeridas
- **📖 Documentación completa** - README, guía de cookies y ejemplos

### 🌐 Plataformas Soportadas

| Plataforma | Estado | Notas |
|-----------|--------|-------|
| Facebook | ⭐ Optimizado | Múltiples métodos, soporte de cookies |
| Instagram | ✅ Soportado | Reels y posts |
| TikTok | ✅ Soportado | Videos y slideshows |
| YouTube | ✅ Soportado | Videos, shorts, playlists |
| Twitter/X | ✅ Soportado | Videos y GIFs |
| +1000 sitios | ✅ Soportado | Via yt-dlp |

## 🚀 Inicio Rápido

### Instalación en 2 pasos:

```bash
# 1. Ejecuta el instalador (automático)
bash instalar.sh          # Linux/Mac
# o
instalar.bat              # Windows

# 2. Inicia el programa
python3 descargar_videos.py
```

## 📖 Guías de Uso

### Ejemplo 1: Descargar un video de YouTube

```bash
$ python3 descargar_videos.py

================================================================
                   🎬 DESCARGADOR DE VIDEOS
================================================================
📱 Plataformas soportadas:
   • Facebook (fb.com, facebook.com, fb.watch)
   • Instagram
   • TikTok
   • YouTube
   • Twitter/X
   • +1000 sitios más

🍪 Cookies: ✗ No configuradas

📋 OPCIONES:
   1. Descargar un video
   2. Descargar múltiples videos (desde archivo)
   3. Configurar cookies de Facebook
   4. Actualizar yt-dlp
   5. Ver ayuda
   6. Salir

👉 Elige una opción (1-6): 1

📎 Ingresa la URL del video: https://www.youtube.com/watch?v=dQw4w9WgXcQ

================================================================
                      🎯 Plataforma: YOUTUBE
================================================================

📥 Descargando video...
📁 Guardando en: /home/usuario/Descargas/Videos

[download] Destination: Rick Astley - Never Gonna Give You Up.mp4
[download] 100% of 3.28MiB in 00:02

✅ ¡Video descargado exitosamente!

⏸  Presiona Enter para continuar...
```

### Ejemplo 2: Descargar video de Facebook (sin cookies)

```bash
👉 Elige una opción (1-6): 1

📎 Ingresa la URL del video: https://www.facebook.com/watch/?v=123456789

================================================================
                     🎯 Plataforma: FACEBOOK
================================================================

📥 Descargando video...
📁 Guardando en: /home/usuario/Descargas/Videos

[download] 100% of 5.12MiB in 00:03

✅ ¡Video descargado exitosamente!
```

### Ejemplo 3: Descargar con cookies (video privado)

```bash
👉 Elige una opción (1-6): 3

================================================================
                  🍪 CONFIGURACIÓN DE COOKIES
================================================================

📖 Para obtener cookies de Facebook:

1. Instala la extensión "Get cookies.txt LOCALLY" en tu navegador
2. Inicia sesión en Facebook
3. Haz clic en la extensión y exporta las cookies
4. Guarda el archivo como "facebook_cookies.txt"

💡 Lee GUIA_COOKIES.md para instrucciones detalladas

Ruta del archivo de cookies (Enter para omitir): facebook_cookies.txt

✓ Archivo de cookies válido: facebook_cookies.txt

✅ Cookies configuradas correctamente
   Archivo: facebook_cookies.txt

⏸  Presiona Enter para continuar...
```

### Ejemplo 4: Descarga masiva desde archivo

Primero, crea `mis_videos.txt`:
```
https://www.facebook.com/watch/?v=123456789
https://www.instagram.com/p/ABC123xyz/
https://www.tiktok.com/@user/video/1234567890
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Luego ejecuta:

```bash
👉 Elige una opción (1-6): 2

📋 DESCARGA MÚLTIPLE
💡 El archivo debe tener una URL por línea
   Revisa ejemplo_urls.txt como referencia

📄 Ruta del archivo con URLs: mis_videos.txt

✓ 4 URLs válidas encontradas

================================================================
              📋 DESCARGA MASIVA: 4 videos
================================================================

============================================================
📹 Video 1/4
============================================================
🔗 https://www.facebook.com/watch/?v=123456789

[... descarga ...]

✅ ¡Video descargado exitosamente!

============================================================
📹 Video 2/4
============================================================
🔗 https://www.instagram.com/p/ABC123xyz/

[... descarga ...]

✅ ¡Video descargado exitosamente!

[...]

================================================================
                   📊 RESUMEN DE DESCARGAS
================================================================
✅ Exitosas: 3/4
❌ Fallidas: 1/4

❌ Videos que fallaron:
   3. https://www.tiktok.com/@user/video/1234567890...

¿Guardar lista de URLs fallidas? (s/n): s

💾 URLs fallidas guardadas en:
   /home/usuario/Descargas/Videos/urls_fallidas.txt
```

### Ejemplo 5: Manejo de error con sugerencias

```bash
📎 Ingresa la URL del video: www.facebook.com/watch/?v=123

❌ URL inválida. Debe comenzar con http:// o https://
   Recibido: www.facebook.com/watch/?v=123...

💡 Sugerencias:
   1. Copia la URL completa desde tu navegador
   2. Verifica que el video exista y sea accesible
   3. Para videos privados, configura cookies (opción 3)
```

## 📦 Instalación Detallada

### Requisitos

- **Python 3.6+** (Verifica con: `python3 --version`)
- **pip** (Gestor de paquetes de Python)
- **ffmpeg** (Opcional pero recomendado)

### Método 1: Instalación Automática (Recomendado)

```bash
# Linux/macOS
bash instalar.sh

# Windows
instalar.bat
```

Esto instalará automáticamente:
- yt-dlp
- Creará directorios necesarios
- Configurará permisos

### Método 2: Instalación Manual

```bash
# 1. Instalar yt-dlp
pip install yt-dlp

# 2. (Opcional) Instalar ffmpeg
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows: Descargar desde https://ffmpeg.org
```

## 🎮 Uso del Script Especializado para Facebook

Para casos difíciles de Facebook, usa el script especializado:

```bash
python3 facebook_descargador.py

================================================================
           📱 DESCARGADOR ESPECIALIZADO DE FACEBOOK
================================================================

1. Descargar video (todos los métodos)
2. Obtener información del video
3. Actualizar yt-dlp
4. Salir

Elige una opción (1-4): 1

📎 URL del video de Facebook: https://fb.watch/abc123/

📎 URL limpia: https://www.facebook.com/watch/?v=123456789
📁 Carpeta de descarga: /home/usuario/Descargas/Facebook_Videos

¿Tienes un archivo de cookies de Facebook? (s/n): n

================================================================
        🚀 Iniciando descarga con múltiples métodos...
================================================================

[Método 1] Descarga básica optimizada...
✅ ¡Descarga exitosa con método: Básico!
```

## 🍪 Configuración de Cookies (Videos Privados)

### ¿Cuándo necesito cookies?

- ✅ Videos de amigos (privacidad: Amigos)
- ✅ Videos de grupos privados
- ✅ Cuando aparece error "Login required"
- ✅ Videos con restricciones de visualización

### Cómo obtener cookies (Método rápido):

1. **Instala extensión** en Chrome/Firefox:
   - Chrome: "Get cookies.txt LOCALLY"
   - Firefox: "cookies.txt"

2. **Exporta las cookies:**
   - Abre Facebook e inicia sesión
   - Haz clic en la extensión
   - Exporta cookies de facebook.com
   - Guarda como `facebook_cookies.txt`

3. **Úsalas en el script:**
   ```bash
   Opción 3 → Configurar cookies
   Ruta: /ruta/a/facebook_cookies.txt
   ```

📖 **Lee `GUIA_COOKIES.md` para instrucciones paso a paso con imágenes**

## 📁 Estructura del Proyecto

```
descargador-videos/
├── core.py                    # ⭐ Módulo central (nuevo)
├── descargar_videos.py        # Script principal mejorado
├── facebook_descargador.py    # Script especializado Facebook
├── README.md                  # Esta guía
├── GUIA_COOKIES.md           # Tutorial detallado de cookies
├── ejemplo_urls.txt          # Plantilla para descarga masiva
├── instalar.sh               # Instalador Linux/Mac
└── instalar.bat              # Instalador Windows
```

## 🔧 Solución de Problemas

### ❌ Error: "No module named 'core'"

**Causa:** El archivo `core.py` no está en el mismo directorio

**Solución:**
```bash
# Asegúrate de que todos los archivos estén juntos:
ls -l
# Debes ver: core.py, descargar_videos.py, etc.
```

### ❌ Error: "yt-dlp no encontrado"

**Solución:**
```bash
# Opción 1: Usar el instalador
bash instalar.sh

# Opción 2: Manual
pip install --upgrade yt-dlp

# Opción 3: Desde el menú
python3 descargar_videos.py → Opción 4
```

### ❌ Error al descargar de Facebook

**Causas comunes:**

1. **Video privado sin cookies:**
   ```
   Solución: Configura cookies (Opción 3)
   ```

2. **URL incorrecta:**
   ```
   Solución: Copia la URL completa: https://www.facebook.com/watch/?v=...
   ```

3. **yt-dlp desactualizado:**
   ```
   Solución: Actualiza con Opción 4 del menú
   ```

4. **Nada funciona:**
   ```bash
   # Usa el script especializado
   python3 facebook_descargador.py
   ```

### ❌ El video se descarga pero no se reproduce

**Causa:** Falta ffmpeg

**Solución:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Descarga desde: https://ffmpeg.org/download.html
```

### ❌ Archivo de cookies inválido

**Solución:**
```
1. Asegúrate de exportar en formato Netscape
2. No edites el archivo manualmente
3. Verifica que las cookies sean recientes
4. Lee GUIA_COOKIES.md para el formato correcto
```

## 💡 Tips y Trucos

### 🚀 Tip 1: Descarga más rápida

```bash
# Usa formato específico si sabes la calidad
python3 -c "from core import *; ..."  # Ver ejemplos en core.py
```

### 📊 Tip 2: Organizar descargas

Los videos se guardan automáticamente en:
- Script principal: `~/Descargas/Videos/`
- Facebook especializado: `~/Descargas/Facebook_Videos/`

Puedes cambiar esto editando el script.

### 🍪 Tip 3: Cookies para múltiples cuentas

Crea archivos separados:
```
facebook_personal.txt
facebook_trabajo.txt
instagram_personal.txt
```

Y cámbialos según necesites.

### 🔄 Tip 4: Actualización regular

Ejecuta semanalmente:
```bash
python3 descargar_videos.py → Opción 4
```

Facebook cambia frecuentemente, mantén yt-dlp actualizado.

## 📊 Comparación con Otras Herramientas

| Característica | Este Script | yt-dlp solo | Otros scripts |
|---------------|-------------|-------------|---------------|
| Múltiples métodos Facebook | ✅ | ❌ | ❌ |
| Manejo de errores claro | ✅ | ⚠️ | ❌ |
| Descarga masiva | ✅ | ✅ | ⚠️ |
| Gestión de cookies | ✅ | ⚠️ | ❌ |
| Documentación completa | ✅ | ✅ | ❌ |
| Soporte multiplataforma | ✅ | ✅ | ⚠️ |
| Interfaz amigable | ✅ | ❌ | ⚠️ |

## 🤝 Contribuciones

Este es un proyecto de código abierto. Sugerencias de mejora:

1. Reporta bugs o errores encontrados
2. Sugiere nuevas características
3. Comparte casos de uso exitosos
4. Mejora la documentación

## ⚖️ Licencia y Uso Responsable

- ✅ **Permitido:** Uso personal, descargar tu propio contenido
- ✅ **Permitido:** Respaldo de videos que has creado
- ❌ **No permitido:** Violación de derechos de autor
- ❌ **No permitido:** Descarga masiva sin permiso
- ❌ **No permitido:** Redistribución de contenido ajeno

**Importante:** Respeta los términos de servicio de cada plataforma y los derechos de autor.

## 📞 Ayuda y Soporte

### Recursos Disponibles:

1. **README.md** - Esta guía (uso general)
2. **GUIA_COOKIES.md** - Tutorial de cookies paso a paso
3. **ejemplo_urls.txt** - Plantilla para descargas masivas
4. **Opción 5 del menú** - Ayuda integrada en el programa

### Si nada funciona:

1. Actualiza yt-dlp (Opción 4)
2. Verifica tu conexión a internet
3. Prueba con otra URL similar
4. Lee los mensajes de error detenidamente
5. Consulta la sección de solución de problemas

## 🎓 Ejemplos Avanzados

### Usar yt-dlp directamente (línea de comandos)

```bash
# Descargar con cookies
yt-dlp --cookies facebook_cookies.txt [URL]

# Solo audio MP3
yt-dlp -x --audio-format mp3 [URL]

# Mejor calidad hasta 1080p
yt-dlp -f "bestvideo[height<=1080]+bestaudio" [URL]

# Listar formatos disponibles
yt-dlp -F [URL]

# Subtítulos en español
yt-dlp --write-subs --sub-langs es [URL]
```

## 📝 Changelog

### v2.0 (Actual)
- ✨ Añadido módulo core.py para lógica compartida
- ✨ Validación mejorada de URLs y archivos
- ✨ Mensajes de error más claros con sugerencias
- ✨ Opción de ayuda integrada
- ✨ Guardado automático de URLs fallidas
- ✨ Mejor manejo de interrupciones
- 🐛 Corrección de errores de permisos
- 📖 Documentación expandida con ejemplos reales

### v1.0
- 🎉 Lanzamiento inicial
- 🌐 Soporte multiplataforma
- 🍪 Gestión de cookies
- 📊 Descarga masiva

---

**Última actualización:** Febrero 2026  
**Versión:** 2.0  
**Mantenedor:** Proyecto de código abierto

---

💡 **¿Te fue útil?** Comparte con otros que necesiten descargar videos!
