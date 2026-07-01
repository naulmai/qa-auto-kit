# 🛠 Test Case Generator Skill

---

## Metadata

- name: testcase_generator
- version: 3.0.0
- category: QA / Test Design
- description: Generate enterprise-level manual test cases from software requirements using standardized QA test design techniques.

---

## Purpose

Generate a complete, executable, traceable, and review-ready manual test suite directly from software requirements while ensuring coverage, quality, and automation readiness.

---

## Inputs

### Primary
- docs/SRS.md

### Secondary
- docs/UI.*
- docs/Flow.*
- docs/Design.*

### Optional
- reports/requirement_gap_analysis.md
- reports/design_audit.md
- reports/edge_case_report.md

---

## Output

reports/testcases.md

Use output template:

templates/testcases.md

---

## Processing Engine

Execute the following engines sequentially:

1. Requirement Analysis Engine
2. Requirement Decomposition Engine
3. Test Design Engine
4. Test Case Generation Engine
5. Requirement Traceability Engine
6. Coverage Enforcement Engine
7. Quality Validation Engine
8. Self Review Engine
9. Output Formatting Engine

---

## Invoke Rules

- rules/global_rules.md
- rules/test_generation_rules.md

---

## Failure Handling

If SRS is missing:
- STOP execution.

If requirement is ambiguous:
- Generate best-effort test cases.
- Mark Remarks = ASSUMPTION_BASED.

If UI document is unavailable:
- Generate using SRS only.

Never invent undocumented features.

---

## Execution Principle

The generator shall complete every processing engine before producing output.

No partial execution is allowed.