#!/bin/bash

# M3U Scraper Launcher Script
# This script launches the M3U scraper application

echo "🚀 Starting M3U Scraper..."
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 and try again"
    exit 1
fi

# Check if required files exist
if [ ! -f "src/main.py" ]; then
    echo "❌ Error: src/main.py not found"
    echo "Please run this script from the M3U Scraper directory"
    exit 1
fi

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "📦 Checking dependencies..."
    python3 -m pip install -r requirements.txt --break-system-packages --quiet
fi

# Create necessary directories
mkdir -p logs output

# Run the application
echo "🎯 Launching M3U Scraper application..."
echo ""
cd src && python3 main.py 