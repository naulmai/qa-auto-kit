# 📊 Coverage Analyzer Skill (Production Version)

---

## 🧩 Skill Metadata
- **name:** coverage_analyst
- **version:** 3.0.0
- **description:** Map test cases against requirements, scenarios, edge cases, and risk items to measure multi-dimensional coverage, detect gaps, and recommend missing tests.
- **category:** QA / Test Analysis / Coverage Engineering
- **author:** System

---

## 🎯 Purpose
Analyze requirements and all generated QA artifacts to:
- Measure requirement coverage across multiple dimensions
- Detect untested or partially tested requirements
- Identify missing negative / edge / boundary test cases
- Validate scenario-to-testcase conversion completeness
- Verify edge case and risk coverage
- Produce structured coverage report with recommendations

---

## 📥 Inputs

### Required Inputs
- `docs/requirements/*` → Requirement documents (SRS, PRD, BRD)
- `reports/*_Testcases.md` (dynamic naming)

### Optional Inputs (Multi-Dimensional Coverage)
- `reports/*_Test_Scenarios_Report.md` (dynamic naming)
- `reports/*_Edge_Case_Report.md` (dynamic naming)
- `reports/*_Risk_Analysis_Report.md` (dynamic naming)
- `reports/*_Req_Gap_Report.md` → For Gap findings coverage

---

## 📤 Output

Generate:
📄 `reports/[Requirement_Name]_Coverage_Report.md`

Use template:
📄 `templates/coverage_report.md`

---

## ⚙️ Core Processing Rules

### 1. Requirement Extraction Engine
Extract and normalize requirements from documents:

- Functional Requirements (FR)
- Business Rules (BR)
- Validation / Constraints

#### Normalization Rules:
- Assign ID format: `REQ-XX`
- One atomic requirement per ID
- Split compound requirements into sub-requirements if needed

---

### 2. Test Case Parsing Engine
Parse test cases from `testcases.md`:

- Extract:
  - Test Case ID (TC-XXX)
  - Linked requirement (if exists)
  - Test type (Positive / Negative / Edge)

#### If no mapping exists:
- Attempt keyword-based mapping
- If still no match → mark as `UNMAPPED`

---

### 3. Requirement → Test Case Coverage (Primary)

Each requirement must be evaluated across 3 dimensions:

#### ✔ Positive Coverage
- At least 1 valid success scenario exists

#### ❌ Negative Coverage
- At least 1 invalid / failure scenario exists

#### ⚠ Edge Coverage
- Boundary conditions covered (min/max, limits, extremes)

---

### 4. Scenario → Test Case Coverage

*Executes only if `reports/test_scenarios.md` is available.*

For each scenario in the scenarios report:
- Check if at least one test case covers this scenario.
- Mark uncovered scenarios as `SCENARIO_GAP`.
- Calculate: `Scenario Coverage % = (Covered Scenarios / Total Scenarios) × 100`

---

### 5. Edge Case → Test Case Coverage

*Executes only if `reports/edge_case_report.md` is available.*

For each edge case finding:
- Check if at least one test case or scenario covers this edge case.
- Mark uncovered edge cases as `EDGE_CASE_GAP`.
- Calculate: `Edge Case Coverage % = (Covered Edge Cases / Total Edge Cases) × 100`

---

### 6. Risk Item → Test Case Coverage

*Executes only if `reports/risk_analysis.md` is available.*

For each identified risk:
- Check if at least one test case validates the risk mitigation.
- Prioritize: Critical and High risks with no test coverage are flagged as `CRITICAL_RISK_GAP`.
- Calculate: `Risk Coverage % = (Covered Risks / Total Risks) × 100`

---

### 7. Coverage Classification Logic

| Status | Condition |
|--------|----------|
| ✅ FULL | Positive + Negative + Edge exist |
| ⚠ PARTIAL | Only Positive OR missing one dimension |
| ❌ NONE | No test cases mapped |

---

### 8. Gap Detection Rules

Detect and report:

- ❌ Requirements with ZERO test cases
- ⚠ Requirements missing Negative or Edge coverage
- ⚠ Scenarios not converted to test cases
- ⚠ Edge cases without test coverage
- ⚠ Critical/High risks without test coverage
- ⚠ Overloaded test cases (too many duplicates)
- ⚠ Unmapped test cases (no requirement link)

