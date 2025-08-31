#!/bin/bash

# M3U Scraper Production Setup Script
# This script sets up the M3U scraper for production use

echo "🔧 M3U Scraper Production Setup"
echo "================================"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 and try again"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create necessary directories
echo ""
echo "📁 Creating directory structure..."
mkdir -p logs output examples temp

# Create .gitkeep files to maintain directory structure while ignoring contents
echo "📋 Setting up git ignore patterns..."
touch output/.gitkeep
touch logs/.gitkeep

# Install dependencies
echo ""
echo "📦 Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
    # Try to install with --break-system-packages flag for externally managed environments
    python3 -m pip install -r requirements.txt --break-system-packages --quiet
    if [ $? -eq 0 ]; then
        echo "✅ Dependencies installed successfully"
    else
        echo "⚠️  Failed to install with --break-system-packages"
        echo "💡 Alternative: Create a virtual environment"
        echo "   python3 -m venv venv"
        echo "   source venv/bin/activate"
        echo "   pip install -r requirements.txt"
        echo ""
        echo "Continuing with setup..."
    fi
else
    echo "❌ requirements.txt not found"
    exit 1
fi

# Make scripts executable
echo ""
echo "🔧 Making scripts executable..."
chmod +x run.sh
chmod +x setup.sh

# Test installation
echo ""
echo "🧪 Testing installation..."
python3 test_installation.py

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Setup completed successfully!"
    echo ""
    echo "🚀 You can now run the application with:"
    echo "   ./run.sh"
    echo ""
    echo "📚 Documentation is available in the docs/ directory"
    echo "📁 Generated files will be saved to the output/ directory"
    echo "📋 Logs will be saved to the logs/ directory"
    echo ""
    echo "🔒 Security Note: Output files are excluded from git for privacy"
else
    echo ""
    echo "❌ Setup failed. Please check the errors above."
    exit 1
fi 