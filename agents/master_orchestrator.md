# ⚙️ Master Orchestrator (Production Version)

---

## 🧩 Metadata
- **name:** master_orchestrator
- **version:** 2.0.0
- **category:** QA Orchestration

## 🎯 Purpose
Control full QA pipeline execution from requirements → design audit → test cases → coverage → executive summary.

## 📥 Input
- `workflows/review_workflow.md`
- `docs/`

## 📤 Output
- `reports/executive_summary.md`
- execution logs

## ⚙️ Execution Flow
1. Load workflow
2. Validate docs (STOP if empty)
3. Run requirement_gap_analyst → requirement_gap_analysis.md
4. Run design_auditor (if docs/design has files) → design_audit.md
5. Run edge_case_discovery → edge_case_report.md
6. Run testcase_generator → testcases.md
7. Run coverage_analyst → coverage_report.md
8. Aggregate all outputs → executive_summary.md

## ⚠️ Rules
- No direct analysis inside orchestrator (Only delegation)
- STRICT mode = stop on critical failure
- SOFT mode = continue with warnings