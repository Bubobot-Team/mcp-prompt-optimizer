"""
Domain-specific prompt templates for various professional contexts.
Each template provides a structured format for specific business domains.
Integrates both comprehensive professional templates and additional use cases.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass

@dataclass
class PromptTemplate:
    """Represents a domain-specific prompt template"""
    name: str
    domain: str
    template: str
    variables: List[str]
    example: str
    best_practices: Optional[List[str]] = None
    examples: Optional[List[str]] = None

class DomainTemplates:
    """Collection of comprehensive domain-specific templates for professional use"""
    
    def __init__(self):
        self.templates: Dict[str, PromptTemplate] = {}
        self._load_professional_templates()
        self._load_additional_use_cases()
    
    def _load_professional_templates(self):
        """Load comprehensive professional templates with advanced features"""
        professional_templates = {
            "competitor_analysis": {
                "name": "Competitive Analysis Framework",
                "domain": "business_analysis",
                "template": """Conduct a comprehensive competitive analysis for {company_name} in the {industry} market.

**Executive Summary**
Provide a high-level overview of the competitive landscape and {company_name}'s position.

**Market Overview**
- Market size: {market_size}
- Growth rate: {growth_rate}
- Key trends: {market_trends}
- Market segments: {segments}

**Competitor Identification**
Analyze these key competitors:
1. {competitor_1}: {competitor_1_description}
2. {competitor_2}: {competitor_2_description}
3. {competitor_3}: {competitor_3_description}

**Competitive Analysis Matrix**

| Criteria | {company_name} | {competitor_1} | {competitor_2} | {competitor_3} |
|----------|----------------|----------------|----------------|----------------|
| Market Share | {company_share} | {comp1_share} | {comp2_share} | {comp3_share} |
| Pricing Strategy | {company_pricing} | {comp1_pricing} | {comp2_pricing} | {comp3_pricing} |
| Product Features | {company_features} | {comp1_features} | {comp2_features} | {comp3_features} |
| Target Audience | {company_audience} | {comp1_audience} | {comp2_audience} | {comp3_audience} |
| Strengths | {company_strengths} | {comp1_strengths} | {comp2_strengths} | {comp3_strengths} |
| Weaknesses | {company_weaknesses} | {comp1_weaknesses} | {comp2_weaknesses} | {comp3_weaknesses} |

**SWOT Analysis for {company_name}**
- Strengths: {detailed_strengths}
- Weaknesses: {detailed_weaknesses}
- Opportunities: {opportunities}
- Threats: {threats}

**Competitive Positioning**
{positioning_analysis}

**Strategic Recommendations**
1. {recommendation_1}
2. {recommendation_2}
3. {recommendation_3}

**Action Plan**
- Short-term (0-6 months): {short_term_actions}
- Medium-term (6-12 months): {medium_term_actions}
- Long-term (12+ months): {long_term_actions}""",
                "variables": ["company_name", "industry", "market_size", "growth_rate", "market_trends", 
                            "segments", "competitor_1", "competitor_1_description", "competitor_2", 
                            "competitor_2_description", "competitor_3", "competitor_3_description",
                            "company_share", "comp1_share", "comp2_share", "comp3_share",
                            "company_pricing", "comp1_pricing", "comp2_pricing", "comp3_pricing",
                            "company_features", "comp1_features", "comp2_features", "comp3_features",
                            "company_audience", "comp1_audience", "comp2_audience", "comp3_audience",
                            "company_strengths", "comp1_strengths", "comp2_strengths", "comp3_strengths",
                            "company_weaknesses", "comp1_weaknesses", "comp2_weaknesses", "comp3_weaknesses",
                            "detailed_strengths", "detailed_weaknesses", "opportunities", "threats",
                            "positioning_analysis", "recommendation_1", "recommendation_2", "recommendation_3",
                            "short_term_actions", "medium_term_actions", "long_term_actions"],
                "examples": ["SaaS company analysis", "E-commerce platform comparison", "Mobile app competitive landscape"],
                "best_practices": ["Use recent data", "Include visual comparisons", "Focus on actionable insights"],
                "example": "Competitive Analysis: SaaS CRM Market..."
            },
            
            "user_research_synthesis": {
                "name": "User Research Synthesis",
                "domain": "product_management",
                "template": """# User Research Synthesis: {research_topic}

**Research Overview**
- Research period: {research_period}
- Methods used: {research_methods}
- Sample size: {sample_size}
- Demographics: {demographics}

**Key Research Questions**
1. {research_question_1}
2. {research_question_2}
3. {research_question_3}

**Methodology**
{methodology_description}

**Key Findings**

### Finding 1: {finding_1_title}
- **Observation**: {finding_1_observation}
- **Data**: {finding_1_data}
- **Quote**: "{finding_1_quote}"
- **Implication**: {finding_1_implication}

### Finding 2: {finding_2_title}
- **Observation**: {finding_2_observation}
- **Data**: {finding_2_data}
- **Quote**: "{finding_2_quote}"
- **Implication**: {finding_2_implication}

### Finding 3: {finding_3_title}
- **Observation**: {finding_3_observation}
- **Data**: {finding_3_data}
- **Quote**: "{finding_3_quote}"
- **Implication**: {finding_3_implication}

**User Personas Refinement**
Based on research, update personas:
- {persona_1_changes}
- {persona_2_changes}

**Journey Map Insights**
Key pain points discovered:
1. {pain_point_1}: {pain_point_1_details}
2. {pain_point_2}: {pain_point_2_details}
3. {pain_point_3}: {pain_point_3_details}

