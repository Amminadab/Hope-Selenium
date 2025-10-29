#!/bin/bash

# Setup script for Selenium Tests (Python)

echo "🚀 Setting up Selenium Tests (Python)..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run tests:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run a test: python tests/example_test.py"
echo "  3. Or run: python tests/support_ticket_test.py"
echo ""
echo "To deactivate the virtual environment: deactivate"
