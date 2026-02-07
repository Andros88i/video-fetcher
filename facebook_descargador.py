#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script especializado para descargar videos de Facebook
Incluye múltiples métodos y técnicas para manejar errores
"""

import subprocess
import sys
import os
from pathlib import Path
import re

class DescargadorFacebook:
    def __init__(self):
        self.directorio_descargas = Path.home() / "Descargas" / "Facebook_Videos"
        self.directorio_descargas.mkdir(parents=True, exist_ok=True)
    
    def limpiar_url_facebook(self, url):
        """Limpia y normaliza URLs de Facebook"""
        # Eliminar parámetros innecesarios
        url = re.sub(r'[?&](mibextid|app|source|paipv)=[^&]*', '', url)
        
        # Convertir fb.watch a URL completa
        if 'fb.watch' in url:
            video_id = url.split('/')[-1].split('?')[0]
            url = f"https://www.facebook.com/watch/?v={video_id}"
        
        return url
    
    def metodo_1_basico(self, url):
        """Método 1: Descarga básica con mejor formato"""
        print("\n[Método 1] Descarga básica optimizada...")
        comando = [
            "yt-dlp",
            "--format", "best",
            "--no-warnings",
            "-o", str(self.directorio_descargas / "%(title)s.%(ext)s"),
            url
        ]
        
        try:
            subprocess.run(comando, check=True, capture_output=False)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def metodo_2_con_headers(self, url):
        """Método 2: Con headers y user-agent específicos"""
        print("\n[Método 2] Con headers personalizados...")
        comando = [
            "yt-dlp",
            "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "--referer", "https://www.facebook.com/",
            "--add-header", "Accept-Language:es-ES,es;q=0.9,en;q=0.8",
            "--add-header", "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "--format", "best",
            "--no-check-certificate",
            "-o", str(self.directorio_descargas / "%(title)s.%(ext)s"),
            url
        ]
        
        try:
            subprocess.run(comando, check=True, capture_output=False)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def metodo_3_api_version(self, url):
        """Método 3: Con versión específica de API"""
        print("\n[Método 3] Con configuración de API...")
        comando = [
            "yt-dlp",
            "--extractor-args", "facebook:api_version=v13.0",
            "--format", "best",
            "--http-chunk-size", "10M",
            "--retries", "15",
            "--fragment-retries", "15",
            "-o", str(self.directorio_descargas / "%(title)s.%(ext)s"),
            url
        ]
        
        try:
            subprocess.run(comando, check=True, capture_output=False)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def metodo_4_formato_especifico(self, url):
        """Método 4: Probando diferentes formatos"""
        print("\n[Método 4] Probando formatos alternativos...")
        
        formatos = [
            "bestvideo[height<=720]+bestaudio/best[height<=720]",
            "worst",
            "bestvideo+bestaudio",
            "mp4",
        ]
        
        for formato in formatos:
            print(f"  Probando formato: {formato}")
            comando = [
                "yt-dlp",
                "--format", formato,
                "--merge-output-format", "mp4",
                "-o", str(self.directorio_descargas / "%(title)s.%(ext)s"),
                url
            ]
            
            try:
                subprocess.run(comando, check=True, capture_output=True)
                print(f"  ✓ Éxito con formato: {formato}")
                return True
            except subprocess.CalledProcessError:
                continue
        
        return False
    
    def metodo_5_cookies(self, url, archivo_cookies):
        """Método 5: Con cookies de sesión"""
        if not archivo_cookies or not os.path.exists(archivo_cookies):
            print("\n[Método 5] Cookies no disponibles, omitiendo...")
            return False
        
        print("\n[Método 5] Usando cookies de sesión...")
        comando = [
            "yt-dlp",
            "--cookies", archivo_cookies,
            "--format", "best",
            "-o", str(self.directorio_descargas / "%(title)s.%(ext)s"),
            url
        ]
        
        try:
            subprocess.run(comando, check=True, capture_output=False)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def metodo_6_extraccion_directa(self, url):
        """Método 6: Extracción directa sin descarga"""
        print("\n[Método 6] Obteniendo URL directa del video...")
        comando = [
            "yt-dlp",
            "--get-url",
            "--format", "best",
            url
        ]
        
        try:
            resultado = subprocess.run(comando, check=True, 
                                     capture_output=True, text=True)
            url_directa = resultado.stdout.strip()
            
            if url_directa:
                print(f"\n✓ URL directa obtenida:")
                print(f"  {url_directa}")
                print("\nPuedes descargar directamente con wget o curl:")
                print(f"  wget -O video.mp4 '{url_directa}'")
                return True
        except subprocess.CalledProcessError:
            return False
        
        return False
    
    def descargar_con_todos_los_metodos(self, url):
        """Intenta descargar usando todos los métodos disponibles"""
        url = self.limpiar_url_facebook(url)
        print(f"\n📎 URL limpia: {url}")
        print(f"📁 Carpeta de descarga: {self.directorio_descargas}")
        
        # Preguntar por cookies
        archivo_cookies = None
        usar_cookies = input("\n¿Tienes un archivo de cookies de Facebook? (s/n): ").lower()
        if usar_cookies == 's':
            archivo_cookies = input("Ruta del archivo de cookies: ").strip()
        
        metodos = [
            ("Básico", lambda: self.metodo_1_basico(url)),
            ("Headers personalizados", lambda: self.metodo_2_con_headers(url)),
            ("API configurada", lambda: self.metodo_3_api_version(url)),
            ("Formatos alternativos", lambda: self.metodo_4_formato_especifico(url)),
            ("Con cookies", lambda: self.metodo_5_cookies(url, archivo_cookies)),
            ("Extracción URL directa", lambda: self.metodo_6_extraccion_directa(url)),
        ]
        
        print("\n" + "="*60)
        print("🚀 Iniciando descarga con múltiples métodos...")
        print("="*60)
        
        for nombre, metodo in metodos:
            try:
                if metodo():
                    print(f"\n✅ ¡Descarga exitosa con método: {nombre}!")
                    return True
            except Exception as e:
                print(f"❌ Error en método {nombre}: {str(e)}")
                continue
        
        print("\n" + "="*60)
        print("❌ No se pudo descargar con ningún método")
        print("="*60)
        print("\n💡 Sugerencias:")
        print("  1. Verifica que la URL sea correcta y el video esté disponible")
        print("  2. Intenta copiar las cookies de tu navegador")
        print("  3. Verifica que el video no sea privado")
        print("  4. Actualiza yt-dlp: pip install --upgrade yt-dlp")
        
        return False
    
    def obtener_info_video(self, url):
        """Obtiene información del video sin descargarlo"""
        print("\n📋 Obteniendo información del video...")
        comando = [
            "yt-dlp",
            "--dump-json",
            "--no-warnings",
            url
        ]
        
        try:
            resultado = subprocess.run(comando, check=True, 
                                     capture_output=True, text=True)
            import json
            info = json.loads(resultado.stdout)
            
            print("\n" + "="*60)
            print("📊 INFORMACIÓN DEL VIDEO")
            print("="*60)
            print(f"Título: {info.get('title', 'N/A')}")
            print(f"Duración: {info.get('duration', 'N/A')} segundos")
            print(f"Vistas: {info.get('view_count', 'N/A')}")
            print(f"Autor: {info.get('uploader', 'N/A')}")
            
            if 'formats' in info:
                print(f"\nFormatos disponibles: {len(info['formats'])}")
                print("\nMejores calidades:")
                for fmt in info['formats'][:5]:
                    print(f"  - {fmt.get('format_id')}: {fmt.get('format_note', 'N/A')}")
            
            print("="*60)
            return True
            
        except subprocess.CalledProcessError:
            print("❌ No se pudo obtener información del video")
            return False
        except Exception as e:
            print(f"❌ Error al procesar información: {e}")
            return False


def menu():
    """Menú principal"""
    descargador = DescargadorFacebook()
    
    while True:
        print("\n" + "="*60)
        print("📱 DESCARGADOR ESPECIALIZADO DE FACEBOOK")
        print("="*60)
        print("\n1. Descargar video (todos los métodos)")
        print("2. Obtener información del video")
        print("3. Actualizar yt-dlp")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ").strip()
        
        if opcion == "1":
            url = input("\n📎 URL del video de Facebook: ").strip()
            if url:
                descargador.descargar_con_todos_los_metodos(url)
            else:
                print("❌ URL no válida")
        
        elif opcion == "2":
            url = input("\n📎 URL del video de Facebook: ").strip()
            if url:
                descargador.obtener_info_video(url)
            else:
                print("❌ URL no válida")
        
        elif opcion == "3":
            print("\n🔄 Actualizando yt-dlp...")
            try:
                subprocess.run([sys.executable, "-m", "pip", 
                              "install", "--upgrade", "yt-dlp"], check=True)
                print("✅ yt-dlp actualizado")
            except:
                print("❌ Error al actualizar")
        
        elif opcion == "4":
            print("\n👋 ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción no válida")
        
        input("\n⏸ Presiona Enter para continuar...")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido")
        sys.exit(0)
