#!/bin/bash

# MCP Prompt Optimizer Installation Script

echo "Installing MCP Prompt Optimizer dependencies..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not found. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "Error: Python $required_version or higher is required. Found: $python_version"
    exit 1
fi

# Check if we're in a virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "Warning: No virtual environment detected."
    echo "It's recommended to create a virtual environment:"
    echo "  python3 -m venv venv"
    echo "  source venv/bin/activate"
    echo ""
    read -p "Continue with global installation? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled. Please create a virtual environment first."
        exit 1
    fi
fi

# Install dependencies
echo "Installing dependencies..."
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
else
    pip3 install mcp>=0.1.0
fi

echo "Installation complete!"
echo ""
echo "Usage:"
echo "  python3 prompt_optimizer.py"
echo ""
echo "For Claude Desktop integration, add this server to your claude_desktop_config.json"