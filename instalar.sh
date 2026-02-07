#!/bin/bash
# Script de instalación y configuración automática
# Descargador de Videos Mejorado

echo "=========================================="
echo "📥 INSTALADOR - Descargador de Videos"
echo "=========================================="
echo ""

# Detectar sistema operativo
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    OS="Windows"
else
    OS="Desconocido"
fi

echo "🖥️  Sistema operativo detectado: $OS"
echo ""

# Verificar Python
echo "🔍 Verificando Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ $PYTHON_VERSION encontrado"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version)
    echo "✅ $PYTHON_VERSION encontrado"
    PYTHON_CMD="python"
else
    echo "❌ Python no encontrado"
    echo "Por favor instala Python 3.6 o superior desde https://www.python.org"
    exit 1
fi

echo ""

# Verificar pip
echo "🔍 Verificando pip..."
if $PYTHON_CMD -m pip --version &> /dev/null; then
    PIP_VERSION=$($PYTHON_CMD -m pip --version)
    echo "✅ $PIP_VERSION encontrado"
else
    echo "❌ pip no encontrado"
    echo "Instalando pip..."
    $PYTHON_CMD -m ensurepip --upgrade
fi

echo ""

# Instalar yt-dlp
echo "📦 Instalando/Actualizando yt-dlp..."
$PYTHON_CMD -m pip install --upgrade yt-dlp

if [ $? -eq 0 ]; then
    echo "✅ yt-dlp instalado correctamente"
else
    echo "❌ Error al instalar yt-dlp"
    exit 1
fi

echo ""

# Verificar ffmpeg
echo "🔍 Verificando ffmpeg..."
if command -v ffmpeg &> /dev/null; then
    FFMPEG_VERSION=$(ffmpeg -version | head -n 1)
    echo "✅ ffmpeg encontrado: $FFMPEG_VERSION"
else
    echo "⚠️  ffmpeg no encontrado (opcional pero recomendado)"
    echo ""
    echo "Para instalar ffmpeg:"
    if [[ "$OS" == "Linux" ]]; then
        echo "  sudo apt install ffmpeg  (Ubuntu/Debian)"
        echo "  sudo yum install ffmpeg  (CentOS/RHEL)"
    elif [[ "$OS" == "macOS" ]]; then
        echo "  brew install ffmpeg"
    elif [[ "$OS" == "Windows" ]]; then
        echo "  Descarga desde: https://ffmpeg.org/download.html"
    fi
fi

echo ""

# Crear directorios de descarga
echo "📁 Creando directorios de descarga..."
mkdir -p ~/Descargas/Videos
mkdir -p ~/Descargas/Facebook_Videos
echo "✅ Directorios creados"

echo ""

# Dar permisos de ejecución (Linux/Mac)
if [[ "$OS" != "Windows" ]]; then
    echo "🔐 Configurando permisos de ejecución..."
    chmod +x descargar_videos.py 2>/dev/null
    chmod +x facebook_descargador.py 2>/dev/null
    echo "✅ Permisos configurados"
    echo ""
fi

# Resumen
echo "=========================================="
echo "✅ INSTALACIÓN COMPLETADA"
echo "=========================================="
echo ""
echo "📋 Resumen de instalación:"
echo "  ✓ Python detectado"
echo "  ✓ pip verificado"
echo "  ✓ yt-dlp instalado/actualizado"
if command -v ffmpeg &> /dev/null; then
    echo "  ✓ ffmpeg disponible"
else
    echo "  ⚠ ffmpeg no instalado (opcional)"
fi
echo "  ✓ Directorios de descarga creados"
echo ""
echo "🚀 Para empezar a usar:"
echo "  $PYTHON_CMD descargar_videos.py"
echo ""
echo "📱 Para Facebook específicamente:"
echo "  $PYTHON_CMD facebook_descargador.py"
echo ""
echo "📖 Lee el README.md para más información"
echo "=========================================="