---

## 🔁 Failure Handling Rules

### If requirement documents are missing or unreadable:
- Return error section in report
- Stop requirement extraction phase

### If testcases file is missing:
- Generate report with requirements only
- Mark all as ❌ UNTESTED

### If optional reports are unavailable:
- Skip corresponding coverage dimension
- Note in report: "[Dimension] coverage not evaluated — input report unavailable."

### If requirement cannot be parsed:
- Mark as `REQ-UNKNOWN`
- Include in "Data Quality Issues"

---

## 📊 Coverage Scoring System

Each requirement gets a score:

- Positive coverage = +40
- Negative coverage = +30
- Edge coverage = +30

### Score Interpretation:
- 100 → Fully Covered
- 60–99 → Partial Coverage
- <60 → High Risk
- 0 → Not Tested

---

## 📄 Output Format

---

## 1. 📌 Executive Summary

- Total Requirements: X
- Fully Covered: Y
- Partially Covered: Z
- Not Covered: W
- Unmapped Test Cases: U
- Overall Requirement Coverage: XX%
- Scenario Coverage: XX% (if available)
- Edge Case Coverage: XX% (if available)
- Risk Coverage: XX% (if available)
- Average Risk Score: XX/100

---

## 2. 📊 Requirement Coverage Matrix

| Req ID | Requirement | Test Cases | Positive | Negative | Edge | Score | Status |
|--------|------------|------------|----------|----------|------|-------|--------|
| REQ-01 | Login | TC-01, TC-02 | ✔ | ✔ | ✔ | 100 | ✅ FULL |
| REQ-02 | Reset Password | TC-03 | ✔ | ❌ | ❌ | 40 | ⚠ PARTIAL |
| REQ-03 | Upload Image | None | ❌ | ❌ | ❌ | 0 | ❌ NONE |

---

## 3. 📊 Scenario Coverage Matrix

*(Only if `reports/test_scenarios.md` is available)*

| Scenario ID | Scenario Name | Covered by Test Case | Status |
|-------------|---------------|----------------------|--------|
| SCN-001 | Login valid | TC-01 | ✅ Covered |
| SCN-005 | Session timeout | None | ❌ GAP |

---

## 4. 📊 Edge Case Coverage Matrix

*(Only if `reports/edge_case_report.md` is available)*

| Edge Case ID | Description | Covered by Test Case | Status |
|--------------|-------------|----------------------|--------|
| EDGE-001 | Double payment | TC-15 | ✅ Covered |
| EDGE-003 | Network recovery | None | ❌ GAP |

---

## 5. 📊 Risk Coverage Matrix

*(Only if `reports/risk_analysis.md` is available)*

| Risk ID | Risk Description | Level | Covered by Test Case | Status |
|---------|------------------|-------|----------------------|--------|
| RISK-001 | Brute-force attack | Critical | TC-20 | ✅ Covered |
| RISK-004 | Duplicate payment | Critical | None | 🔴 CRITICAL GAP |

---

## 6. 🚨 Coverage Gaps Report

For each issue, include:

### ❌ Gap Type: Missing Coverage

**Requirement:** REQ-03 Upload Image

**Issue:** No test cases found

**Recommended Test Cases:**
- Valid image upload (JPG/PNG)
- File size exceeds limit (Negative)
- Invalid format upload (PDF/EXE) (Negative)
- Corrupted file upload (Edge)

---

### ⚠ Gap Type: Partial Coverage

**Requirement:** REQ-02 Reset Password

**Issue:** Missing Negative & Edge coverage

**Missing Test Cases:**
- Email not found
- Invalid email format
- OTP expired
- OTP retry limit exceeded

---

## 7. 🧾 Data Quality Report

- Unmapped Test Cases: TC-09, TC-12
- Duplicate Test Cases: TC-05, TC-06
- Missing Requirement IDs: 2 cases

---

## 8. 📈 Final Summary Insight

- Risk Areas: High / Medium / Low
- Most untested module: XXX
- Recommendation priority: High-risk requirements first

---