**Opportunities Identified**
- **Quick wins**: {quick_wins}
- **Medium-term**: {medium_term_opportunities}
- **Long-term**: {long_term_opportunities}

**Recommendations**
1. {recommendation_1}: {rec_1_rationale}
2. {recommendation_2}: {rec_2_rationale}
3. {recommendation_3}: {rec_3_rationale}

**Next Steps**
- {next_step_1}
- {next_step_2}
- {next_step_3}

**Appendix**
- Raw data: {data_location}
- Interview recordings: {recordings_location}
- Survey results: {survey_location}""",
                "variables": ["research_topic", "research_period", "research_methods", "sample_size",
                            "demographics", "research_question_1", "research_question_2", "research_question_3",
                            "methodology_description", "finding_1_title", "finding_1_observation",
                            "finding_1_data", "finding_1_quote", "finding_1_implication",
                            "finding_2_title", "finding_2_observation", "finding_2_data",
                            "finding_2_quote", "finding_2_implication", "finding_3_title",
                            "finding_3_observation", "finding_3_data", "finding_3_quote",
                            "finding_3_implication", "persona_1_changes", "persona_2_changes",
                            "pain_point_1", "pain_point_1_details", "pain_point_2", "pain_point_2_details",
                            "pain_point_3", "pain_point_3_details", "quick_wins", "medium_term_opportunities",
                            "long_term_opportunities", "recommendation_1", "rec_1_rationale",
                            "recommendation_2", "rec_2_rationale", "recommendation_3", "rec_3_rationale",
                            "next_step_1", "next_step_2", "next_step_3", "data_location",
                            "recordings_location", "survey_location"],
                "examples": ["Usability study synthesis", "Customer interview insights", "Survey analysis report"],
                "best_practices": ["Include direct quotes", "Link findings to business impact", "Prioritize actionability"],
                "example": "User Research Synthesis: Mobile App Navigation Study..."
            },
            
            "technical_blog_post": {
                "name": "Technical Blog Post Structure",
                "domain": "content_creation",
                "template": """# {title}

**Meta Description**: {meta_description} (150-160 characters)
**Keywords**: {keywords}
**Reading Time**: {reading_time} minutes

## Introduction

{hook_statement}

{problem_context}

In this post, you'll learn:
- {learning_outcome_1}
- {learning_outcome_2}
- {learning_outcome_3}

## Prerequisites

Before diving in, you should be familiar with:
- {prerequisite_1}
- {prerequisite_2}

## The Problem

{problem_description}

### Real-World Impact
{real_world_example}

## The Solution

### Overview
{solution_overview}

### Implementation

#### Step 1: {step_1_title}
{step_1_description}

```{code_language}
{step_1_code}
```

**Explanation**: {step_1_explanation}

#### Step 2: {step_2_title}
{step_2_description}

```{code_language}
{step_2_code}
```

**Explanation**: {step_2_explanation}

#### Step 3: {step_3_title}
{step_3_description}

```{code_language}
{step_3_code}
```

**Explanation**: {step_3_explanation}

## Best Practices

1. **{best_practice_1}**: {bp_1_explanation}
2. **{best_practice_2}**: {bp_2_explanation}
3. **{best_practice_3}**: {bp_3_explanation}

## Common Pitfalls

- **{pitfall_1}**: {pitfall_1_solution}
- **{pitfall_2}**: {pitfall_2_solution}

## Performance Considerations

{performance_analysis}

### Benchmarks
| Approach | Time | Memory | Complexity |
|----------|------|--------|------------|
| {approach_1} | {time_1} | {memory_1} | {complexity_1} |
| {approach_2} | {time_2} | {memory_2} | {complexity_2} |

## Conclusion

{summary}

### Key Takeaways
- {takeaway_1}
- {takeaway_2}
- {takeaway_3}

### Next Steps
{next_steps}

## Additional Resources
- [{resource_1_title}]({resource_1_link})
- [{resource_2_title}]({resource_2_link})
- [{resource_3_title}]({resource_3_link})

---

**About the Author**: {author_bio}

**Comments**: Enable below or link to discussion platform""",
                "variables": ["title", "meta_description", "keywords", "reading_time", "hook_statement",
                            "problem_context", "learning_outcome_1", "learning_outcome_2", "learning_outcome_3",
                            "prerequisite_1", "prerequisite_2", "problem_description", "real_world_example",
                            "solution_overview", "step_1_title", "step_1_description", "code_language",
                            "step_1_code", "step_1_explanation", "step_2_title", "step_2_description",
                            "step_2_code", "step_2_explanation", "step_3_title", "step_3_description",
                            "step_3_code", "step_3_explanation", "best_practice_1", "bp_1_explanation",
                            "best_practice_2", "bp_2_explanation", "best_practice_3", "bp_3_explanation",
                            "pitfall_1", "pitfall_1_solution", "pitfall_2", "pitfall_2_solution",
                            "performance_analysis", "approach_1", "time_1", "memory_1", "complexity_1",
                            "approach_2", "time_2", "memory_2", "complexity_2", "summary",
                            "takeaway_1", "takeaway_2", "takeaway_3", "next_steps",
                            "resource_1_title", "resource_1_link", "resource_2_title", "resource_2_link",
                            "resource_3_title", "resource_3_link", "author_bio"],
                "examples": ["React hooks tutorial", "Kubernetes deployment guide", "Python optimization techniques"],
                "best_practices": ["Use code examples", "Include visuals", "SEO optimization", "Mobile-friendly formatting"],
                "example": "Technical Blog Post: Advanced React Patterns..."
            },
            
            "code_review_checklist": {
                "name": "Comprehensive Code Review Checklist",
                "domain": "development",
                "template": """# Code Review: {pr_title}

