#!/bin/bash
# Script to find and setup Claude Desktop configuration

echo "Setting up MCP Prompt Optimizer for Claude Desktop"
echo "=================================================="

# Detect OS and find config location
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    CONFIG_PATH="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
    echo "Detected macOS"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    CONFIG_PATH="$APPDATA/Claude/claude_desktop_config.json"
    echo "Detected Windows"
else
    # Linux
    CONFIG_PATH="$HOME/.config/Claude/claude_desktop_config.json"
    echo "Detected Linux"
fi

echo "Configuration file location: $CONFIG_PATH"

# Create config directory if it doesn't exist
CONFIG_DIR=$(dirname "$CONFIG_PATH")
if [ ! -d "$CONFIG_DIR" ]; then
    echo "Creating configuration directory..."
    mkdir -p "$CONFIG_DIR"
fi

# Get the full path to the MCP server
MCP_PATH="/Users/phongpham/Project/boldlab/mcp-prompt-optimizer/prompt_optimizer.py"
echo "MCP Server path: $MCP_PATH"

# Create or update the configuration
if [ -f "$CONFIG_PATH" ]; then
    echo "Existing configuration found. Creating backup..."
    cp "$CONFIG_PATH" "$CONFIG_PATH.backup"
fi

# Generate the configuration
cat > "$CONFIG_PATH" << EOF
{
  "mcpServers": {
    "prompt-optimizer": {
      "command": "python3",
      "args": ["$MCP_PATH"],
      "env": {}
    }
  }
}
EOF

echo "Configuration updated successfully!"
echo
echo "Next steps:"
echo "1. Make sure Python dependencies are installed:"
echo "   cd /Users/phongpham/Project/boldlab/mcp-prompt-optimizer"
echo "   pip install mcp"
echo
echo "2. Restart Claude Desktop"
echo
echo "3. Test by typing in Claude:"
echo "   'Analyze this prompt: write a blog post'"
echo "   'Apply advanced optimization with tree_of_thoughts: design a distributed system'"
echo "   'Get domain template for api_design'"
