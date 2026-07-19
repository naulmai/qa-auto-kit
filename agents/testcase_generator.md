# 🛠 Test Case Generator Skill (Production Version)

---

## 🧩 Skill Metadata

- **name:** testcase_generator
- **version:** 3.0.0
- **category:** QA / Test Design
- **description:** Generate enterprise-level manual test cases from software requirements using standardized QA test design techniques. Produces executable, traceable, and review-ready test suites.

---

## 🎯 Purpose

Generate a complete, executable, traceable, and review-ready manual test suite directly from software requirements while ensuring coverage, quality, and automation readiness.

---

## 📥 Inputs

### Required
- `docs/requirements/*` (SRS, PRD, BRD, or any requirement document)

### Secondary
- `docs/designs/*` (UI Flow, Wireframes, Design descriptions)

### Optional (Cross-Reference Inputs)
- `reports/*_Test_Scenarios_Report.md` (from scenario_generator — primary scenario source)
- `reports/*_Req_Gap_Report.md` (from requirement_gap_analyst — identifies gaps to cover)
- `reports/*_Risk_Analysis_Report.md` (from risk_analyst — drives priority assignment)
- `reports/*_Edge_Case_Report.md` (from advanced_edge_case_analyzer — edge cases to include)
- `reports/design_audit.md` (from design_auditor — UI-specific test cases)

---

## 📤 Output

📄 `reports/[Requirement_Name]_Testcases.md`
📄 `reports/[Requirement_Name]_Testcases.csv` (For Excel / Test Management Tool import)

Use output template:

📄 `templates/testcases.md`

---

## ⚙️ Processing Engines

Execute the following engines **sequentially**. No engine may be skipped.

### Engine 1: Requirement Analysis
- Read all documents from `docs/requirements/*`.
- Identify functional requirements, business rules, constraints, user roles.
- If `reports/*_Req_Gap_Report.md` exists → incorporate gap findings as additional test targets.
- Decompose compound requirements into atomic functional behaviors.

### Engine 2: Input Cross-Reference
- If `reports/test_scenarios.md` exists → use scenarios as the primary skeleton for test case generation.
- If `reports/risk_analysis.md` exists → use risk levels to assign priority (Critical→High, High→High, Medium→Medium, Low→Low).
- If `reports/edge_case_report.md` exists → generate dedicated test cases for each edge case finding.
- If `reports/design_audit.md` exists → generate UI-specific test cases for each design defect.

### Engine 3: Test Design
- Apply all test design techniques defined in `rules/test_generation_rules.md`:
  - Happy Path, Negative Testing, BVA, Equivalence Partitioning
  - State Transition, Decision Table, Role-Based, Error Guessing
  - Error Handling, Security, Performance, UI/UX, Regression
- These techniques are internal reasoning tools — do NOT print them in output unless explicitly requested.

### Engine 4: Test Case Generation
- Generate test cases following the exact output structure defined in `templates/testcases.md`.
- Each test case validates ONE business objective (atomicity rule).
- Each step performs ONE user action.
- Use realistic, executable test data.
- Expected results must be observable, measurable, and deterministic.

### Engine 5: Requirement Traceability
- Every test case MUST map to at least one Requirement ID (FR ID).
- Every requirement must have at least one test case.
- Build traceability links: Requirement → Scenario → Test Case.

### Engine 6: Coverage Enforcement
- Validate coverage distribution against thresholds in `rules/test_generation_rules.md`.
- If any category is below threshold → generate additional test cases.
- Ensure minimum test case counts based on feature size.

### Engine 7: Quality Validation
- Verify test data is realistic (not "Valid Email" or "Sample Data").
- Verify expected results are specific (not "Works correctly" or "Pass").
- Verify test steps use action verbs (Launch, Navigate, Tap, Enter, Verify).
- Verify no duplicate test cases exist.

### Engine 8: Self Review
- Run the Self Audit Engine defined in `rules/test_generation_rules.md` Section 15.
- Output audit reasoning inside `<audit_trace>` block before the final table.
- If ANY audit step fails → regenerate affected test cases and re-validate.

### Engine 9: Output Formatting
- Format output strictly following `templates/testcases.md`.
- Use HTML `<br>` tags for multi-step cells.
- Ensure TC_IDs are unique and sequential.
- Apply Token Limit Handling if suite exceeds 40 test cases.

### Engine 10: Post-Generation CSV Export
- Do **not** attempt to generate CSV text directly in the output.
- After the markdown table is successfully saved to `reports/[Requirement_Name]_Testcases.md`, the system (or orchestrator) shall execute the conversion script:
  `python scripts/md_to_csv.py reports/[Requirement_Name]_Testcases.md reports/[Requirement_Name]_Testcases.csv`

---

## 📜 Invoke Rules

- `rules/global_rules.md`
- `rules/test_generation_rules.md`

---

## 🔁 Failure Handling

### If requirement documents are missing:
- **STOP** execution.
- Output: "No requirement documents found in docs/requirements/."

### If requirement is ambiguous:
- Generate best-effort test cases.
- Mark Remarks = `ASSUMPTION_BASED`.

### If design documents are unavailable:
- Generate test cases using requirements only.
- Skip UI-specific test case generation.

### If scenario or risk reports are unavailable:
- Generate test cases directly from requirements.
- Mark confidence as Medium for priority assignments.

### Never invent undocumented features.

---

## ⚙️ Execution Principle

The generator shall complete **every** processing engine before producing output.

No partial execution is allowed.