# 🧠 Requirement & Gap Analyst (Production Version)

---

## 🧩 Skill Metadata
- **name:** requirement_gap_analyst
- **version:** 3.0.0
- **category:** QA / Requirement Engineering / Traceability
- **description:** Advanced BA audit to detect internal logic defects (ambiguity, edge cases) AND external gaps (traceability, orphans) across documents.

---

## 🎯 Purpose
Perform a unified Senior BA + QA hybrid review of requirements to ensure:
- Business logic completeness & Quality (Internal Quality)
- Full traceability across PRD, BRD, and SRS (External Quality)

---

## 📥 Input
- Requirements: `docs/requirements/`
- Output: `reports/[Tên_File_Requirement]_Req_Gap_Report.md` (bắt buộc đặt tên theo tên của file requirement)
- Template: `templates/requirement_gap_report.md`

---

## ⚙️ Core Processing Engines

### Engine 1: Cross-Document Traceability (Gap Detection)
*Executes ONLY IF >= 2 documents are present in `docs/requirements/`.*
- **Missing Coverage**: Upstream feature missing in Downstream.
- **Partial Coverage**: Feature exists but lacks full implementation details.
- **Orphan / Gold Plating**: Downstream feature has no Upstream justification.
- **Inconsistency**: Conflicting terms, limits across docs.

### Engine 2: Internal Requirement Quality (Missing Logic & Defects)
*Executes on all individual documents.*
- **Ambiguity**: Undefined terms, missing quantification.
- **Missing Rules**: Permission, state transitions, validation rules.
- **Missing Edge Cases**: Boundary values, null input, partial failure flows.
- **Contradiction**: Rule conflicts within the same document.

---

## 📊 Output Format (Strict)
*Must follow `templates/requirement_gap_report.md` strictly.*

1. **Executive Summary**: Overall Score & Prioritized Counts.
2. **Traceability Gaps (Cross-Doc)**: Gap findings.
3. **Internal Logic Defects (Single-Doc)**: Ambiguity, missing rules, edge cases.
4. **Missing Requirement Map**: Missing flows, rules, states.
5. **Action Items**: Prioritized fixes (P0, P1, P2).

---

## ⚙️ Execution Principles
- If requirement is not testable → it is incomplete.
- If upstream feature is missing downstream → it is a gap.
- Every business rule must have: Input, Process, Output, Failure behavior.
