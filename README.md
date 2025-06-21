# MCP Prompt Optimizer

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)

> A professional-grade MCP (Model Context Protocol) server that provides cutting-edge prompt optimization tools with research-backed strategies delivering 15-74% performance improvements.

## ✨ Features

### 🎯 Basic Optimization Strategies

- **Clarity**: Simplifies prompts for directness and precision
- **Specificity**: Adds detailed constraints and requirements
- **Chain of Thought**: Incorporates step-by-step reasoning
- **Few-Shot**: Includes example formats for guidance
- **Structured Output**: Defines clear output organization
- **Role-Based**: Adds expert role context

### 🚀 Advanced Optimization Strategies

- **Tree of Thoughts (ToT)**: Multi-path reasoning with 74% success rate on complex tasks
- **Constitutional AI**: Self-critique and alignment with safety principles
- **Automatic Prompt Engineer (APE)**: AI-discovered optimal instruction patterns
- **Meta-Prompting**: AI generates its own optimized prompts
- **Self-Refine**: Iterative improvement with 20% performance gains
- **TEXTGRAD**: Natural language feedback as optimization gradients
- **Medprompt**: Multi-technique ensemble achieving 90%+ accuracy
- **PromptWizard**: Feedback-driven self-evolving prompts

### 📋 Professional Domain Templates

Production-ready templates across 11 domains:

- **Business Analysis**: Competitive analysis frameworks
- **Product Management**: User research synthesis
- **Content Creation**: Technical blog posts with SEO optimization
- **Development**: Comprehensive code review checklists
- **Communication**: Stakeholder updates and project reports
- **Strategy**: OKR planning frameworks
- **Operations**: Standard Operating Procedures (SOPs)
- **Legal**: Contract termination and compliance
- **Customer Experience**: Feedback surveys and insights
- **Data Analysis**: Data insights and reporting
- **Meeting Management**: Effective meeting agendas

## 🛠️ Installation

### Quick Setup

```bash
# Clone the repository
git clone <repository-url>
cd mcp-prompt-optimizer

# Install dependencies
pip install mcp

# Configure Claude Desktop
python3 ai_docs/setup_interactive.py
```

### Manual Configuration

Add to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "prompt-optimizer": {
      "command": "python3",
      "args": ["/path/to/mcp-prompt-optimizer/prompt_optimizer.py"],
      "env": {}
    }
  }
}
```

## 🎮 Usage

### Basic Commands

```plaintext
# Analyze prompt quality
"Analyze this prompt: write a blog post about AI"

# Apply specific optimization
"Optimize this prompt using chain_of_thought: explain machine learning"

# Auto-select best strategy
"Auto-optimize: help me debug this code"

# Get domain template
"Get domain template for code_review_checklist"
```

### Advanced Commands

```plaintext
# Use Tree of Thoughts for complex problems
"Apply advanced optimization with tree_of_thoughts: design a microservices architecture"

# Use Constitutional AI for safety-critical tasks
"Apply advanced optimization with constitutional_ai: create content moderation guidelines"

# Use Medprompt for high-accuracy classification
"Apply advanced optimization with medprompt: categorize customer support tickets"

# List available templates
"List all domain templates"
```

## 🏗️ Architecture

```
mcp-prompt-optimizer/
├── prompt_optimizer.py      # Main MCP server
├── advanced_strategies.py   # Research-backed optimization strategies
├── domain_templates.py      # Professional domain templates
├── ai_docs/                 # Documentation and tools
│   ├── setup_interactive.py    # Automated setup script
│   ├── test_advanced.py        # Comprehensive test suite
│   └── *.md                    # Documentation files
├── CLAUDE.md               # Project guidance for AI
└── README.md               # This file
```

## 🧪 Testing

```bash
# Run basic tests
./test.sh

# Run advanced feature tests
python3 ai_docs/test_advanced.py

# Run comprehensive test suite
./ai_docs/test_advanced.sh
```

## 📊 Performance Benchmarks

| Strategy          | Use Case              | Performance Improvement |
| ----------------- | --------------------- | ----------------------- |
| Tree of Thoughts  | Complex reasoning     | 70-74% success rate     |
| Medprompt         | Classification tasks  | 90%+ accuracy           |
| Self-Refine       | Iterative improvement | 20% per iteration       |
| Constitutional AI | Safety alignment      | High compliance         |
| Chain of Thought  | Step-by-step tasks    | 15-25% improvement      |

## 🔧 Available Tools

### Core Tools

1. **analyze_prompt**: Analyzes prompt quality and identifies issues
2. **optimize_prompt**: Applies specific optimization strategies
3. **auto_optimize**: Automatically selects optimal strategy
4. **get_prompt_template**: Returns basic templates

### Advanced Tools

5. **advanced_optimize**: Applies research-backed strategies
6. **get_domain_template**: Returns professional domain templates
7. **list_domain_templates**: Lists available templates by domain

## 🎯 Strategy Selection Guide

| Prompt Type          | Recommended Strategy |
| -------------------- | -------------------- |
| Complex problems     | `tree_of_thoughts`   |
| Classification tasks | `medprompt`          |
| Safety-critical      | `constitutional_ai`  |
| Vague requirements   | `meta_prompting`     |
| Needs refinement     | `self_refine`        |
| General optimization | `auto`               |

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Update documentation
5. Submit a pull request

### Adding New Features

- **New Strategy**: Add to `advanced_strategies.py`
- **New Template**: Add to `domain_templates.py`
- **Tests**: Add to `ai_docs/test_advanced.py`

## 📚 Documentation

- **[Setup Guide](./ai_docs/CLAUDE_DESKTOP_GUIDE.md)** - Detailed installation instructions
- **[Examples](./ai_docs/EXAMPLES.md)** - Usage examples and workflows
- **[Research](./ai_docs/RESEARCH.md)** - Academic sources and benchmarks

## 🐛 Troubleshooting

### Common Issues

**MCP not working?**

- Check Python version: `python3 --version` (requires 3.8+)
- Verify MCP installation: `pip show mcp`
- Check Claude Desktop logs
- Restart Claude Desktop

**Commands not recognized?**

- Verify configuration file location
- Check file paths in configuration
- Run setup script again

### Debug Mode

```bash
# Test server directly
python3 prompt_optimizer.py

# Verbose logging
export MCP_LOG_LEVEL=debug
python3 prompt_optimizer.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Research from Princeton, Google DeepMind, Microsoft Research
- Anthropic's Constitutional AI framework
- Stanford's DSPy framework
- OpenAI's prompt engineering guidelines

## 📈 Citation

If you use this tool in your research or projects, please cite:

```bibtex
@software{mcp_prompt_optimizer,
  title={MCP Prompt Optimizer: Research-Backed Prompt Optimization for AI Systems},
  author={Bubobot},
  year={2024},
  url={https://github.com/Bubobot-Team/mcp-prompt-optimizer}
}
```

---

**Built with ❤️ for the AI community**

For questions, issues, or contributions, please visit our [GitHub repository](https://github.com/Bubobot-Team/mcp-prompt-optimizer).
