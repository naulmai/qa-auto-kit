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

## 5. Terminology Consistency
- Use consistent terminology throughout all reports.
- Standardized terms:
  - **Requirement** (not "spec", "feature request", or "item")
  - **Test Case** (not "test", "check", or "validation")
  - **Test Scenario** (not "test story" or "use case")
  - **Edge Case** (not "corner case" or "exception")
  - **Finding** (not "issue", "defect", or "bug" — unless confirmed as a defect)
  - **Gap** (not "hole", "miss", or "omission")
- When referencing document names, use the exact filename as it appears in `docs/`.

## 6. Output Language
- All report content (headings, findings, descriptions, recommendations) shall be written in **English**.
- Vietnamese may be used only when directly quoting a Vietnamese-language requirement document.
- Code examples, technical terms, and IDs are always in English.

## 7. Report Versioning
- Every generated report MUST include a `Document Metadata` section with the generation date.
- When regenerating a report for the same requirement document, the new report **completely replaces** the previous version (overwrite, not append).
- Do NOT maintain version history within the report itself. The Git history serves as the version control mechanism.
