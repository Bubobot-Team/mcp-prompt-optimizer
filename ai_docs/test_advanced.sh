#!/bin/bash
# Advanced test script for MCP Prompt Optimizer

echo "Running Advanced MCP Prompt Optimizer Tests..."
echo "============================================="

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python version: $python_version"
echo

# Run basic tests first
echo "1. Running basic functionality tests..."
python3 test.sh
echo

# Run advanced tests
echo "2. Running advanced feature tests..."
python3 test_advanced.py
echo

# Check file sizes to ensure everything was created
echo "3. Checking created files..."
echo "File sizes:"
ls -lh *.py | grep -E "(advanced_strategies|domain_templates|test_advanced)"
echo

echo "============================================="
echo "Advanced testing complete!"
echo
echo "To integrate with Claude Desktop:"
echo "1. Update your claude_desktop_config.json with the path to prompt_optimizer.py"
echo "2. Restart Claude Desktop"
echo "3. Try commands like:"
echo "   - 'Apply advanced optimization with tree_of_thoughts: [your prompt]'"
echo "   - 'Get domain template for api_design'"
echo "   - 'List all domain templates'"
