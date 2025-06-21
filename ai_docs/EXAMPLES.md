# MCP Prompt Optimizer Examples

This file demonstrates real-world usage of the MCP Prompt Optimizer in Claude Desktop.

## Example 1: API Development

### Initial Request
```
You: I need to create an API for managing user profiles
```

### Using MCP to Optimize

**Step 1: Get the template**
```
You: Get domain template for api_design
```

Claude provides a comprehensive API design template with 30+ variables including authentication, rate limiting, OpenAPI specs, etc.

**Step 2: Optimize the request**
```
You: Apply advanced optimization with tree_of_thoughts: Design a user profile API that handles 50k concurrent users, supports GDPR compliance, integrates with OAuth providers, and allows partial updates
```

Claude uses Tree of Thoughts to explore multiple design paths, evaluating trade-offs and providing a 74% more comprehensive solution.

## Example 2: Debugging Production Issue

### Scenario: Database performance degradation

**Step 1: Get RCA template**
```
You: Get domain template for root_cause_analysis
```

**Step 2: Apply advanced analysis**
```
You: Apply advanced optimization with medprompt: Our database queries are 10x slower since yesterday's deployment. Error logs show connection timeouts and lock contentions.
```

Claude uses 4-technique ensemble to achieve 90%+ accuracy in identifying root causes.

## Example 3: Machine Learning Experiment

### Initial vague request
```
You: Help me improve my model performance
```

**Step 1: Analyze the prompt**
```
You: Analyze this prompt: help me improve my model performance
```

Claude identifies:
- Issues: Too vague, no context, no metrics
- Suggestions: Specify model type, current performance, target metrics

**Step 2: Get ML template**
```
You: Get domain template for ml_experiment_design
```

**Step 3: Optimize with details**
```
You: Apply advanced optimization with self_refine: Improve my customer churn prediction model. Current F1: 0.72, target: 0.80. Using XGBoost on imbalanced data (1:20 ratio).
```

Claude iteratively refines the approach with 20% expected improvement.

## Example 4: Writing Technical Documentation

**Using auto-optimization**
```
You: Auto-optimize: write documentation for our authentication system
```

Claude automatically:
1. Detects this is a documentation task
2. Selects appropriate strategy (structured_output)
3. Provides optimized prompt with sections, audience, and format

## Example 5: Complex System Design

**Multi-strategy approach**
```
You: I need to design a real-time analytics platform

You: Get domain template for architecture_decision_record

You: Apply advanced optimization with tree_of_thoughts: Design a real-time analytics platform handling 1M events/sec, sub-second query latency, exactly-once processing, and multi-region deployment

You: Apply advanced optimization with constitutional_ai: What are the security implications of this design?
```

## Example 6: Product Requirements

**From vague to specific**
```
You: Apply advanced optimization with meta_prompting: We need a feature for users to share stuff

Claude generates an optimized prompt:
"Design a content sharing feature that allows users to share [specific content types] via [sharing channels] with [permission controls] while maintaining [privacy requirements] and supporting [scale requirements]"
```

## Example 7: Testing Strategy

**Comprehensive test planning**
```
You: Get domain template for test_plan

You: Apply advanced optimization with medprompt: Create test cases for our payment processing system covering PCI compliance, edge cases, and integration scenarios
```

## Example 8: Incident Response

**During an outage**
```
You: Get domain template for incident_postmortem

You: Apply advanced optimization with tree_of_thoughts: API Gateway returning 503 errors, started 2 hours ago, affecting 30% of requests, coincided with auto-scaling event
```

## Example 9: Business Analysis

**ROI calculation**
```
You: Get domain template for business_case

You: Apply advanced optimization with textgrad: Build business case for migrating from on-prem to cloud, considering 3-year TCO, migration risks, and operational benefits
```

## Example 10: Security Assessment

**Threat modeling**
```
You: Get domain template for security_assessment

You: Apply advanced optimization with constitutional_ai: Perform STRIDE analysis on our new mobile banking app with focus on transaction integrity and user authentication
```

## Tips for Best Results

1. **Start simple**: Use `analyze_prompt` first to understand improvements needed
2. **Use templates**: They provide structure and ensure completeness
3. **Layer strategies**: Combine multiple optimizations for complex tasks
4. **Iterate**: Use `self_refine` for continuous improvement
5. **Match strategy to task**: 
   - Complex problems → `tree_of_thoughts`
   - Safety concerns → `constitutional_ai`
   - Classifications → `medprompt`
   - Improvements → `self_refine`

## Measuring Success

After using optimized prompts, you should see:
- More comprehensive responses
- Better structured outputs
- Fewer clarification requests
- Higher accuracy on specific tasks
- Improved actionability

Remember: The goal is not just better prompts, but better outcomes for your work!
