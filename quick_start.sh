#!/bin/bash

# Data Science Playground - Quick Start Script
# This script sets up a virtual environment and installs dependencies

echo "🚀 Setting up Data Science Playground..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python version: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "ℹ️  Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip --quiet
echo "✅ pip upgraded"
echo ""

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt --quiet
echo "✅ Dependencies installed"
echo ""

# Install package in development mode
echo "🔧 Installing package in development mode..."
pip install -e . --quiet
echo "✅ Package installed"
echo ""

echo "🎉 Setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Activate the virtual environment: source venv/bin/activate"
echo "   2. Start Jupyter: jupyter notebook"
echo "   3. Open notebooks/getting_started.ipynb"
echo ""
echo "Happy Data Exploring! 🚀"

