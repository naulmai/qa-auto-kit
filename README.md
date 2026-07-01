# AI Manual Testing & Requirement Analysis Framework

An ultra-lean, **Agent-Based AI Framework** designed to perform Requirement Analysis, Gap Detection, Test Case Generation, and Coverage Analysis on software requirements.

> **Note**: This system focuses purely on analysis and manual test generation. It does NOT include CI/CD, automation testing, API testing, or database testing.

---

## Architecture

This framework uses a minimalist, deterministic, 5-agent architecture.

```text
Input Documents → Rules → Workflow → Agents → Output Reports
```

### Folder Structure

| Folder | Purpose |
|--------|---------|
| `docs/requirements/` | **Input**: PRD, BRD, SRS. |
| `docs/design/` | **Input**: UI Flow, Wireframes, Figma exports. |
| `reports/` | **Output**: Where all generated Markdown reports are saved. |
| `agents/` | **Core Logic**: Contains the definitions for the 5 analytical agents. |
| `workflows/` | **Orchestration**: Defines the execution order (1 single pipeline). |
| `rules/` | **Standards**: Global standards, requirement quality metrics, and reporting formats. |
| `templates/` | **Formatting**: Reusable Markdown templates for consistent report output. |

---

## The Agents (The Pipeline)

1. **`requirement_gap_analyst`**: Audits internal logic (ambiguity, edge cases) AND detects cross-document traceability gaps (e.g. PRD vs SRS).
2. **`design_auditor`**: Audits Design/UI flow against SRS to find missing components, error states, and flow mismatches.
3. **`edge_case_discovery`**: Discovers high-risk edge cases, concurrency issues, and system vulnerabilities.
4. **`testcase_generator`**: Directly generates step-by-step Manual Test Cases based on logic and design.
5. **`coverage_analyst`**: Maps the generated test cases back to the requirements to find any untested features.
6. **`master_orchestrator`**: The controller that runs the above 5 agents in order and produces the final Executive Summary.

---

## Execution Flow

To run the complete pipeline:

1. **Prepare Input**: Place your requirements in `docs/requirements/` and designs in `docs/design/`.
2. **Trigger Workflow**: Invoke the Master Orchestrator.
   ```text
   Run agents/master_orchestrator.md
   ```
3. **Pipeline Execution**:
   - The Orchestrator triggers `requirement_gap_analyst` → `reports/requirement_gap_analysis.md`
   - The Orchestrator triggers `design_auditor` → `reports/design_audit.md`
   - The Orchestrator triggers `edge_case_discovery` → `reports/edge_case_report.md`
   - The Orchestrator triggers `testcase_generator` → `reports/testcases.md`
   - The Orchestrator triggers `coverage_analyst` → `reports/coverage_report.md`
4. **Finalization**:
   - The Orchestrator reads all 4 reports and synthesizes `reports/executive_summary.md`.

---

## Core Principles

1. **No Hallucination**: Agents are strictly forbidden from inventing requirements.
2. **Evidence-Based**: Every finding (except 'Missing' features) must cite direct quotes from the input documents.
3. **Deterministic Output**: Reports always follow predefined templates.
