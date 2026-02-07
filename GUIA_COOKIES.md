# 🍪 Guía Completa de Cookies para Facebook

## ¿Por qué necesito cookies?

Las cookies son necesarias para:
- ✅ Descargar videos privados de amigos
- ✅ Descargar videos de grupos privados
- ✅ Evitar bloqueos y limitaciones
- ✅ Mejorar la tasa de éxito en descargas

## Métodos para Obtener Cookies

### Método 1: Extensión del Navegador (Más Fácil) ⭐

#### Para Chrome/Edge/Brave:

1. **Instala la extensión:**
   - Busca "Get cookies.txt LOCALLY" en Chrome Web Store
   - O ve directamente: https://chrome.google.com/webstore
   - Haz clic en "Agregar a Chrome"

2. **Obtén las cookies:**
   - Abre Facebook y **inicia sesión**
   - Navega a cualquier página de Facebook
   - Haz clic en el ícono de la extensión
   - Haz clic en "Export"
   - Se descargará un archivo "facebook.com_cookies.txt"

3. **Ubica el archivo:**
   - Por defecto está en tu carpeta de Descargas
   - Renómbralo a "facebook_cookies.txt" (opcional)

#### Para Firefox:

1. **Instala la extensión:**
   - Busca "cookies.txt" en Firefox Add-ons
   - Instala "cookies.txt" o "Export Cookies"

2. **Exporta:**
   - Inicia sesión en Facebook
   - Haz clic en el ícono de la extensión
   - Exporta las cookies de facebook.com
   - Guarda como "facebook_cookies.txt"

### Método 2: Manualmente desde DevTools (Avanzado)

#### Chrome/Edge:

1. **Abre DevTools:**
   - Presiona F12 en Facebook
   - O clic derecho → "Inspeccionar"

2. **Ve a Application:**
   - Haz clic en la pestaña "Application"
   - En el panel izquierdo, expande "Cookies"
   - Selecciona "https://www.facebook.com"

3. **Copia las cookies:**
   - Verás una lista de cookies
   - Las más importantes son:
     - c_user
     - xs
     - datr
     - sb

4. **Crea el archivo:**
   - Crea un archivo de texto "facebook_cookies.txt"
   - Usa el formato Netscape (ver abajo)

### Método 3: Desde Android (App)

1. **Instala Cookie Editor:**
   - Busca "Cookie Editor" en Play Store
   - O usa "Web Developer Tools"

2. **Exporta cookies:**
   - Abre Facebook en Chrome móvil
   - Abre Cookie Editor
   - Exporta las cookies
   - Envíalas a tu PC

## Formato del Archivo de Cookies

El archivo debe tener formato **Netscape**, así:

```
# Netscape HTTP Cookie File
# This is a generated file! Do not edit.
.facebook.com	TRUE	/	TRUE	1234567890	c_user	123456789
.facebook.com	TRUE	/	TRUE	1234567890	xs	1%7Cabcdefg
.facebook.com	TRUE	/	TRUE	1234567890	datr	abcdefghijklmnop
.facebook.com	TRUE	/	FALSE	1234567890	sb	qrstuvwxyz
```

**Formato de cada línea:**
```
dominio	flag	path	secure	expiration	nombre	valor
```

## Uso de las Cookies en los Scripts

### Script Principal (`descargar_videos.py`):

```bash
python3 descargar_videos.py
# Selecciona: 3. Configurar cookies de Facebook
# Ingresa la ruta: /ruta/a/facebook_cookies.txt
# Luego descarga normalmente
```

### Script Facebook (`facebook_descargador.py`):

```bash
python3 facebook_descargador.py
# Cuando descargues, te preguntará por las cookies
# Ingresa: s (sí)
# Ingresa la ruta: /ruta/a/facebook_cookies.txt
```

### Uso Directo con yt-dlp:

```bash
yt-dlp --cookies facebook_cookies.txt [URL]
```

## Verificar que las Cookies Funcionan

```bash
# Prueba con información del video
yt-dlp --cookies facebook_cookies.txt --dump-json [URL]

# Si funciona, verás información JSON del video
# Si falla, las cookies pueden estar expiradas
```