**PR #**: {pr_number}
**Author**: {author}
**Reviewer**: {reviewer}
**Date**: {date}
**Files Changed**: {files_changed}
**Lines**: +{lines_added} / -{lines_removed}

## Summary
{pr_description}

## Review Checklist

### 🏗️ Architecture & Design
- [ ] Follows established patterns: {patterns_check}
- [ ] SOLID principles: {solid_check}
- [ ] Appropriate abstractions: {abstractions_check}
- [ ] No over-engineering: {overengineering_check}

### 🔧 Code Quality
- [ ] Readable and self-documenting: {readability_check}
- [ ] DRY (Don't Repeat Yourself): {dry_check}
- [ ] Appropriate naming: {naming_check}
- [ ] Complexity manageable: {complexity_check}

### 🧪 Testing
- [ ] Unit tests added/updated: {unit_tests_check}
- [ ] Integration tests: {integration_tests_check}
- [ ] Edge cases covered: {edge_cases_check}
- [ ] Test coverage adequate: {coverage_check}

### 🔒 Security
- [ ] Input validation: {input_validation_check}
- [ ] No hardcoded secrets: {secrets_check}
- [ ] SQL injection prevention: {sql_injection_check}
- [ ] XSS prevention: {xss_check}
- [ ] Authentication/Authorization: {auth_check}

### ⚡ Performance
- [ ] No N+1 queries: {n_plus_one_check}
- [ ] Efficient algorithms: {algorithm_check}
- [ ] Caching considered: {caching_check}
- [ ] Database indexes: {indexes_check}

### 📝 Documentation
- [ ] Code comments where needed: {comments_check}
- [ ] README updated: {readme_check}
- [ ] API documentation: {api_docs_check}
- [ ] Changelog entry: {changelog_check}

## Detailed Feedback

### 🌟 What's Great
{positive_feedback}

### 🔍 Issues Found

#### Critical (Must Fix)
1. **{critical_issue_1}**
   - Location: `{critical_location_1}`
   - Issue: {critical_description_1}
   - Suggestion: {critical_suggestion_1}

#### Major (Should Fix)
1. **{major_issue_1}**
   - Location: `{major_location_1}`
   - Issue: {major_description_1}
   - Suggestion: {major_suggestion_1}

#### Minor (Consider Fixing)
1. **{minor_issue_1}**
   - Location: `{minor_location_1}`
   - Issue: {minor_description_1}
   - Suggestion: {minor_suggestion_1}

### 💡 Suggestions for Improvement
{improvement_suggestions}

## Code Examples

### Current Implementation
```{language}
{current_code}
```

### Suggested Improvement
```{language}
{improved_code}
```

**Rationale**: {improvement_rationale}

## Overall Assessment

**Approval Status**: {approval_status}
**Confidence Level**: {confidence_level}/10
**Estimated Impact**: {impact_assessment}

## Action Items
- [ ] {action_item_1}
- [ ] {action_item_2}
- [ ] {action_item_3}

## Additional Notes
{additional_notes}""",
                "variables": ["pr_title", "pr_number", "author", "reviewer", "date", "files_changed",
                            "lines_added", "lines_removed", "pr_description", "patterns_check",
                            "solid_check", "abstractions_check", "overengineering_check",
                            "readability_check", "dry_check", "naming_check", "complexity_check",
                            "unit_tests_check", "integration_tests_check", "edge_cases_check",
                            "coverage_check", "input_validation_check", "secrets_check",
                            "sql_injection_check", "xss_check", "auth_check", "n_plus_one_check",
                            "algorithm_check", "caching_check", "indexes_check", "comments_check",
                            "readme_check", "api_docs_check", "changelog_check", "positive_feedback",
                            "critical_issue_1", "critical_location_1", "critical_description_1",
                            "critical_suggestion_1", "major_issue_1", "major_location_1",
                            "major_description_1", "major_suggestion_1", "minor_issue_1",
                            "minor_location_1", "minor_description_1", "minor_suggestion_1",
                            "improvement_suggestions", "language", "current_code", "improved_code",
                            "improvement_rationale", "approval_status", "confidence_level",
                            "impact_assessment", "action_item_1", "action_item_2", "action_item_3",
                            "additional_notes"],
                "examples": ["Feature PR review", "Bug fix review", "Refactoring review"],
                "best_practices": ["Be constructive", "Provide examples", "Focus on learning", "Acknowledge good work"],
                "example": "Code Review: Authentication System Enhancement..."
            },
            
            "stakeholder_update": {
                "name": "Stakeholder Update Email",
                "domain": "communication",
                "template": """Subject: {project_name} - {update_type} Update - {date}

Dear {stakeholder_group},

I hope this email finds you well. I'm writing to provide you with an update on {project_name}.

## Executive Summary

{executive_summary}

**Overall Status**: {overall_status_emoji} {overall_status}
**Timeline**: {timeline_status}
**Budget**: {budget_status}
**Risk Level**: {risk_level}

## Key Accomplishments ({reporting_period})

✅ {accomplishment_1}
   - Impact: {accomplishment_1_impact}
   
✅ {accomplishment_2}
   - Impact: {accomplishment_2_impact}
   
✅ {accomplishment_3}
   - Impact: {accomplishment_3_impact}

## Current Focus

{current_focus_description}

### In Progress
- {in_progress_1} ({progress_1}% complete)
- {in_progress_2} ({progress_2}% complete)
- {in_progress_3} ({progress_3}% complete)

## Upcoming Milestones

| Milestone | Target Date | Status |
|-----------|------------|---------|
| {milestone_1} | {date_1} | {status_1} |
| {milestone_2} | {date_2} | {status_2} |
| {milestone_3} | {date_3} | {status_3} |

## Challenges & Mitigation

### Challenge 1: {challenge_1}
- **Impact**: {challenge_1_impact}
- **Mitigation**: {challenge_1_mitigation}
- **Status**: {challenge_1_status}

### Challenge 2: {challenge_2}
- **Impact**: {challenge_2_impact}
- **Mitigation**: {challenge_2_mitigation}
- **Status**: {challenge_2_status}

## Decisions Needed

{decision_context}

1. **{decision_1}**
   - Options: {decision_1_options}
   - Recommendation: {decision_1_recommendation}
   - Needed by: {decision_1_deadline}

## Metrics & KPIs

- {metric_1}: {metric_1_value} ({metric_1_trend} from last period)
- {metric_2}: {metric_2_value} ({metric_2_trend} from last period)
- {metric_3}: {metric_3_value} ({metric_3_trend} from last period)

## Next Steps

1. {next_step_1}
2. {next_step_2}
3. {next_step_3}

## Questions or Concerns?

Please don't hesitate to reach out if you have any questions or would like to discuss any aspect of the project in more detail.

{closing_note}

Best regards,
{sender_name}
{sender_title}
{contact_information}

---
📎 Attachments: {attachments_list}
📊 Detailed Report: {detailed_report_link}""",
                "variables": ["project_name", "update_type", "date", "stakeholder_group",
                            "executive_summary", "overall_status_emoji", "overall_status",
                            "timeline_status", "budget_status", "risk_level", "reporting_period",
                            "accomplishment_1", "accomplishment_1_impact", "accomplishment_2",
                            "accomplishment_2_impact", "accomplishment_3", "accomplishment_3_impact",
                            "current_focus_description", "in_progress_1", "progress_1",
                            "in_progress_2", "progress_2", "in_progress_3", "progress_3",
                            "milestone_1", "date_1", "status_1", "milestone_2", "date_2",
                            "status_2", "milestone_3", "date_3", "status_3", "challenge_1",
                            "challenge_1_impact", "challenge_1_mitigation", "challenge_1_status",
                            "challenge_2", "challenge_2_impact", "challenge_2_mitigation",
                            "challenge_2_status", "decision_context", "decision_1",
                            "decision_1_options", "decision_1_recommendation", "decision_1_deadline",
                            "metric_1", "metric_1_value", "metric_1_trend", "metric_2",
                            "metric_2_value", "metric_2_trend", "metric_3", "metric_3_value",
                            "metric_3_trend", "next_step_1", "next_step_2", "next_step_3",
                            "closing_note", "sender_name", "sender_title", "contact_information",
                            "attachments_list", "detailed_report_link"],
                "examples": ["Weekly status update", "Monthly executive briefing", "Project milestone update"],
                "best_practices": ["Lead with key info", "Use visuals", "Be specific about needs", "Maintain regular cadence"],
                "example": "Project Update: Q3 Platform Migration..."
            },
            
            "okr_planning": {
                "name": "OKR Planning Framework",
                "domain": "strategy",
                "template": """# OKR Planning: {period} {year}

**Organization/Team**: {team_name}
**Mission**: {mission_statement}
**Vision**: {vision_statement}

## Strategic Context

### Previous Period Review
- Achievement Rate: {previous_achievement_rate}%
- Key Learnings: {key_learnings}
- Carry-over Items: {carryover_items}

### Current Landscape
- Market Conditions: {market_conditions}
- Competitive Position: {competitive_position}
- Internal Capabilities: {internal_capabilities}

## Company/Team OKRs

### Objective 1: {objective_1}
*{objective_1_description}*

**Why This Matters**: {objective_1_rationale}

#### Key Results:
1. **KR1**: {o1_kr1}
   - Baseline: {o1_kr1_baseline}
   - Target: {o1_kr1_target}
   - Owner: {o1_kr1_owner}
   
2. **KR2**: {o1_kr2}
   - Baseline: {o1_kr2_baseline}
   - Target: {o1_kr2_target}
   - Owner: {o1_kr2_owner}
   
3. **KR3**: {o1_kr3}
   - Baseline: {o1_kr3_baseline}
   - Target: {o1_kr3_target}
   - Owner: {o1_kr3_owner}

#### Initiatives:
- {o1_initiative_1}
- {o1_initiative_2}
- {o1_initiative_3}

### Objective 2: {objective_2}
*{objective_2_description}*

**Why This Matters**: {objective_2_rationale}

#### Key Results:
1. **KR1**: {o2_kr1}
   - Baseline: {o2_kr1_baseline}
   - Target: {o2_kr1_target}
   - Owner: {o2_kr1_owner}
   
2. **KR2**: {o2_kr2}
   - Baseline: {o2_kr2_baseline}
   - Target: {o2_kr2_target}
   - Owner: {o2_kr2_owner}
   
3. **KR3**: {o2_kr3}
   - Baseline: {o2_kr3_baseline}
   - Target: {o2_kr3_target}
   - Owner: {o2_kr3_owner}

#### Initiatives:
- {o2_initiative_1}
- {o2_initiative_2}
- {o2_initiative_3}

### Objective 3: {objective_3}
*{objective_3_description}*

**Why This Matters**: {objective_3_rationale}

#### Key Results:
1. **KR1**: {o3_kr1}
   - Baseline: {o3_kr1_baseline}
   - Target: {o3_kr1_target}
   - Owner: {o3_kr1_owner}
   
2. **KR2**: {o3_kr2}
   - Baseline: {o3_kr2_baseline}
   - Target: {o3_kr2_target}
   - Owner: {o3_kr2_owner}
   
3. **KR3**: {o3_kr3}
   - Baseline: {o3_kr3_baseline}
   - Target: {o3_kr3_target}
   - Owner: {o3_kr3_owner}

#### Initiatives:
- {o3_initiative_1}
- {o3_initiative_2}
- {o3_initiative_3}

## Alignment & Dependencies

### Cross-functional Dependencies
- {dependency_1}: {dependency_1_details}
- {dependency_2}: {dependency_2_details}

### Resource Requirements
- Headcount: {headcount_needs}
- Budget: {budget_needs}
- Tools/Systems: {tools_needs}

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {risk_1} | {risk_1_prob} | {risk_1_impact} | {risk_1_mitigation} |
| {risk_2} | {risk_2_prob} | {risk_2_impact} | {risk_2_mitigation} |

## Success Metrics

### Leading Indicators
- {leading_indicator_1}
- {leading_indicator_2}

### Lagging Indicators
- {lagging_indicator_1}
- {lagging_indicator_2}

## Review Cadence

- **Weekly**: {weekly_review_format}
- **Monthly**: {monthly_review_format}
- **Quarterly**: {quarterly_review_format}

## Communication Plan

- **Updates**: {update_frequency} via {update_channel}
- **Dashboards**: {dashboard_location}
- **Stakeholders**: {stakeholder_list}""",
                "variables": ["period", "year", "team_name", "mission_statement", "vision_statement",
                            "previous_achievement_rate", "key_learnings", "carryover_items",
                            "market_conditions", "competitive_position", "internal_capabilities",
                            "objective_1", "objective_1_description", "objective_1_rationale",
                            "o1_kr1", "o1_kr1_baseline", "o1_kr1_target", "o1_kr1_owner",
                            "o1_kr2", "o1_kr2_baseline", "o1_kr2_target", "o1_kr2_owner",
                            "o1_kr3", "o1_kr3_baseline", "o1_kr3_target", "o1_kr3_owner",
                            "o1_initiative_1", "o1_initiative_2", "o1_initiative_3",
                            "objective_2", "objective_2_description", "objective_2_rationale",
                            "o2_kr1", "o2_kr1_baseline", "o2_kr1_target", "o2_kr1_owner",
                            "o2_kr2", "o2_kr2_baseline", "o2_kr2_target", "o2_kr2_owner",
                            "o2_kr3", "o2_kr3_baseline", "o2_kr3_target", "o2_kr3_owner",
                            "o2_initiative_1", "o2_initiative_2", "o2_initiative_3",
                            "objective_3", "objective_3_description", "objective_3_rationale",
                            "o3_kr1", "o3_kr1_baseline", "o3_kr1_target", "o3_kr1_owner",
                            "o3_kr2", "o3_kr2_baseline", "o3_kr2_target", "o3_kr2_owner",
                            "o3_kr3", "o3_kr3_baseline", "o3_kr3_target", "o3_kr3_owner",
                            "o3_initiative_1", "o3_initiative_2", "o3_initiative_3",
                            "dependency_1", "dependency_1_details", "dependency_2", "dependency_2_details",
                            "headcount_needs", "budget_needs", "tools_needs", "risk_1", "risk_1_prob",
                            "risk_1_impact", "risk_1_mitigation", "risk_2", "risk_2_prob",
                            "risk_2_impact", "risk_2_mitigation", "leading_indicator_1",
                            "leading_indicator_2", "lagging_indicator_1", "lagging_indicator_2",
                            "weekly_review_format", "monthly_review_format", "quarterly_review_format",
                            "update_frequency", "update_channel", "dashboard_location", "stakeholder_list"],
                "examples": ["Quarterly OKRs", "Annual company OKRs", "Team OKRs", "Product OKRs"],
                "best_practices": ["Limit to 3-5 objectives", "Make KRs measurable", "Ambitious but achievable", "Regular reviews"],
                "example": "OKR Planning: Q4 2024 Engineering Team..."
            },
            
            "standard_operating_procedure": {
                "name": "Standard Operating Procedure (SOP)",
                "domain": "operations",
                "template": """# Standard Operating Procedure: {procedure_name}

**SOP ID**: {sop_id}
**Version**: {version}
**Effective Date**: {effective_date}
**Review Date**: {review_date}
**Owner**: {owner}
**Approved By**: {approver}

## 1. Purpose

{purpose_statement}

## 2. Scope

### Applies To
- {applies_to_1}
- {applies_to_2}
- {applies_to_3}

### Does Not Apply To
- {exception_1}
- {exception_2}

## 3. Definitions

| Term | Definition |
|------|------------|
| {term_1} | {definition_1} |
| {term_2} | {definition_2} |
| {term_3} | {definition_3} |

## 4. Responsibilities

### {role_1}
- {role_1_responsibility_1}
- {role_1_responsibility_2}

### {role_2}
- {role_2_responsibility_1}
- {role_2_responsibility_2}

### {role_3}
- {role_3_responsibility_1}
- {role_3_responsibility_2}

## 5. Prerequisites

### Required Resources
- {resource_1}
- {resource_2}
- {resource_3}

### Required Access/Permissions
- {permission_1}
- {permission_2}

### Required Training
- {training_1}
- {training_2}

## 6. Procedure

### Step 1: {step_1_title}
**Responsible**: {step_1_responsible}
**Duration**: {step_1_duration}

1.1 {step_1_substep_1}
    - {step_1_detail_1}
    
1.2 {step_1_substep_2}
    - {step_1_detail_2}
    
**Checkpoint**: {step_1_checkpoint}

### Step 2: {step_2_title}
**Responsible**: {step_2_responsible}
**Duration**: {step_2_duration}

2.1 {step_2_substep_1}
    - {step_2_detail_1}
    
2.2 {step_2_substep_2}
    - {step_2_detail_2}
    
**Checkpoint**: {step_2_checkpoint}

### Step 3: {step_3_title}
**Responsible**: {step_3_responsible}
**Duration**: {step_3_duration}

3.1 {step_3_substep_1}
    - {step_3_detail_1}
    
3.2 {step_3_substep_2}
    - {step_3_detail_2}
    
**Checkpoint**: {step_3_checkpoint}

## 7. Decision Points

### Decision 1: {decision_1}
- **If** {condition_1}: Go to Step {goto_1}
- **If** {condition_2}: Go to Step {goto_2}

## 8. Quality Checks

| Check Point | Criteria | Action if Failed |
|-------------|----------|------------------|
| {check_1} | {criteria_1} | {action_1} |
| {check_2} | {criteria_2} | {action_2} |

## 9. Error Handling

### Common Errors

#### Error: {error_1}
- **Symptoms**: {error_1_symptoms}
- **Resolution**: {error_1_resolution}
- **Prevention**: {error_1_prevention}

#### Error: {error_2}
- **Symptoms**: {error_2_symptoms}
- **Resolution**: {error_2_resolution}
- **Prevention**: {error_2_prevention}

## 10. Documentation

### Required Records
- {record_1}: Stored in {location_1}
- {record_2}: Stored in {location_2}

### Retention Period
- {retention_policy}

## 11. Key Performance Indicators

- {kpi_1}: Target = {kpi_1_target}
- {kpi_2}: Target = {kpi_2_target}
- {kpi_3}: Target = {kpi_3_target}

## 12. References

- {reference_1}
- {reference_2}
- {reference_3}

## 13. Revision History

| Version | Date | Changes | Author |
|---------|------|---------|---------|
| {version_1} | {date_1} | {changes_1} | {author_1} |
| {version_2} | {date_2} | {changes_2} | {author_2} |

## 14. Appendices

### Appendix A: {appendix_a_title}
{appendix_a_content}

### Appendix B: Forms and Templates
- {form_1}: {form_1_location}
- {form_2}: {form_2_location}""",
                "variables": ["procedure_name", "sop_id", "version", "effective_date", "review_date",
                            "owner", "approver", "purpose_statement", "applies_to_1", "applies_to_2",
                            "applies_to_3", "exception_1", "exception_2", "term_1", "definition_1",
                            "term_2", "definition_2", "term_3", "definition_3", "role_1",
                            "role_1_responsibility_1", "role_1_responsibility_2", "role_2",
                            "role_2_responsibility_1", "role_2_responsibility_2", "role_3",
                            "role_3_responsibility_1", "role_3_responsibility_2", "resource_1",
                            "resource_2", "resource_3", "permission_1", "permission_2", "training_1",
                            "training_2", "step_1_title", "step_1_responsible", "step_1_duration",
                            "step_1_substep_1", "step_1_detail_1", "step_1_substep_2", "step_1_detail_2",
                            "step_1_checkpoint", "step_2_title", "step_2_responsible", "step_2_duration",
                            "step_2_substep_1", "step_2_detail_1", "step_2_substep_2", "step_2_detail_2",
                            "step_2_checkpoint", "step_3_title", "step_3_responsible", "step_3_duration",
                            "step_3_substep_1", "step_3_detail_1", "step_3_substep_2", "step_3_detail_2",
                            "step_3_checkpoint", "decision_1", "condition_1", "goto_1", "condition_2",
                            "goto_2", "check_1", "criteria_1", "action_1", "check_2", "criteria_2",
                            "action_2", "error_1", "error_1_symptoms", "error_1_resolution",
                            "error_1_prevention", "error_2", "error_2_symptoms", "error_2_resolution",
                            "error_2_prevention", "record_1", "location_1", "record_2", "location_2",
                            "retention_policy", "kpi_1", "kpi_1_target", "kpi_2", "kpi_2_target",
                            "kpi_3", "kpi_3_target", "reference_1", "reference_2", "reference_3",
                            "version_1", "date_1", "changes_1", "author_1", "version_2", "date_2",
                            "changes_2", "author_2", "appendix_a_title", "appendix_a_content",
                            "form_1", "form_1_location", "form_2", "form_2_location"],
                "examples": ["Customer onboarding", "Incident response", "Release management", "Data backup"],
                "best_practices": ["Be specific", "Include visuals", "Test procedures", "Regular updates"],
                "example": "SOP: Customer Support Ticket Escalation..."
            }
        }
        
        # Add professional templates to the main templates dictionary
        for template_key, config in professional_templates.items():
            self.templates[template_key] = PromptTemplate(
                name=config["name"],
                domain=config["domain"],
                template=config["template"],
                variables=config["variables"],
                example=config["example"],
                best_practices=config.get("best_practices", []),
                examples=config.get("examples", [])
            )

    def _load_additional_use_cases(self):
        """Load additional useful templates from the simplified version"""
        additional_templates = {
            # Contract and Legal Templates
            "client_contract_termination": {
                "name": "Client Contract Termination Letter",
                "domain": "legal",
                "template": """Create a professional, respectful client contract termination letter.

**Company Information**
- Your Company Name: {company_name}
- Client Name: {client_name}
- Service/Product Provided: {service_description}

**Contract Details**
- Contract Start Date: {start_date}
- Contract End/Termination Date: {end_date}
- Reason for Termination: {termination_reason}
- Notice Period Required: {notice_period}

**Outstanding Items**
- Remaining Deliverables: {remaining_deliverables}
- Final Payment Information: {payment_details}
- Transition Plans: {transition_details}

**Letter Requirements:**
1. Professional opening stating the purpose
2. Reference to specific contract and termination clauses
3. Clear explanation of termination reason in neutral language
4. Details on remaining obligations for both parties
5. Information on transition process
6. Expression of appreciation for business relationship
7. Contact information for transition questions
8. Professional closing

**Tone Guidelines:**
- Professional and business-appropriate
- Respectful and appreciative
- Clear but not overly blunt
- Non-emotional and factual
- Forward-looking where appropriate

**Avoid:**
- Blame or accusatory language
- Unnecessary details or explanations
- Emotional expressions
- Burning bridges""",
                "variables": ["company_name", "client_name", "service_description", "start_date", 
                            "end_date", "termination_reason", "notice_period", "remaining_deliverables",
                            "payment_details", "transition_details"],
                "examples": ["Service contract termination", "Project completion termination", "Breach-based termination"],
                "best_practices": ["Maintain professionalism", "Document everything", "Preserve relationships where possible"],
                "example": "Professional termination letter for software development services..."
            },
            
            "client_feedback_survey": {
                "name": "Client Feedback Survey Design",
                "domain": "customer_experience",
                "template": """Design a comprehensive client feedback survey to gather actionable insights.

**Survey Context**
- Service/Product Type: {service_type}
- Client Relationship Stage: {relationship_stage}
- Key Areas to Evaluate: {evaluation_areas}
- Survey Purpose: {survey_purpose}
- Follow-up Plans: {followup_plans}
- Distribution Method: {distribution_method}

**Survey Structure:**

**1. Introduction Section**
- Purpose statement and expected completion time
- Confidentiality assurance
- How feedback will be used

**2. Quantitative Questions**
- Satisfaction ratings (1-5 or 1-10 scale)
- Net Promoter Score question
- Multiple choice for specific aspects

**3. Qualitative Questions**
- Open-ended experience questions
- Specific improvement suggestions
- Success stories and challenges

**4. Service-Specific Questions**
- Questions targeting the specific service provided
- Team member performance evaluation
- Communication effectiveness assessment

**5. Future Needs Assessment**
- Questions about upcoming needs
- Interest in additional services
- Preferred communication methods

**6. Closing Section**
- Thank you message
- Next steps information
- Contact details for questions

**Design Guidelines:**
- Keep survey concise yet comprehensive
- Use clear, unbiased questions
- Include skip logic where appropriate
- Target 5-7 minutes completion time""",
                "variables": ["service_type", "relationship_stage", "evaluation_areas", "survey_purpose",
                            "followup_plans", "distribution_method"],
                "examples": ["Post-project survey", "Annual relationship review", "Service improvement survey"],
                "best_practices": ["Keep it short", "Avoid leading questions", "Include both ratings and open text"],
                "example": "Client feedback survey for consulting services completion..."
            },
            
            # Project Management Templates
            "crisis_communication": {
                "name": "Crisis Communication Message",
                "domain": "communication",
                "template": """Draft a comprehensive crisis communication message for stakeholders.

**Crisis Context**
- Situation: {crisis_situation}
- Target Audience: {target_audience}
- Nature of Crisis: {crisis_description}
- Current Status: {current_status}
- Stakeholder Impact: {stakeholder_impact}

**Actions and Plans**
- Actions Already Taken: {actions_taken}
- Planned Next Steps: {planned_steps}
- Key Facts to Communicate: {key_facts}
- Potential Concerns to Address: {potential_concerns}
- Communication Channels: {communication_channels}

**Message Structure:**
1. Clear, direct acknowledgment of the situation
2. Accurate, relevant facts without unnecessary detail
3. Demonstration of empathy for those affected
4. Clear explanation of actions being taken
5. Specific guidance if stakeholders need to take action
6. Timeline for additional updates
7. Appropriate contact information for questions

**Communication Principles:**
- Transparency and honesty
- Timeliness and urgency
- Empathy and concern
- Clear action items
- Consistent messaging across channels""",
                "variables": ["crisis_situation", "target_audience", "crisis_description", "current_status",
                            "stakeholder_impact", "actions_taken", "planned_steps", "key_facts",
                            "potential_concerns", "communication_channels"],
                "examples": ["Security breach notification", "Service outage communication", "Product recall notice"],
                "best_practices": ["Be transparent", "Show empathy", "Provide clear next steps", "Update regularly"],
                "example": "Crisis communication for data security incident..."
            },
            
            # Data and Analytics Templates
            "data_insights_analysis": {
                "name": "Data Insights Analysis Framework",
                "domain": "data_analysis",
                "template": """Analyze data findings to extract actionable business insights.

**Analysis Context**
- Data Subject: {data_subject}
- Analysis Period: {analysis_period}
- Data Findings: {data_findings}
- Target Audience: {target_audience}
- Business Context: {business_context}

**Analysis Framework:**

**1. Key Insights Identification**
Identify the 3-5 most significant patterns or insights:
- {insight_1_pattern}
- {insight_2_pattern}
- {insight_3_pattern}

**2. Business Implications**
For each insight, explain potential business implications:
- Impact on revenue/costs
- Operational implications
- Strategic considerations
- Risk factors

**3. Actionable Recommendations**
Provide specific, prioritized recommendations:
- High-impact, low-effort quick wins
- Medium-term strategic initiatives
- Long-term transformation opportunities

**4. Implementation Roadmap**
- Immediate actions (0-30 days)
- Short-term initiatives (1-3 months)
- Long-term strategies (3+ months)

**5. Success Metrics**
Define how to measure implementation effectiveness:
- Leading indicators
- Lagging indicators
- Success criteria

**6. Analysis Limitations**
- Data quality constraints
- Sample size limitations
- Potential biases
- Recommendations for additional data""",
                "variables": ["data_subject", "analysis_period", "data_findings", "target_audience",
                            "business_context", "insight_1_pattern", "insight_2_pattern", "insight_3_pattern"],
                "examples": ["Customer behavior analysis", "Sales performance review", "Marketing campaign effectiveness"],
                "best_practices": ["Focus on actionability", "Quantify impact where possible", "Consider implementation feasibility"],
                "example": "Customer churn analysis insights and recommendations..."
            },
            
            # Meeting and Facilitation Templates
            "effective_meeting_agenda": {
                "name": "Effective Meeting Agenda Creator",
                "domain": "meeting_management",
                "template": """Create a detailed and effective meeting agenda for productive outcomes.

**Meeting Details**
- Meeting Title: {meeting_title}
- Meeting Purpose: {meeting_purpose}
- Attendees: {attendees}
- Date: {meeting_date}
- Time: {meeting_time}
- Duration: {duration}
- Key Objectives: {meeting_objectives}

**Agenda Structure:**

**1. Opening (5-10% of total time)**
- Welcome and introductions (if necessary)
- Review and approval of previous meeting minutes
- Review of agenda and objectives

**2. Information Sharing/Updates (20-30% of total time)**
- Brief updates on relevant topics (assign presenters)
- Key data or reports to be shared
- Status updates from team members

**3. Discussion/Decision-Making (40-50% of total time)**
- Specific topics for discussion with clear questions
- Decisions that need to be made
- Time allocation for each discussion point
- Discussion leaders identified

**4. Action Items/Next Steps (10-15% of total time)**
- Summarize decisions made
- Assign clear action items with owners and deadlines
- Review next steps and follow-up plan

**5. Closing (5% of total time)**
- Recap of key decisions and action items
- Confirm next meeting date/time (if applicable)
- Adjourn

**Meeting Guidelines:**
- Each agenda item has clear purpose and assigned lead
- Estimated time for each section
- Promotes active participation
- Efficient use of meeting time""",
                "variables": ["meeting_title", "meeting_purpose", "attendees", "meeting_date",
                            "meeting_time", "duration", "meeting_objectives"],
                "examples": ["Weekly team meeting", "Project kickoff", "Strategic planning session"],
                "best_practices": ["Send agenda in advance", "Stick to time limits", "Assign clear owners", "Follow up on action items"],
                "example": "Weekly product team standup agenda..."
            }
        }
        
        # Add additional templates to the main templates dictionary
        for template_key, config in additional_templates.items():
            self.templates[template_key] = PromptTemplate(
                name=config["name"],
                domain=config["domain"],
                template=config["template"],
                variables=config["variables"],
                example=config["example"],
                best_practices=config.get("best_practices", []),
                examples=config.get("examples", [])
            )

    def get_template(self, name: str) -> Optional[PromptTemplate]:
        """Get a template by name"""
        return self.templates.get(name)
    
    def list_templates(self, domain: str = None) -> List[str]:
        """List all available templates, optionally filtered by domain"""
        if domain:
            # Filter templates by domain
            return [key for key, template in self.templates.items() 
                   if template.domain == domain]
        return list(self.templates.keys())
    
    def get_templates_by_domain(self, domain: str) -> List[PromptTemplate]:
        """Get all templates for a specific domain"""
        return [t for t in self.templates.values() if t.domain == domain]
    
    def list_templates_by_domain(self) -> Dict[str, List[Dict[str, str]]]:
        """List all templates organized by domain"""
        domains = {}
        for name, template in self.templates.items():
            if template.domain not in domains:
                domains[template.domain] = []
            domains[template.domain].append({
                "key": name,
                "name": template.name,
                "description": f"Variables: {len(template.variables)} | Examples: {', '.join(template.examples[:2]) if template.examples else 'N/A'}"
            })
        return domains
    
    def search_templates(self, query: str) -> List[Dict[str, Any]]:
        """Search templates by name, domain, or content"""
        query_lower = query.lower()
        results = []
        
        for key, template in self.templates.items():
            if (query_lower in key.lower() or 
                query_lower in template.name.lower() or 
                query_lower in template.domain.lower() or
                query_lower in template.template.lower()):
                results.append({
                    "key": key,
                    "name": template.name,
                    "domain": template.domain,
                    "variables_count": len(template.variables),
                    "examples": template.examples or [],
                    "best_practices": template.best_practices or []
                })
        return results
    
    def render_template(self, name: str, variables: Dict[str, str]) -> str:
        """Render a template with provided variables"""
        template = self.get_template(name)
        if not template:
            raise ValueError(f"Template '{name}' not found")
            
        # Check for missing variables
        missing_vars = set(template.variables) - set(variables.keys())
        if missing_vars:
            raise ValueError(f"Missing required variables: {missing_vars}")
            
        # Render the template
        rendered = template.template
        for var, value in variables.items():
            rendered = rendered.replace(f"{{{var}}}", str(value))
            
        return rendered
    
    def get_template_info(self, name: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a template"""
        template = self.get_template(name)
        if not template:
            return None
            
        return {
            "name": template.name,
            "domain": template.domain,
            "variables": template.variables,
            "variables_count": len(template.variables),
            "example": template.example,
            "examples": template.examples or [],
            "best_practices": template.best_practices or [],
            "template_preview": template.template[:500] + "..." if len(template.template) > 500 else template.template
        }