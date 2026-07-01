# 🌐 Global Rules

> Applies to: ALL Agents

---

## 1. Zero Hallucination Policy
- NEVER invent or assume requirements that do not exist in the source documents.
- NEVER fabricate evidence, quotes, or document references.
- If information is missing, explicitly report it as **[MISSING]**. Do not attempt to fill in the blanks using industry standards unless specifically advising as a recommendation.

## 2. Evidence-Based Reasoning
- Every finding MUST reference the source document and section.
- Every finding MUST include a direct quote from the text.
- If a feature is missing, state exactly which document and section was searched.

## 3. Severity & Priority Definitions
When classifying findings or gaps, use the following scale:

- 🔴 **Critical (P0)**: System cannot function, blocks core business flow, or causes severe data corruption/security breach. Must be fixed immediately.
- 🟠 **High (P1)**: Major feature failure with no workaround. High business impact.
- 🟡 **Medium (P2)**: Non-critical feature failure, edge case defect, or has a viable workaround.
- 🟢 **Low (P3)**: Minor UI/UX issue, typo, or slight ambiguity that does not block development.

## 4. Output Formatting
- Always output valid Markdown.
- Use tables for structured data (Coverage matrix, Test case steps).
- Use blockquotes (`>`) for evidence text.
