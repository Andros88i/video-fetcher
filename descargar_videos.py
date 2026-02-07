#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script mejorado para descargar videos de múltiples plataformas
Optimizado especialmente para Facebook, Instagram, TikTok, YouTube y más
"""

import sys
from pathlib import Path

# Importar módulo core con manejo de errores
try:
    from core import (
        verificar_dependencias,
        validar_url,
        validar_archivo_cookies,
        crear_directorio_seguro,
        leer_urls_de_archivo,
        ejecutar_comando_ytdlp,
        detectar_plataforma,
        mostrar_error_con_ayuda,
        confirmar_accion,
        pausar,
        formatear_titulo_seccion,
        ValidacionError,
        DependenciaError,
        AYUDA_COOKIES,
        AYUDA_ERRORES_COMUNES
    )
except ImportError:
    print("❌ Error: No se encuentra el módulo 'core.py'")
    print("   Asegúrate de que core.py esté en el mismo directorio")
    sys.exit(1)


class DescargadorVideos:
    def __init__(self):
        try:
            self.directorio_descargas = crear_directorio_seguro(
                Path.home() / "Descargas" / "Videos"
            )
            self.archivo_cookies = None
            print(f"📁 Directorio de descargas: {self.directorio_descargas}")
        except ValidacionError as e:
            print(str(e))
            sys.exit(1)
    
    def obtener_opciones_base(self):
        """Opciones base optimizadas para todas las plataformas"""
        opciones = [
            "--no-warnings",
            "--no-check-certificate",
            "--prefer-free-formats",
            "--add-metadata",
            "--embed-thumbnail",
            "--embed-subs",
            "--sub-langs", "es,en",
            "--convert-subs", "srt",
            "-o", str(self.directorio_descargas / "%(title)s.%(ext)s"),
        ]
        
        # Agregar cookies si existen
        if self.archivo_cookies and os.path.exists(self.archivo_cookies):
            opciones.extend(["--cookies", self.archivo_cookies])
        
        return opciones
    
    def obtener_opciones_facebook(self):
        """Opciones específicas optimizadas para Facebook"""
        return [
            "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "--referer", "https://www.facebook.com/",
            "--format", "best",
            "--http-chunk-size", "10M",
            "--retries", "10",
            "--fragment-retries", "10",
            "--extractor-args", "facebook:api_version=v13.0",
        ]
    
    def obtener_opciones_instagram(self):
        """Opciones específicas para Instagram"""
        return [
            "--format", "best",
            "--user-agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15",
        ]
    
    def obtener_opciones_tiktok(self):
        """Opciones específicas para TikTok"""
        return [
            "--format", "best",
            "--extractor-args", "tiktok:api_hostname=api16-normal-c-useast1a.tiktokv.com",
        ]
    
    def obtener_opciones_youtube(self):
        """Opciones específicas para YouTube"""
        return [
            "--format", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "--merge-output-format", "mp4",
        ]
    
    def descargar_video(self, url):
        """Descarga el video con opciones optimizadas según la plataforma"""
        try:
            # Validar URL
            url = validar_url(url)
            plataforma = detectar_plataforma(url)
            
            print(formatear_titulo_seccion(f"🎯 Plataforma: {plataforma.upper()}"))
            
            # Construir comando
            comando = ["yt-dlp"] + self.obtener_opciones_base()
            
            # Agregar opciones específicas de plataforma
            if plataforma == "facebook":
                comando.extend(self.obtener_opciones_facebook())
            elif plataforma == "instagram":
                comando.extend(self.obtener_opciones_instagram())
            elif plataforma == "tiktok":
                comando.extend(self.obtener_opciones_tiktok())
            elif plataforma == "youtube":
                comando.extend(self.obtener_opciones_youtube())
            
            comando.append(url)
            
            # Intentar descarga
            print(f"\n📥 Descargando video...")
            print(f"📁 Guardando en: {self.directorio_descargas}")
            
            exito, _ = ejecutar_comando_ytdlp(comando)
            
            if exito:
                print("\n✅ ¡Video descargado exitosamente!")
                return True
            else:
                # Intentar métodos alternativos
                print("\n⚠️  Descarga falló, intentando métodos alternativos...")
                if plataforma == "facebook":
                    return self.intentar_descarga_facebook_alternativa(url)
                else:
                    return self.intentar_descarga_genérica(url)
                    
        except ValidacionError as e:
            mostrar_error_con_ayuda(
                str(e),
                [
                    "Copia la URL completa desde tu navegador",
                    "Verifica que el video exista y sea accesible",
                    "Para videos privados, configura cookies (opción 3)"
                ]
            )
            return False
        except Exception as e:
            mostrar_error_con_ayuda(
                f"Error inesperado: {e}",
                [
                    "Actualiza yt-dlp con la opción 4 del menú",
                    "Verifica tu conexión a internet",
                    "Lee README.md para más ayuda"
                ]
            )
            return False
    
    def configurar_cookies_facebook(self):
        """Configura el archivo de cookies para Facebook"""
        print(formatear_titulo_seccion("🍪 CONFIGURACIÓN DE COOKIES"))
        print(AYUDA_COOKIES)
        
        ruta_cookies = input("Ruta del archivo de cookies (Enter para omitir): ").strip()
        
        if not ruta_cookies:
            print("\n⚠️  Continuando sin cookies")
            print("   Nota: Algunos videos privados pueden no descargarse")
            return
        
        try:
            self.archivo_cookies = validar_archivo_cookies(ruta_cookies)
            print(f"\n✅ Cookies configuradas correctamente")
            print(f"   Archivo: {Path(self.archivo_cookies).name}")
        except ValidacionError as e:
            print(f"\n{e}")
            print("\n💡 Revisa GUIA_COOKIES.md para ayuda detallada")
            self.archivo_cookies = None
    
    def intentar_descarga_facebook_alternativa(self, url):
        """Intenta métodos alternativos para Facebook"""
        print("\n🔄 Intentando métodos alternativos para Facebook...")
        
        metodos = [
            ("Mejor calidad disponible", ["yt-dlp", "--format", "best"]),
            ("Calidad media", ["yt-dlp", "--format", "worst"]),
            ("HD 720p", ["yt-dlp", "--format", "bestvideo[height<=720]+bestaudio/best"]),
        ]
        
        for i, (nombre, comando_base) in enumerate(metodos, 1):
            print(f"\n⏳ Método {i}/3: {nombre}...")
            comando = comando_base + [
                "-o", str(self.directorio_descargas / "%(title)s.%(ext)s"),
                url
            ]
            
            exito, _ = ejecutar_comando_ytdlp(comando)
            if exito:
                print(f"✅ ¡Descarga exitosa con: {nombre}!")
                return True
        
        mostrar_error_con_ayuda(
            "No se pudo descargar con ningún método alternativo",
            [
                "Verifica que la URL sea correcta",
                "Intenta configurar cookies (opción 3 del menú)",
                "Lee GUIA_COOKIES.md si es un video privado",
                "Prueba facebook_descargador.py para más opciones"
            ]
        )
        return False
    
    def intentar_descarga_genérica(self, url):
        """Intenta descarga genérica simplificada"""
        print("\n🔄 Intentando descarga simplificada...")
        
        comando = [
            "yt-dlp",
            "--format", "best",
            "-o", str(self.directorio_descargas / "%(title)s.%(ext)s"),
            url
        ]
        
        exito, _ = ejecutar_comando_ytdlp(comando)
        
        if exito:
            print("✅ ¡Video descargado exitosamente!")
            return True
        else:
            mostrar_error_con_ayuda(
                "No se pudo descargar el video",
                [
                    "Actualiza yt-dlp (opción 4 del menú)",
                    "Verifica que el video esté disponible",
                    "Prueba con otra URL",
                    "Lee README.md para más ayuda"
                ]
            )
            return False
    
    def descargar_multiples(self, archivo_urls):
        """Descarga múltiples videos desde un archivo"""
        try:
            urls = leer_urls_de_archivo(archivo_urls)
            
            total = len(urls)
            exitosos = 0
            fallidos = []
            
            print(formatear_titulo_seccion(f"📋 DESCARGA MASIVA: {total} videos"))
            
            for i, url in enumerate(urls, 1):
                print(f"\n{'='*60}")
                print(f"📹 Video {i}/{total}")
                print(f"{'='*60}")
                print(f"🔗 {url[:70]}..." if len(url) > 70 else f"🔗 {url}")
                
                if self.descargar_video(url):
                    exitosos += 1
                else:
                    fallidos.append((i, url))
            
            # Resumen final
            print(formatear_titulo_seccion("📊 RESUMEN DE DESCARGAS"))
            print(f"✅ Exitosas: {exitosos}/{total}")
            print(f"❌ Fallidas: {len(fallidos)}/{total}")
            
            if fallidos:
                print("\n❌ Videos que fallaron:")
                for num, url_fallida in fallidos:
                    print(f"   {num}. {url_fallida[:60]}...")
                
                if confirmar_accion("\n¿Guardar lista de URLs fallidas?"):
                    self._guardar_urls_fallidas(fallidos)
                    
        except ValidacionError as e:
            mostrar_error_con_ayuda(
                str(e),
                [
                    "Verifica que el archivo exista",
                    "El archivo debe tener una URL por línea",
                    "Revisa ejemplo_urls.txt como referencia"
                ]
            )
    
    def _guardar_urls_fallidas(self, fallidos):
        """Guarda las URLs que fallaron en un archivo"""
        try:
            archivo_fallidos = self.directorio_descargas / "urls_fallidas.txt"
            with open(archivo_fallidos, 'w', encoding='utf-8') as f:
                f.write("# URLs que fallaron en la descarga\n")
                f.write(f"# Total: {len(fallidos)}\n\n")
                for num, url in fallidos:
                    f.write(f"{url}\n")
            
            print(f"\n💾 URLs fallidas guardadas en:")
            print(f"   {archivo_fallidos}")
        except Exception as e:
            print(f"\n⚠️  No se pudieron guardar URLs fallidas: {e}")
    
    def menu_principal(self):
        """Muestra el menú principal"""
        print(formatear_titulo_seccion("🎬 DESCARGADOR DE VIDEOS"))
        print("📱 Plataformas soportadas:")
        print("   • Facebook (fb.com, facebook.com, fb.watch)")
        print("   • Instagram")
        print("   • TikTok")
        print("   • YouTube")
        print("   • Twitter/X")
        print("   • +1000 sitios más")
        
        if self.archivo_cookies:
            print(f"\n🍪 Cookies: ✓ {Path(self.archivo_cookies).name}")
        else:
            print("\n🍪 Cookies: ✗ No configuradas")
        
        print("\n📋 OPCIONES:")
        print("   1. Descargar un video")
        print("   2. Descargar múltiples videos (desde archivo)")
        print("   3. Configurar cookies de Facebook")
        print("   4. Actualizar yt-dlp")
        print("   5. Ver ayuda")
        print("   6. Salir")
        
        return input("\n👉 Elige una opción (1-6): ").strip()
    
    def actualizar_ytdlp(self):
        """Actualiza yt-dlp a la última versión"""
        print(formatear_titulo_seccion("🔄 ACTUALIZACIÓN"))
        print("Actualizando yt-dlp a la última versión...\n")
        
        try:
            import subprocess
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"],
                check=True
            )
            print("\n✅ yt-dlp actualizado correctamente")
            print("💡 Se recomienda actualizar semanalmente")
        except subprocess.CalledProcessError:
            mostrar_error_con_ayuda(
                "Error al actualizar yt-dlp",
                [
                    "Verifica tu conexión a internet",
                    "Intenta manualmente: pip install --upgrade yt-dlp",
                    "Consulta README.md para más información"
                ]
            )
    
    def mostrar_ayuda(self):
        """Muestra información de ayuda"""
        print(formatear_titulo_seccion("📖 AYUDA"))
        
        print("🎯 USO BÁSICO:")
        print("   1. Copia la URL completa del video desde tu navegador")
        print("   2. Selecciona opción 1 en el menú")
        print("   3. Pega la URL y presiona Enter")
        print()
        print("📁 DESCARGA MÚLTIPLE:")
        print("   1. Crea un archivo .txt con una URL por línea")
        print("   2. Usa ejemplo_urls.txt como referencia")
        print("   3. Selecciona opción 2 en el menú")
        print()
        print("🍪 PARA FACEBOOK:")
        print("   - Videos públicos: No necesitas cookies")
        print("   - Videos privados: Configura cookies (opción 3)")
        print("   - Lee GUIA_COOKIES.md para instrucciones detalladas")
        print()
        print("📖 DOCUMENTACIÓN:")
        print("   - README.md: Guía completa")
        print("   - GUIA_COOKIES.md: Tutorial de cookies")
        print("   - ejemplo_urls.txt: Plantilla para descargas masivas")
        print()
        print(AYUDA_ERRORES_COMUNES)
        pausar()    
    def ejecutar(self):
        """Ejecuta el descargador"""
        # Verificar dependencias al inicio
        if not verificar_dependencias():
            sys.exit(1)
        
        while True:
            try:
                opcion = self.menu_principal()
                
                if opcion == "1":
                    url = input("\n📎 Ingresa la URL del video: ").strip()
                    if url:
                        self.descargar_video(url)
                    else:
                        print("⚠️  No ingresaste ninguna URL")
                
                elif opcion == "2":
                    print("\n📋 DESCARGA MÚLTIPLE")
                    print("💡 El archivo debe tener una URL por línea")
                    print("   Revisa ejemplo_urls.txt como referencia\n")
                    archivo = input("📄 Ruta del archivo con URLs: ").strip()
                    if archivo:
                        self.descargar_multiples(archivo)
                    else:
                        print("⚠️  No ingresaste ninguna ruta")
                
                elif opcion == "3":
                    self.configurar_cookies_facebook()
                
                elif opcion == "4":
                    self.actualizar_ytdlp()
                
                elif opcion == "5":
                    self.mostrar_ayuda()
                    continue  # No pausar después de la ayuda
                
                elif opcion == "6":
                    print(formatear_titulo_seccion("👋 ¡HASTA LUEGO!"))
                    print("Gracias por usar el descargador de videos")
                    print("Si tienes sugerencias, revisa el README.md")
                    break
                
                else:
                    print("\n⚠️  Opción no válida. Elige un número del 1 al 6")
                
                pausar()
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Operación cancelada por el usuario")
                if confirmar_accion("¿Deseas salir del programa?"):
                    break
                else:
                    continue
