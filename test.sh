#!/bin/bash
# Test script for the MCP Prompt Optimizer

echo "Testing MCP Prompt Optimizer..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python version: $python_version"

# Run the examples
echo -e "\nRunning examples..."
python3 examples.py

# Check if the main script runs without errors
echo -e "\nChecking main script..."
python3 -c "from prompt_optimizer import PromptOptimizer; print('✓ Import successful')"

echo -e "\nTest complete!"
echo "To use this MCP with Claude Desktop, add the configuration to your claude_desktop_config.json"
