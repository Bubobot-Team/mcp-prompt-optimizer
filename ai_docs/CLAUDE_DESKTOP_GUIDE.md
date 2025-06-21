# Using MCP Prompt Optimizer in Claude Desktop

## Quick Setup

### 1. Configure Claude Desktop

Add this to your `claude_desktop_config.json`:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "prompt-optimizer": {
      "command": "python3",
      "args": ["/Users/phongpham/Project/boldlab/mcp-prompt-optimizer/prompt_optimizer.py"],
      "env": {}
    }
  }
}
```

### 2. Install Dependencies

```bash
cd /Users/phongpham/Project/boldlab/mcp-prompt-optimizer
pip install mcp
```

### 3. Restart Claude Desktop

Quit and restart Claude Desktop to load the MCP server.

## Usage Examples

Once configured, you can use these commands directly in Claude:

### Basic Prompt Optimization

```
Analyze this prompt: "write something about AI"
```

```
Optimize this prompt for clarity: "help me code"
```

```
Auto-optimize: "explain quantum computing"
```

### Advanced Optimization Strategies

```
Apply advanced optimization with tree_of_thoughts: "design a scalable microservices architecture"
```

```
Apply advanced optimization with constitutional_ai: "create a content moderation system"
```

```
Apply advanced optimization with medprompt: "classify customer support tickets"
```

```
Apply advanced optimization with self_refine: "improve this product description"
```

### Domain-Specific Templates

```
Get domain template for api_design
```

```
Get domain template for root_cause_analysis
```

```
Get domain template for ml_experiment_design
```

```
List all domain templates
```

```
List domain templates for security
```

## Real-World Examples

### 1. API Development

```
Get domain template for api_design

Then fill in:
- service_name: "Payment Processing API"
- auth_method: "OAuth 2.0"
- primary_resources: "payments, transactions, refunds"
```

### 2. Debugging Production Issues

```
Get domain template for root_cause_analysis

Use for:
- System outages
- Performance degradation
- Data inconsistencies
```

### 3. ML Experiment Design

```
Get domain template for ml_experiment_design

Perfect for:
- Setting up A/B tests
- Designing model experiments
- Tracking metrics
```

### 4. Security Assessment

```
Get domain template for security_assessment

Covers:
- STRIDE threat modeling
- OWASP compliance
- Risk assessment
```

## Advanced Workflows

### Workflow 1: Optimize Complex Prompts

1. Start with analysis:
   ```
   Analyze this prompt: "create a recommendation system"
   ```

2. Apply advanced optimization:
   ```
   Apply advanced optimization with tree_of_thoughts: "create a recommendation system that handles cold start, scales to millions of users, and provides explainable results"
   ```

3. Get implementation template:
   ```
   Get domain template for ml_experiment_design
   ```

### Workflow 2: System Design

1. Get the template:
   ```
   Get domain template for architecture_decision_record
   ```

2. Optimize your problem statement:
   ```
   Apply advanced optimization with meta_prompting: "choose between PostgreSQL and MongoDB for our e-commerce platform"
   ```

### Workflow 3: Incident Response

1. Get postmortem template:
   ```
   Get domain template for incident_postmortem
   ```

2. Analyze root cause:
   ```
   Get domain template for root_cause_analysis
   ```

3. Optimize action items:
   ```
   Apply advanced optimization with self_refine: "prevent similar database connection pool exhaustion issues"
   ```

## Tips for Best Results

1. **Be Specific**: The more context you provide, the better the optimization
2. **Use Templates**: Start with domain templates for structured tasks
3. **Iterate**: Use self_refine strategy for continuous improvement
4. **Combine Strategies**: Use multiple strategies for complex problems

## Performance Expectations

- **Tree of Thoughts**: 70-74% improvement for complex reasoning
- **Medprompt**: 90%+ accuracy for classification tasks
- **Self-Refine**: 20% improvement through iteration
- **Constitutional AI**: Enhanced safety and alignment

## Troubleshooting

If the MCP server doesn't appear to be working:

1. Check Claude Desktop logs
2. Verify Python path: `which python3`
3. Test manually: `python3 /path/to/prompt_optimizer.py`
4. Ensure all dependencies are installed
5. Check file permissions

## Integration with Your Workflow

### For Developers
- Use `api_design` template before implementation
- Apply `tree_of_thoughts` for architecture decisions
- Use `test_plan` template for comprehensive testing

### For Product Managers
- Use `product_requirements` template for PRDs
- Apply `meta_prompting` to clarify vague requirements
- Use `business_case` template for stakeholder buy-in

### For Data Scientists
- Use `ml_experiment_design` for experiments
- Apply `medprompt` for classification tasks
- Use `exploratory_data_analysis` template

### For DevOps
- Use `incident_postmortem` template
- Apply `root_cause_analysis` for debugging
- Use `security_assessment` for audits
