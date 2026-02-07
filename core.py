#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
core.py - Módulo central con lógica compartida
Descargador de Videos - Funciones reutilizables
"""

import os
import sys
import subprocess
from pathlib import Path


class ValidacionError(Exception):
    """Error personalizado para validaciones"""
    pass


class DependenciaError(Exception):
    """Error cuando falta una dependencia"""
    pass


def verificar_python_version():
    """Verifica que la versión de Python sea compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        raise ValidacionError(
            f"❌ Python 3.6+ requerido. Tienes Python {version.major}.{version.minor}\n"
            "Descarga Python desde: https://www.python.org"
        )
    return True


def verificar_ytdlp_instalado():
    """Verifica si yt-dlp está instalado"""
    try:
        resultado = subprocess.run(
            ["yt-dlp", "--version"],
            capture_output=True,
            check=True,
            timeout=5
        )
        version = resultado.stdout.decode().strip()
        return True, version
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return False, None


def instalar_ytdlp():
    """Instala yt-dlp automáticamente"""
    print("\n⚠️  yt-dlp no está instalado")
    print("📦 Instalando yt-dlp...\n")
    
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"],
            check=True
        )
        print("\n✅ yt-dlp instalado correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print("\n❌ Error al instalar yt-dlp")
        print("\n💡 Intenta manualmente:")
        print(f"   {sys.executable} -m pip install yt-dlp")
        print("\nO visita: https://github.com/yt-dlp/yt-dlp")
        raise DependenciaError("No se pudo instalar yt-dlp") from e


def verificar_dependencias():
    """Verifica e instala todas las dependencias necesarias"""
    # Verificar Python
    try:
        verificar_python_version()
    except ValidacionError as e:
        print(str(e))
        sys.exit(1)
    
    # Verificar yt-dlp
    instalado, version = verificar_ytdlp_instalado()
    
    if instalado:
        print(f"✓ yt-dlp {version} encontrado")
        return True
    else:
        try:
            instalar_ytdlp()
            return True
        except DependenciaError:
            return False


def validar_url(url):
    """Valida que la URL sea válida"""
    if not url:
        raise ValidacionError("❌ La URL no puede estar vacía")
    
    if not isinstance(url, str):
        raise ValidacionError("❌ La URL debe ser texto")
    
    url = url.strip()
    
    if not url.startswith(('http://', 'https://')):
        raise ValidacionError(
            "❌ URL inválida. Debe comenzar con http:// o https://\n"
            f"   Recibido: {url[:50]}..."
        )
    
    if len(url) < 10:
        raise ValidacionError("❌ URL demasiado corta, verifica que sea correcta")
    
    return url


def validar_archivo_existe(ruta, tipo="archivo"):
    """Valida que un archivo exista"""
    if not ruta:
        raise ValidacionError(f"❌ Debes especificar la ruta del {tipo}")
    
    ruta_path = Path(ruta).expanduser()
    
    if not ruta_path.exists():
        raise ValidacionError(
            f"❌ {tipo.capitalize()} no encontrado: {ruta}\n"
            f"   Ruta absoluta buscada: {ruta_path.absolute()}\n"
            "   Verifica que la ruta sea correcta"
        )
    
    return str(ruta_path.absolute())


def validar_archivo_cookies(ruta_cookies):
    """Valida específicamente un archivo de cookies"""
    try:
        ruta_absoluta = validar_archivo_existe(ruta_cookies, "archivo de cookies")
        
        # Verificar que sea legible
        with open(ruta_absoluta, 'r', encoding='utf-8') as f:
            contenido = f.read(100)
            if not contenido.strip():
                raise ValidacionError(
                    "❌ El archivo de cookies está vacío\n"
                    "   Revisa la GUIA_COOKIES.md para saber cómo obtener cookies válidas"
                )
        
        print(f"✓ Archivo de cookies válido: {Path(ruta_cookies).name}")
        return ruta_absoluta
        
    except (OSError, UnicodeDecodeError) as e:
        raise ValidacionError(
            f"❌ Error al leer el archivo de cookies: {e}\n"
            "   Verifica que el archivo no esté corrupto"
        )


def crear_directorio_seguro(ruta):
    """Crea un directorio de forma segura"""
    try:
        ruta_path = Path(ruta).expanduser()
        ruta_path.mkdir(parents=True, exist_ok=True)
        return ruta_path
    except PermissionError:
        raise ValidacionError(
            f"❌ Sin permisos para crear directorio: {ruta}\n"
            "   Verifica los permisos o elige otra ubicación"
        )
    except OSError as e:
        raise ValidacionError(f"❌ Error al crear directorio: {e}")


def leer_urls_de_archivo(archivo):
    """Lee URLs desde un archivo de texto"""
    try:
        ruta_absoluta = validar_archivo_existe(archivo, "archivo de URLs")
        
        with open(ruta_absoluta, 'r', encoding='utf-8') as f:
            urls = []
            linea_num = 0
            
            for linea in f:
                linea_num += 1
                linea = linea.strip()
                
                # Ignorar líneas vacías y comentarios
                if not linea or linea.startswith('#'):
                    continue
                
                try:
                    url_valida = validar_url(linea)
                    urls.append(url_valida)
                except ValidacionError as e:
                    print(f"⚠️  Línea {linea_num} ignorada: {e}")
                    continue
            
            if not urls:
                raise ValidacionError(
                    "❌ No se encontraron URLs válidas en el archivo\n"
                    "   Las URLs deben:\n"
                    "   - Comenzar con http:// o https://\n"
                    "   - No estar comentadas con #\n"
                    "   - No estar vacías"
                )
            
            print(f"✓ {len(urls)} URLs válidas encontradas")
            return urls
            
    except UnicodeDecodeError:
        raise ValidacionError(
            "❌ Error de codificación en el archivo\n"
            "   Guarda el archivo con codificación UTF-8"
        )


def ejecutar_comando_ytdlp(comando, capturar_salida=False):
    """Ejecuta un comando de yt-dlp de forma segura"""
    try:
        if capturar_salida:
            resultado = subprocess.run(
                comando,
                check=True,
                capture_output=True,
                text=True,
                timeout=300  # 5 minutos timeout
            )
            return True, resultado.stdout
        else:
            subprocess.run(comando, check=True, timeout=300)
            return True, None
            
    except subprocess.TimeoutExpired:
        print("\n⏱️  Timeout: La descarga está tardando demasiado")
        print("   Esto puede deberse a:")
        print("   - Archivo muy grande")
        print("   - Conexión lenta")
        print("   - Servidor del sitio lento")
        return False, None
        
    except subprocess.CalledProcessError as e:
        return False, e.stderr if capturar_salida else None


def formatear_titulo_seccion(titulo):
    """Formatea un título de sección para la consola"""
    ancho = 60
    return f"\n{'='*ancho}\n{titulo.center(ancho)}\n{'='*ancho}\n"


def mostrar_error_con_ayuda(mensaje_error, sugerencias=None):
    """Muestra un error con sugerencias de ayuda"""
    print(f"\n❌ {mensaje_error}")
    
    if sugerencias:
        print("\n💡 Sugerencias:")
        for i, sugerencia in enumerate(sugerencias, 1):
            print(f"   {i}. {sugerencia}")
    print()


def confirmar_accion(mensaje):
    """Pide confirmación al usuario"""
    while True:
        respuesta = input(f"\n{mensaje} (s/n): ").lower().strip()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("⚠️  Por favor responde 's' para sí o 'n' para no")


def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa hasta que el usuario presione Enter"""
    input("\n⏸  Presiona Enter para continuar...")


# Constantes útiles
SITIOS_POPULARES = {
    'facebook': ['facebook.com', 'fb.watch', 'fb.com'],
    'instagram': ['instagram.com'],
    'tiktok': ['tiktok.com'],
    'youtube': ['youtube.com', 'youtu.be'],
    'twitter': ['twitter.com', 'x.com'],
}


def detectar_plataforma(url):
    """Detecta la plataforma de una URL"""
    url_lower = url.lower()
    
    for plataforma, dominios in SITIOS_POPULARES.items():
        if any(dominio in url_lower for dominio in dominios):
            return plataforma
    
    return 'generico'


# Mensajes de ayuda reutilizables
AYUDA_COOKIES = """
📖 Para obtener cookies de Facebook:

1. Instala la extensión "Get cookies.txt LOCALLY" en tu navegador
2. Inicia sesión en Facebook
3. Haz clic en la extensión y exporta las cookies
4. Guarda el archivo como "facebook_cookies.txt"

💡 Lee GUIA_COOKIES.md para instrucciones detalladas
"""

AYUDA_INSTALACION = """
📦 Instalación rápida:

Linux/Mac:
   bash instalar.sh

Windows:
   instalar.bat

Manual:
   pip install yt-dlp
"""

AYUDA_ERRORES_COMUNES = """
🔧 Soluciones a errores comunes:

1. "URL inválida"
   → Copia la URL completa del navegador
   → Debe empezar con http:// o https://

2. "Video no disponible"
   → Verifica que el video exista
   → Puede requerir cookies si es privado

3. "Error de descarga"
   → Actualiza yt-dlp: pip install --upgrade yt-dlp
   → Prueba con cookies si es Facebook

4. "Permiso denegado"
   → Verifica permisos de escritura en la carpeta
   → Intenta cambiar la carpeta de destino
"""


if __name__ == "__main__":
    # Pruebas del módulo
    print("🧪 Probando módulo core...")
    
    try:
        verificar_python_version()
        print("✓ Versión de Python OK")
        
        verificar_dependencias()
        print("✓ Dependencias OK")
        
        # Prueba de validación de URL
        try:
            validar_url("https://www.youtube.com/watch?v=test")
            print("✓ Validación de URL OK")
        except ValidacionError as e:
            print(f"✗ Error en validación de URL: {e}")
        
        print("\n✅ Módulo core funcionando correctamente")
        
    except Exception as e:
        print(f"\n❌ Error en pruebas: {e}")
        sys.exit(1)
