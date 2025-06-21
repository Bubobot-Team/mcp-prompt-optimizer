# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an advanced MCP (Model Context Protocol) server that provides cutting-edge prompt optimization tools with research-backed strategies delivering 15-74% performance improvements. The project offers dual implementations in Python (`prompt_optimizer.py`) and JavaScript (`index.js`).

**Important Memory Note:** All generated documents should be stored in the `@ai_docs` directory to maintain organization and easy access.

## Common Development Commands

### Testing
```bash
# Run basic tests
./test.sh

# Run advanced feature tests
./ai_docs/test_advanced.sh

# Test Python implementation manually
python3 examples.py

# Test advanced strategies
python3 ai_docs/test_advanced.py

# Test JavaScript implementation
npm start
```

### Python Development
```bash
# Install dependencies
pip install mcp

# Run the Python MCP server
python prompt_optimizer.py

# Check imports including new modules
python3 -c "from prompt_optimizer import PromptOptimizer; from advanced_strategies import AdvancedPromptOptimizer; from domain_templates import DomainTemplates"
```

### JavaScript Development
```bash
# Install dependencies
npm install

# Run the JavaScript MCP server
npm start
# or
node index.js
```

## Architecture

The MCP server now provides both basic and advanced prompt optimization capabilities:

### Basic Optimization Strategies
- **Clarity**: Simplifies prompts for directness
- **Specificity**: Adds detailed constraints
- **Chain of Thought**: Incorporates step-by-step reasoning
- **Few-Shot**: Includes example formats
- **Structured Output**: Defines clear output structure
- **Role-Based**: Adds expert role context

### Advanced Optimization Strategies (Research-Based)
- **Tree of Thoughts (ToT)**: Multi-path reasoning with 74% success rate on complex tasks
- **Constitutional AI**: Self-critique and alignment with safety principles
- **Automatic Prompt Engineer (APE)**: AI-discovered optimal instruction patterns
- **Meta-Prompting**: AI generates its own optimized prompts
- **Self-Refine**: Iterative improvement with 20% performance gains
- **TEXTGRAD**: Natural language feedback as optimization gradients
- **Medprompt**: Multi-technique ensemble achieving 90%+ accuracy
- **PromptWizard**: Feedback-driven self-evolving prompts

### Domain-Specific Templates
Production-ready templates across 11 domains:
- **Development**: API design, debugging, system architecture
- **Data Science**: EDA pipelines, ML experiment design
- **Operations**: DevOps runbooks, incident postmortems
- **Security**: STRIDE threat modeling, security reviews
- **Business**: PRDs, business cases, ROI analysis
- **Quality**: Test plans, documentation standards

### Tool Interface
The server exposes seven main tools through the MCP protocol:
1. `analyze_prompt` - Identifies issues and provides quality scoring
2. `optimize_prompt` - Applies basic optimization strategies
3. `auto_optimize` - Automatically selects best basic strategy
4. `get_prompt_template` - Provides basic templates
5. `advanced_optimize` - Applies research-based strategies (auto-selection available)
6. `get_domain_template` - Returns production-ready domain templates
7. `list_domain_templates` - Lists available templates by domain

### Module Structure
- `prompt_optimizer.py` - Main server with basic strategies and MCP integration
- `advanced_strategies.py` - Implementation of 8 research-based optimization strategies
- `domain_templates.py` - Collection of 11 domain-specific production templates
- Strategy selection logic based on prompt characteristics and performance metrics

The server integrates with Claude Desktop, providing AI agents with state-of-the-art prompt optimization capabilities for superior model responses.