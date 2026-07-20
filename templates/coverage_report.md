# 📊 Test Coverage & Traceability Matrix

---

## 📄 Document Metadata
| Property | Details |
|----------|---------|
| **Date Generated** | [YYYY-MM-DD] |
| **Target Requirements** | [e.g., Requirement_Name.md] |
| **Test Suite** | [e.g., testcases.md] |
| **Overall Coverage**| **[XX]%** |

---

## 📈 1. Coverage Statistics

| Coverage Dimension | Score / Percentage | Status |
|--------------------|--------------------|--------|
| **Positive Path Coverage** | [XX]% | [✅ / ⚠️ / ❌] |
| **Negative Path Coverage** | [XX]% | [✅ / ⚠️ / ❌] |
| **Edge/Boundary Coverage** | [XX]% | [✅ / ⚠️ / ❌] |
| **Automation Candidate Ratio** | [XX]% | [✅ / ⚠️ / ❌] |
| **UAT Script Coverage** | [Count] cases | [✅ / ⚠️ / ❌] |
| **Test Type Distribution** | Functional: [X]% <br> Negative: [X]% <br> Edge: [X]% | - |
| **Fully Covered Requirements** | [Y] / [Total] | - |
| **Untested Requirements** | [Z] / [Total] | - |
| **Scenario Coverage** | [XX]% | [✅ / ⚠️ / ❌] |
| **Edge Case Coverage** | [XX]% | [✅ / ⚠️ / ❌] |
| **Risk Coverage** | [XX]% | [✅ / ⚠️ / ❌] |

---

## 🧮 2. Requirement Coverage Matrix

| FR ID | Requirement Summary | Positive TC | Negative TC | Edge TC | Score | Status |
|-------|---------------------|-------------|-------------|---------|-------|--------|
| REQ-01| User Login | TC-01, TC-02| TC-03, TC-04| TC-05 | 100 | ✅ FULL |
| REQ-02| Reset Password | TC-06 | None | None | 40 | ⚠️ PARTIAL|
| REQ-03| Upload Avatar | None | None | None | 0 | ❌ NONE |

---

## 📊 3. Scenario Coverage Matrix

*(Only if `reports/*_Test_Scenarios_Report.md` is available)*

| Scenario ID | Scenario Name | Covered by Test Case | Status |
|-------------|---------------|----------------------|--------|
| SCN-001 | [Scenario Name] | [TC-XXX] | ✅ Covered |
| SCN-005 | [Scenario Name] | None | ❌ GAP |

> If no Test Scenarios Report exists, write: "N/A — Scenario Generator was not executed in this workflow run."

---

## 🧨 4. Edge Case Coverage Matrix

*(Only if `reports/*_Edge_Case_Report.md` is available)*

| Edge Case ID | Description | Covered by Test Case | Status |
|--------------|-------------|----------------------|--------|
| EDGE-001 | [Description] | [TC-XXX] | ✅ Covered |
| EDGE-003 | [Description] | None | ❌ GAP |

> If no Edge Case Report exists, write: "N/A — Edge Case Analyzer was not executed in this workflow run."

---

## 🛡️ 5. Risk Coverage Matrix

*(Only if `reports/*_Risk_Analysis_Report.md` is available)*

| Risk ID | Risk Description | Level | Covered by Test Case | Status |
|---------|------------------|-------|----------------------|--------|
| RISK-001 | [Description] | Critical | [TC-XXX] | ✅ Covered |
| RISK-004 | [Description] | Critical | None | 🔴 CRITICAL GAP |

> If no Risk Analysis Report exists, write: "N/A — Risk Analyst was not executed in this workflow run."

---

## 🚨 6. Coverage Gaps Report

*(For each Requirement marked as ⚠️ PARTIAL or ❌ NONE)*

### 📌 [REQ-XXX]: [Requirement Summary]
- **Current Status**: [Partial / None]
- **Missing Coverage**: [e.g., Missing Negative tests for invalid file formats]
- **Recommended Actions**: 
  - [Suggest specific test case 1]
  - [Suggest specific test case 2]

---

## 🧾 7. Data Quality Report

- **Unmapped Test Cases**: [TC-XXX, TC-YYY — test cases with no requirement link]
- **Duplicate Test Cases**: [TC-XXX, TC-YYY — test cases covering the same objective]
- **Missing Requirement IDs**: [Count] cases with blank or invalid FR ID

---

## 📈 8. Final Summary Insight

- **Most Untested Module**: [Module Name]
- **Highest Risk Area**: [High / Medium / Low]
- **Recommendation Priority**: High-risk requirements first
- **Overall Assessment**: [🟢 Safe to proceed / 🟡 Needs attention / 🔴 High risk — do not release]

---
# End of Report
