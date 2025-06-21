#!/usr/bin/env python3
"""
Prompt Optimizer MCP Server
An MCP server that provides tools for optimizing prompts for better AI responses
"""

import json
import asyncio
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum

# MCP server imports (you'll need to install these)
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Import advanced strategies and domain templates
from advanced_strategies import AdvancedPromptOptimizer, AdvancedStrategy
from domain_templates import DomainTemplates


class OptimizationStrategy(Enum):
    CLARITY = "clarity"
    SPECIFICITY = "specificity"
    CHAIN_OF_THOUGHT = "chain_of_thought"
    FEW_SHOT = "few_shot"
    STRUCTURED_OUTPUT = "structured_output"
    ROLE_BASED = "role_based"
    CONSTRAINTS = "constraints"  # New strategy
    TONE_ADJUSTMENT = "tone_adjustment"  # New strategy


@dataclass
class PromptAnalysis:
    issues: List[str]
    suggestions: List[str]
    score: float


class PromptOptimizer:
    """Core logic for prompt optimization"""

    def analyze_prompt(self, prompt: str) -> PromptAnalysis:
        """Analyze a prompt for common issues"""
        issues = []
        suggestions = []
        score = 100.0

        # Check for vagueness
        vague_words = ["thing", "stuff", "something",
                       "whatever", "somehow", "etc.", "and so on"]
        for word in vague_words:
            if word in prompt.lower():
                issues.append(f"Contains vague word: \'{word}\'")
                suggestions.append(
                    f"Replace \'{word}\' with specific terms or examples.")
                score -= 5

        # Check prompt length
        if len(prompt) < 30:
            issues.append("Prompt is too short.")
            suggestions.append(
                "Add more context, details, and specific instructions.")
            score -= 10

        # Check for clear instructions/action verbs
        action_verbs = ["explain", "describe", "create", "analyze",
                        "generate", "summarize", "list", "compare", "write", "develop"]
        if not any(word in prompt.lower() for word in action_verbs):
            issues.append("Lacks a clear action verb or instruction.")
            suggestions.append(
                "Start the prompt with a clear action verb (e.g., 'Generate', 'Analyze', 'Write').")
            score -= 10

        # Check for context
        if len(prompt.split()) < 15:
            issues.append("Lacks sufficient context.")
            suggestions.append(
                "Provide background information, purpose, or scenario.")
            score -= 5

        # Check for desired format/output structure
        if not any(word in prompt.lower() for word in ["format", "structure", "output as", "in the form of"]):
            issues.append("Missing explicit output format instructions.")
            suggestions.append(
                "Specify the desired output format (e.g., 'as a JSON object', 'in bullet points', 'a table').")
            score -= 7

        # Check for tone/style guidance
        if not any(word in prompt.lower() for word in ["tone", "style", "professional", "casual", "friendly", "formal"]):
            issues.append("Missing tone or style guidance.")
            suggestions.append(
                "Specify the desired tone or writing style (e.g., 'professional', 'casual', 'persuasive').")
            score -= 3

        return PromptAnalysis(issues, suggestions, max(0, score))

    def optimize_prompt(self, prompt: str, strategy: OptimizationStrategy) -> Dict[str, Any]:
        """Optimize a prompt based on the selected strategy"""

        optimized = prompt
        explanation = ""

        if strategy == OptimizationStrategy.CLARITY:
            optimized = self._optimize_for_clarity(prompt)
            explanation = "Improved clarity by removing ambiguity and adding specific instructions."

        elif strategy == OptimizationStrategy.SPECIFICITY:
            optimized = self._optimize_for_specificity(prompt)
            explanation = "Added specific details, constraints, and examples."

        elif strategy == OptimizationStrategy.CHAIN_OF_THOUGHT:
            optimized = self._add_chain_of_thought(prompt)
            explanation = "Added chain-of-thought reasoning instructions to guide the model's thinking process."

        elif strategy == OptimizationStrategy.FEW_SHOT:
            optimized = self._add_few_shot_examples(prompt)
            explanation = "Added examples to guide the response format and content."

        elif strategy == OptimizationStrategy.STRUCTURED_OUTPUT:
            optimized = self._add_structure(prompt)
            explanation = "Added explicit structure for organized and predictable output."

        elif strategy == OptimizationStrategy.ROLE_BASED:
            optimized = self._add_role_context(prompt)
            explanation = "Assigned a specific role to the AI to leverage its expertise."

        elif strategy == OptimizationStrategy.CONSTRAINTS:
            optimized = self._add_constraints(prompt)
            explanation = "Added explicit constraints and limitations to guide the response."

        elif strategy == OptimizationStrategy.TONE_ADJUSTMENT:
            optimized = self._adjust_tone(prompt)
            explanation = "Adjusted the tone and style of the prompt for better alignment with desired output."

        return {
            "original": prompt,
            "optimized": optimized,
            "strategy": strategy.value,
            "explanation": explanation,
            "improvements": self._list_improvements(prompt, optimized)
        }

    def _optimize_for_clarity(self, prompt: str) -> str:
        """Make the prompt clearer and more direct"""
        parts = []

        # Add objective/task explicitly
        if "objective:" not in prompt.lower() and "task:" not in prompt.lower():
            if any(word in prompt.lower() for word in ["help", "need", "want"]):
                parts.append("Objective: " + prompt)
            else:
                parts.append("Task: " + prompt)
        else:
            parts.append(prompt)

        # Add clarifying instructions if not already present
        if not any(instr in prompt.lower() for instr in ["clear and detailed", "concise and direct"]):
            parts.append(
                "\nPlease provide a clear, concise, and detailed response that:")
            parts.append("- Directly addresses the main request.")
            parts.append("- Uses simple, precise, and unambiguous language.")
            parts.append("- Avoids jargon unless explicitly requested.")
            parts.append("- Includes relevant examples where helpful.")

        return "\n".join(parts)

    def _optimize_for_specificity(self, prompt: str) -> str:
        """Add specific constraints and details"""
        enhanced = prompt

        # Add specificity markers based on common action verbs
        if "explain" in prompt.lower() or "describe" in prompt.lower():
            if "specifically:" not in enhanced.lower():
                enhanced += "\n\nSpecifically:"
                enhanced += "\n- Define all key terms and concepts."
                enhanced += "\n- Provide concrete, real-world examples."
                enhanced += "\n- Include relevant background context and assumptions."

        if "create" in prompt.lower() or "write" in prompt.lower() or "generate" in prompt.lower():
            if "requirements:" not in enhanced.lower():
                enhanced += "\n\nRequirements:"
                enhanced += "\n- Length: Be comprehensive but concise, aiming for [specify length, e.g., 500 words, 3 paragraphs]."
                enhanced += "\n- Style: Maintain a professional and clear writing style."
                enhanced += "\n- Format: Ensure the output is well-structured with clear sections, headings, and bullet points where appropriate."
                enhanced += "\n- Target Audience: Tailor the response for [specify audience, e.g., a technical expert, a general audience]."

        return enhanced

    def _add_chain_of_thought(self, prompt: str) -> str:
        """Add chain-of-thought reasoning"""
        cot_prompt = prompt
        if "step-by-step" not in prompt.lower() and "reasoning" not in prompt.lower():
            cot_prompt += "\n\nPlease approach this step-by-step:"
            cot_prompt += "\n1. First, clearly understand the core problem or request."
            cot_prompt += "\n2. Break down the problem into its fundamental components."
            cot_prompt += "\n3. Address each component systematically, showing your thought process."
            cot_prompt += "\n4. Synthesize your findings into a comprehensive and coherent final response."
            cot_prompt += "\n\nShow your reasoning for each step, explaining why you made certain decisions or reached specific conclusions."

        return cot_prompt

    def _add_few_shot_examples(self, prompt: str) -> str:
        """Add example format"""
        few_shot = prompt
        if "example format" not in prompt.lower() and "example:" not in prompt.lower():
            few_shot += "\n\nExample format for your response:"
            few_shot += "\n\n**Main Point**: [Your key insight here]"
            few_shot += "\n**Explanation**: [Detailed explanation of the main point]"
            few_shot += "\n**Example**: [A concrete, illustrative example]"
            few_shot += "\n**Additional Considerations**: [Any other relevant points or caveats]"

        return few_shot

    def _add_structure(self, prompt: str) -> str:
        """Add output structure"""
        structured = prompt
        if "structure your response as follows" not in prompt.lower() and "output format" not in prompt.lower():
            structured += "\n\nPlease structure your response as follows:"
            structured += "\n\n1. **Overview**: A brief, high-level summary of the entire response."
            structured += "\n2. **Detailed Analysis**: An in-depth exploration of the topic, broken into logical sections with clear headings."
            structured += "\n3. **Key Takeaways**: A bulleted list summarizing the most important insights or conclusions."
            structured += "\n4. **Next Steps/Recommendations**: Actionable advice or suggestions based on the analysis."

        return structured

    def _add_role_context(self, prompt: str) -> str:
        """Add role-based expertise context"""
        # Detect domain based on keywords, prioritizing more specific roles
        role = "expert"
        if any(word in prompt.lower() for word in ["code", "program", "software", "debug", "api"]):
            role = "senior software engineer and architect"
        elif any(word in prompt.lower() for word in ["business", "strategy", "market", "finance", "investment"]):
            role = "seasoned business strategist and financial analyst"
        elif any(word in prompt.lower() for word in ["write", "content", "article", "story", "blog"]):
            role = "professional writer and content creator"
        elif any(word in prompt.lower() for word in ["data", "analyze", "statistics", "insights"]):
            role = "expert data scientist and analyst"
        elif any(word in prompt.lower() for word in ["design", "ui", "ux", "user experience"]):
            role = "experienced UX/UI designer"
        elif any(word in prompt.lower() for word in ["legal", "contract", "compliance"]):
            role = "legal counsel specializing in contract law"
        elif any(word in prompt.lower() for word in ["project management", "agile", "scrum"]):
            role = "certified project manager"

        role_prompt = f"As a {role}, {prompt}"
        role_prompt += f"\n\nDraw upon your extensive expertise to provide insights that only a {role} would know, ensuring accuracy and depth."

        return role_prompt

    def _add_constraints(self, prompt: str) -> str:
        """Add explicit constraints and limitations"""
        constraints_prompt = prompt
        if "constraints:" not in prompt.lower() and "limitations:" not in prompt.lower():
            constraints_prompt += "\n\nConstraints and Limitations:"
            constraints_prompt += "\n- Ensure the response is no longer than [specify length, e.g., 300 words]."
            constraints_prompt += "\n- Do not include any external links or references."
            constraints_prompt += "\n- Focus solely on [specific topic] and avoid [off-topic subjects]."
            constraints_prompt += "\n- If information is unavailable, state that clearly rather than fabricating."
        return constraints_prompt

    def _adjust_tone(self, prompt: str) -> str:
        """Adjust the tone and style of the prompt"""
        tone_prompt = prompt
        if "tone:" not in prompt.lower() and "style:" not in prompt.lower():
            tone_prompt += "\n\nDesired Tone and Style:"
            tone_prompt += "\n- Maintain a [e.g., professional, friendly, formal, casual, persuasive, empathetic] tone throughout."
            tone_prompt += "\n- Write in a [e.g., clear, concise, engaging, academic] style."
            tone_prompt += "\n- Avoid [e.g., overly technical jargon, slang, passive voice]."
        return tone_prompt

    def _list_improvements(self, original: str, optimized: str) -> List[str]:
        """List what improvements were made"""
        improvements = []

        if len(optimized) > len(original) * 1.1:  # Adjusted threshold for more accurate reporting
            improvements.append("Added detailed instructions or context.")

        if "step-by-step" in optimized.lower() and "step-by-step" not in original.lower():
            improvements.append(
                "Incorporated step-by-step reasoning (Chain-of-Thought).")

        if "example format" in optimized.lower() or "example:" in optimized.lower():
            improvements.append(
                "Included example formats for structured responses (Few-Shot).")

        if "structure your response as follows" in optimized.lower() or "output format" in optimized.lower():
            improvements.append("Defined explicit output structure.")

        if "as a " in optimized.lower() and "as a " not in original.lower() and "role" in optimized.lower():
            improvements.append(
                "Applied role-based context for specialized expertise.")

        if "constraints and limitations:" in optimized.lower():
            improvements.append(
                "Added explicit constraints to guide the response.")

        if "desired tone and style:" in optimized.lower():
            improvements.append("Provided guidance on desired tone and style.")

        return improvements


