@echo off
REM Script de instalación para Windows
REM Descargador de Videos Mejorado

echo ==========================================
echo 📥 INSTALADOR - Descargador de Videos
echo ==========================================
echo.

REM Verificar Python
echo 🔍 Verificando Python...
python --version >nul 2>&1
if %ERRORLEVEL% == 0 (
    echo ✅ Python encontrado
    set PYTHON_CMD=python
) else (
    python3 --version >nul 2>&1
    if %ERRORLEVEL% == 0 (
        echo ✅ Python3 encontrado
        set PYTHON_CMD=python3
    ) else (
        echo ❌ Python no encontrado
        echo Por favor instala Python desde https://www.python.org
        pause
        exit /b 1
    )
)

echo.

REM Verificar pip
echo 🔍 Verificando pip...
%PYTHON_CMD% -m pip --version >nul 2>&1
if %ERRORLEVEL% == 0 (
    echo ✅ pip encontrado
) else (
    echo ❌ pip no encontrado
    echo Instalando pip...
    %PYTHON_CMD% -m ensurepip --upgrade
)

echo.

REM Instalar yt-dlp
echo 📦 Instalando/Actualizando yt-dlp...
%PYTHON_CMD% -m pip install --upgrade yt-dlp
if %ERRORLEVEL% == 0 (
    echo ✅ yt-dlp instalado correctamente
) else (
    echo ❌ Error al instalar yt-dlp
    pause
    exit /b 1
)

echo.

REM Verificar ffmpeg
echo 🔍 Verificando ffmpeg...
ffmpeg -version >nul 2>&1
if %ERRORLEVEL% == 0 (
    echo ✅ ffmpeg encontrado
) else (
    echo ⚠️  ffmpeg no encontrado (opcional pero recomendado)
    echo.
    echo Para instalar ffmpeg:
    echo   Descarga desde: https://ffmpeg.org/download.html
    echo   O instala con chocolatey: choco install ffmpeg
)

echo.

REM Crear directorios
echo 📁 Creando directorios de descarga...
if not exist "%USERPROFILE%\Downloads\Videos" mkdir "%USERPROFILE%\Downloads\Videos"
if not exist "%USERPROFILE%\Downloads\Facebook_Videos" mkdir "%USERPROFILE%\Downloads\Facebook_Videos"
echo ✅ Directorios creados

echo.
echo ==========================================
echo ✅ INSTALACIÓN COMPLETADA
echo ==========================================
echo.
echo 📋 Resumen de instalación:
echo   ✓ Python detectado
echo   ✓ pip verificado
echo   ✓ yt-dlp instalado/actualizado
echo   ✓ Directorios de descarga creados
echo.
echo 🚀 Para empezar a usar:
echo   %PYTHON_CMD% descargar_videos.py
echo.
echo 📱 Para Facebook específicamente:
echo   %PYTHON_CMD% facebook_descargador.py
echo.
echo 📖 Lee el README.md para más información
echo ==========================================
echo.
pause