## Solución de Problemas

### ❌ Error: "Cookie file not found"

**Solución:**
- Verifica la ruta del archivo
- Usa rutas absolutas: `/home/usuario/facebook_cookies.txt`
- En Windows: `C:\Users\Usuario\facebook_cookies.txt`

### ❌ Error: "Login required"

**Solución:**
- Las cookies están expiradas
- Vuelve a exportarlas desde el navegador
- Asegúrate de estar logueado al exportar

### ❌ Error: "Invalid cookie format"

**Solución:**
- Verifica el formato Netscape
- Usa una extensión confiable para exportar
- No edites manualmente el archivo

### ❌ Las cookies funcionan pero siguen fallando

**Solución:**
1. Actualiza yt-dlp:
   ```bash
   pip install --upgrade yt-dlp
   ```

2. Verifica que el video no esté restringido por región

3. Intenta con diferentes métodos del script especializado

## Seguridad y Privacidad

### ⚠️ IMPORTANTE:

- **NO compartas tu archivo de cookies** - Contiene tu sesión
- Alguien con tus cookies puede acceder a tu cuenta
- Elimina las cookies después de usarlas
- No las subas a GitHub o servicios en la nube
- Considera usar una cuenta secundaria

### Buenas Prácticas:

1. **Crea una cuenta secundaria:**
   - Usa una cuenta de Facebook secundaria
   - Exporta cookies de esa cuenta
   - Más seguro si hay problemas

2. **Renueva periódicamente:**
   - Exporta cookies nuevas cada semana
   - Las cookies expiran con el tiempo

3. **Elimina después de usar:**
   ```bash
   rm facebook_cookies.txt
   ```

4. **Permisos del archivo:**
   ```bash
   chmod 600 facebook_cookies.txt  # Solo tú puedes leer
   ```

## Cookies para Otras Plataformas

### Instagram:
- Mismo proceso que Facebook
- Exporta de "instagram.com"
- Archivo: `instagram_cookies.txt`

### TikTok:
- Exporta de "tiktok.com"
- Archivo: `tiktok_cookies.txt`

### Twitter/X:
- Exporta de "twitter.com" o "x.com"
- Archivo: `twitter_cookies.txt`

## Tips Adicionales

### 💡 Tip 1: Múltiples Cuentas
Crea archivos separados para diferentes cuentas:
- `facebook_personal_cookies.txt`
- `facebook_trabajo_cookies.txt`

### 💡 Tip 2: Automatización
En scripts avanzados:
```python
import os
cookie_file = os.path.expanduser("~/.cookies/facebook.txt")
```

### 💡 Tip 3: Rotación de Cookies
Si descargas mucho, rota entre varias cuentas para evitar bloqueos.

## Herramientas Útiles

### Extensiones Recomendadas:

**Chrome/Edge:**
- Get cookies.txt LOCALLY ⭐ (Recomendado)
- EditThisCookie
- Cookie-Editor

**Firefox:**
- cookies.txt ⭐ (Recomendado)
- Export Cookies

### Verificadores Online:

⚠️ **NUNCA** uses verificadores online con tus cookies reales
- Son inseguros
- Pueden robar tu sesión

## Preguntas Frecuentes

### ¿Las cookies caducan?
Sí, típicamente en 1-2 semanas. Expórtalas nuevamente cuando sea necesario.

### ¿Puedo usar las mismas cookies en varios dispositivos?
Sí, pero Facebook puede detectarlo como sospechoso.

### ¿Necesito cookies para todos los videos?
No, solo para:
- Videos privados
- Videos de grupos privados
- Cuando hay errores de descarga

### ¿Es legal usar cookies?
Sí, si son TUS propias cookies de TU cuenta. No uses cookies de otras personas.

### ¿Qué pasa si Facebook detecta el uso?
Puede:
- Pedirte verificación
- Limitar temporalmente tu cuenta
- En casos extremos, suspender la cuenta (raro)

**Recomendación:** Usa una cuenta secundaria para descargas.

---

**Última actualización:** Febrero 2026

**Nota:** Facebook actualiza constantemente sus sistemas. Si los métodos no funcionan, busca actualizaciones del script y yt-dlp.