# MCP Server Setup
app = Server("prompt-optimizer")
optimizer = PromptOptimizer()
advanced_optimizer = AdvancedPromptOptimizer()
domain_templates = DomainTemplates()


@app.list_tools()
async def list_tools() -> List[Tool]:
    """List available tools"""
    return [
        Tool(
            name="analyze_prompt",
            description="Analyze a prompt for common issues and get improvement suggestions",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to analyze"
                    }
                },
                "required": ["prompt"]
            }
        ),
        Tool(
            name="optimize_prompt",
            description="Optimize a prompt using a specific strategy",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to optimize"
                    },
                    "strategy": {
                        "type": "string",
                        "enum": [strat.value for strat in OptimizationStrategy],
                        "description": "Optimization strategy to use"
                    }
                },
                "required": ["prompt", "strategy"]
            }
        ),
        Tool(
            name="auto_optimize",
            description="Automatically optimize a prompt using the best strategy",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to optimize"
                    },
                    "context": {
                        "type": "string",
                        "description": "Additional context about the use case",
                        "optional": True
                    }
                },
                "required": ["prompt"]
            }
        ),
        Tool(
            name="get_prompt_template",
            description="Get a prompt template for a specific use case",
            inputSchema={
                "type": "object",
                "properties": {
                    "use_case": {
                        "type": "string",
                        "enum": ["code_generation", "analysis", "creative_writing", "data_extraction", "tutoring"],
                        "description": "The use case for the prompt template"
                    }
                },
                "required": ["use_case"]
            }
        ),
        Tool(
            name="advanced_optimize",
            description="Apply advanced optimization strategies (ToT, Constitutional AI, APE, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to optimize"
                    },
                    "strategy": {
                        "type": "string",
                        "enum": ["tree_of_thoughts", "constitutional_ai", "automatic_prompt_engineer",
                                 "meta_prompting", "self_refine", "textgrad", "medprompt", "prompt_wizard", "auto"],
                        "description": "Advanced optimization strategy to use (auto selects best)"
                    }
                },
                "required": ["prompt", "strategy"]
            }
        ),
        Tool(
            name="get_domain_template",
            description="Get a production-ready template for a specific domain",
            inputSchema={
                "type": "object",
                "properties": {
                    "template_name": {
                        "type": "string",
                        "description": "Name of the template (e.g., api_design, root_cause_analysis)"
                    }
                },
                "required": ["template_name"]
            }
        ),
        Tool(
            name="list_domain_templates",
            description="List all available domain-specific templates",
            inputSchema={
                "type": "object",
                "properties": {
                    "domain": {
                        "type": "string",
                        "description": "Optional: filter by domain",
                        "optional": True
                    }
                },
                "required": []
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls"""

    if name == "analyze_prompt":
        analysis = optimizer.analyze_prompt(arguments["prompt"])
        result = {
            "score": analysis.score,
            "issues": analysis.issues,
            "suggestions": analysis.suggestions
        }
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "optimize_prompt":
        strategy = OptimizationStrategy(arguments["strategy"])
        result = optimizer.optimize_prompt(arguments["prompt"], strategy)
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "auto_optimize":
        # Analyze first to determine best strategy
        analysis = optimizer.analyze_prompt(arguments["prompt"])

        # Choose strategy based on issues
        if analysis.score < 50:
            strategy = OptimizationStrategy.CLARITY
        elif "context" in str(analysis.issues):
            strategy = OptimizationStrategy.SPECIFICITY
        elif "output format" in str(analysis.issues):
            strategy = OptimizationStrategy.STRUCTURED_OUTPUT
        elif "tone" in str(analysis.issues):
            strategy = OptimizationStrategy.TONE_ADJUSTMENT
        else:
            strategy = OptimizationStrategy.CHAIN_OF_THOUGHT

        result = optimizer.optimize_prompt(arguments["prompt"], strategy)
        result["auto_selected_reason"] = f"Chose {strategy.value} based on analysis score of {analysis.score}"

        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "get_prompt_template":
        templates = {
            "code_generation": """Task: [Describe what code you need]\n\nRequirements:\n- Language: [Specify programming language]\n- Purpose: [What the code should accomplish]\n- Constraints: [Any limitations or requirements]\n- Style: [Coding standards to follow]\n\nPlease generate code that:\n1. Includes comprehensive error handling\n2. Follows best practices for the language\n3. Is well-commented and documented\n4. Includes example usage""",

            "analysis": """Analyze [subject/data/situation]\n\nContext: [Provide relevant background]\n\nFocus on:\n- Key patterns and trends\n- Underlying causes\n- Implications and consequences\n- Actionable insights\n\nPlease structure your analysis with:\n1. Executive Summary\n2. Detailed Findings\n3. Recommendations\n4. Supporting Evidence""",

            "creative_writing": """Create [type of content] about [topic]\n\nTone: [formal/casual/humorous/serious]\nLength: [word count or scope]\nAudience: [target readers]\nStyle: [narrative/descriptive/persuasive]\n\nKey elements to include:\n- [Element 1]\n- [Element 2]\n- [Element 3]\n\nPlease ensure the content is engaging, original, and appropriate for the audience.""",

            "data_extraction": """Extract [specific data points] from the following text:\n\nText: [Insert text here]\n\nOutput Format: [e.g., JSON, CSV, bullet points]\n\nEnsure accuracy and completeness. If a data point is not found, indicate 'N/A'.""",

            "tutoring": """Explain [concept/topic] to a [target audience, e.g., high school student, beginner in programming].\n\nFocus on:\n- Core principles\n- Simple analogies\n- Practical examples\n- Common misconceptions\n\nBreak down complex ideas into easy-to-understand segments. Encourage questions and provide a clear, supportive explanation."""
        }

        template = templates.get(arguments["use_case"])
        if template:
            return [TextContent(type="text", text=template)]
        else:
            return [TextContent(type="text", text="Template not found for the specified use case.")]

    elif name == "advanced_optimize":
        strategy = AdvancedStrategy(arguments["strategy"])
        result = advanced_optimizer.optimize_prompt(
            arguments["prompt"], strategy)
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "get_domain_template":
        template = domain_templates.get_template(arguments["template_name"])
        if template:
            return [TextContent(type="text", text=template)]
        else:
            return [TextContent(type="text", text="Domain template not found.")]

    elif name == "list_domain_templates":
        templates = domain_templates.list_templates(arguments.get("domain"))
        return [TextContent(type="text", text=json.dumps(templates, indent=2))]

    else:
        return [TextContent(type="text", text="Unknown tool.")]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
