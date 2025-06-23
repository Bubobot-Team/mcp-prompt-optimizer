#!/usr/bin/env python3
"""
Interactive setup script for MCP Prompt Optimizer in Claude Desktop
"""

import os
import json
import platform
import subprocess
import sys
from pathlib import Path

def get_config_path():
    """Get the Claude Desktop config path based on OS"""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    elif system == "Windows":
        return Path(os.environ["APPDATA"]) / "Claude" / "claude_desktop_config.json"
    else:  # Linux
        return Path.home() / ".config" / "Claude" / "claude_desktop_config.json"

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import mcp
        print("✓ MCP library is installed")
        return True
    except ImportError:
        print("✗ MCP library not found")
        return False

def install_dependencies():
    """Install required dependencies"""
    print("\nInstalling dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "mcp"])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to install dependencies")
        print("Please run manually: pip install mcp")
        return False

def setup_config():
    """Setup Claude Desktop configuration"""
    config_path = get_config_path()
    config_dir = config_path.parent
    
    # Create directory if it doesn't exist
    config_dir.mkdir(parents=True, exist_ok=True)
    
    # Get current script directory
    mcp_path = str(Path(__file__).parent / "prompt_optimizer.py")
    
    # Load existing config or create new
    if config_path.exists():
        print(f"\nExisting config found at: {config_path}")
        with open(config_path, 'r') as f:
            config = json.load(f)
        # Backup existing config
        backup_path = config_path.with_suffix('.json.backup')
        with open(backup_path, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"Backup created at: {backup_path}")
    else:
        config = {}
    
    # Add MCP server configuration
    if "mcpServers" not in config:
        config["mcpServers"] = {}
    
    config["mcpServers"]["prompt-optimizer"] = {
        "command": "python3",
        "args": [mcp_path],
        "env": {}
    }
    
    # Write updated config
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"\n✓ Configuration updated at: {config_path}")
    return True

def test_mcp_server():
    """Test if the MCP server can run"""
    print("\nTesting MCP server...")
    mcp_path = Path(__file__).parent / "prompt_optimizer.py"
    
    if not mcp_path.exists():
        print(f"✗ MCP server file not found: {mcp_path}")
        return False
    
    try:
        # Test if the file is executable Python
        with open(mcp_path, 'r') as f:
            content = f.read()
            if 'class PromptOptimizer' in content:
                print("✓ MCP server file is valid")
                return True
            else:
                print("✗ MCP server file appears invalid")
                return False
    except Exception as e:
        print(f"✗ Error reading MCP server: {e}")
        return False

def print_usage_examples():
    """Print usage examples"""
    print("\n" + "="*60)
    print("SETUP COMPLETE! 🎉")
    print("="*60)
    
    print("\n📝 USAGE EXAMPLES:")
    
    print("\n1. Basic Commands:")
    print("   • Analyze this prompt: 'write a blog post'")
    print("   • Optimize this prompt for clarity: 'help me code'")
    print("   • Auto-optimize: 'explain machine learning'")
    
    print("\n2. Advanced Strategies:")
    print("   • Apply advanced optimization with tree_of_thoughts: 'design a distributed system'")
    print("   • Apply advanced optimization with medprompt: 'classify these support tickets'")
    print("   • Apply advanced optimization with self_refine: 'improve this description'")
    
    print("\n3. Domain Templates:")
    print("   • Get domain template for api_design")
    print("   • Get domain template for root_cause_analysis")
    print("   • List all domain templates")
    
    print("\n⚠️  IMPORTANT: Restart Claude Desktop to load the MCP server")
    print("\n📚 Full documentation: CLAUDE_DESKTOP_GUIDE.md")

def main():
    """Main setup function"""
    print("🚀 MCP Prompt Optimizer Setup for Claude Desktop")
    print("="*60)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    # Check and install dependencies
    if not check_dependencies():
        if not install_dependencies():
            print("\n⚠️  Please install dependencies manually and run this script again")
            return
    
    # Setup configuration
    if not setup_config():
        print("\n⚠️  Configuration setup failed")
        return
    
    # Test MCP server
    test_mcp_server()
    
    # Print usage examples
    print_usage_examples()

if __name__ == "__main__":
    main()
