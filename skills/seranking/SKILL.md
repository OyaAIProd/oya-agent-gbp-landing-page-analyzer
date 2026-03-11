---
name: seranking
display_name: "SE Ranking"
description: "Backlink analysis and domain rating via SE Ranking API"
category: seo
icon: trending-up
skill_type: sandbox
catalog_type: addon
requirements: "httpx>=0.25"
resource_requirements:
  - env_var: SERANKING_API_KEY
    name: "SE Ranking API Key"
    description: "SE Ranking API key (UUID format, found in account settings)"
config_schema:
  properties:
    default_target:
      type: string
      label: "Default Target Domain"
      description: "Default domain to analyze when not specified"
      placeholder: "example.com"
      group: defaults
    competitor_domains:
      type: text
      label: "Competitor Domains"
      description: "Competitor domains to compare against (one per line)"
      placeholder: "competitor1.com\ncompetitor2.com\ncompetitor3.com"
      group: defaults
    analysis_rules:
      type: text
      label: "Analysis Rules"
      description: "Rules for backlink analysis behavior"
      placeholder: "- Always compare against competitor domains\n- Flag domains with rating below 30\n- Report domains losing backlinks month-over-month"
      group: rules
    report_template:
      type: text
      label: "Report Template"
      description: "Template for backlink reports"
      placeholder: "## Backlink Report: {domain}\n\nDomain Rating: {rating}/100\nTotal Backlinks: {backlinks}\n\n### Comparison\n{comparison}"
      group: templates
tool_schema:
  name: seranking
  description: "Backlink analysis and domain rating via SE Ranking API"
  parameters:
    type: object
    properties:
      action:
        type: "string"
        description: "Which operation to perform"
        enum: ['backlinks_summary']
      domain:
        type: "string"
        description: "Target domain to analyze"
    required: [action, domain]
---
# SE Ranking

Backlink analysis and domain rating powered by the SE Ranking API.

## Actions
- **backlinks_summary** — Get domain rating (0-100) and total backlink count for a domain. Provide `domain`.

## Notes
- Domain rating is on a 0-100 scale (similar to Ahrefs Domain Rating)
- Each request costs 100 SE Ranking credits
- Use this for quick domain authority checks; use DataForSEO for deeper backlink analysis
