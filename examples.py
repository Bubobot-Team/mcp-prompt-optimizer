#!/usr/bin/env python3
"""
Example usage of the Prompt Optimizer MCP
"""

from prompt_optimizer import PromptOptimizer, OptimizationStrategy

def main():
    optimizer = PromptOptimizer()
    
    # Example 1: Analyze a vague prompt
    print("=== Example 1: Analyzing a vague prompt ===")
    vague_prompt = "write something about AI"
    analysis = optimizer.analyze_prompt(vague_prompt)
    print(f"Prompt: {vague_prompt}")
    print(f"Score: {analysis.score}")
    print(f"Issues: {analysis.issues}")
    print(f"Suggestions: {analysis.suggestions}")
    print()
    
    # Example 2: Optimize for clarity
    print("=== Example 2: Optimizing for clarity ===")
    result = optimizer.optimize_prompt(vague_prompt, OptimizationStrategy.CLARITY)
    print(f"Original: {result['original']}")
    print(f"Optimized: {result['optimized']}")
    print(f"Improvements: {result['improvements']}")
    print()
    
    # Example 3: Chain of thought optimization
    print("=== Example 3: Chain of thought optimization ===")
    complex_prompt = "explain how machine learning works"
    result = optimizer.optimize_prompt(complex_prompt, OptimizationStrategy.CHAIN_OF_THOUGHT)
    print(f"Original: {result['original']}")
    print(f"Optimized: {result['optimized']}")
    print()
    
    # Example 4: Role-based optimization
    print("=== Example 4: Role-based optimization ===")
    coding_prompt = "help me debug this Python code"
    result = optimizer.optimize_prompt(coding_prompt, OptimizationStrategy.ROLE_BASED)
    print(f"Original: {result['original']}")
    print(f"Optimized: {result['optimized']}")
    print()

if __name__ == "__main__":
    main()
