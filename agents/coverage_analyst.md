# 📊 Coverage Analyzer Skill (Production Version)

---

## 🧩 Skill Metadata
- **name:** coverage_analyst
- **version:** 2.0.0
- **description:** Map test cases against SRS requirements to measure coverage, detect gaps, and recommend missing tests.
- **category:** QA / Test Analysis / Coverage Engineering
- **author:** System

---

## 🎯 Purpose
Analyze SRS and generated test cases to:
- Measure requirement coverage
- Detect untested or partially tested requirements
- Identify missing negative / edge / boundary test cases
- Produce structured coverage report with recommendations

---

## 📥 Inputs

### Required Inputs
- `docs/SRS.md` → Source Requirement Specification
- `reports/testcases.md` → Generated test cases

### Optional Inputs
- Requirement ID convention (REQ-xx)
- Test case format schema

---

## 📤 Output

Generate:
📄 `reports/coverage_report.md`

---

## ⚙️ Core Processing Rules

### 1. Requirement Extraction Engine
Extract and normalize requirements from SRS:

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

### 3. Coverage Mapping Rules

Each requirement must be evaluated across 3 dimensions:

#### ✔ Positive Coverage
- At least 1 valid success scenario exists

#### ❌ Negative Coverage
- At least 1 invalid / failure scenario exists

#### ⚠ Edge Coverage
- Boundary conditions covered (min/max, limits, extremes)

---

### 4. Coverage Classification Logic

| Status | Condition |
|--------|----------|
| ✅ FULL | Positive + Negative + Edge exist |
| ⚠ PARTIAL | Only Positive OR missing one dimension |
| ❌ NONE | No test cases mapped |

---

### 5. Gap Detection Rules

Detect and report:

- ❌ Requirements with ZERO test cases
- ⚠ Requirements missing Negative or Edge coverage
- ⚠ Overloaded test cases (too many duplicates)
- ⚠ Unmapped test cases (no requirement link)

---

## 🔁 Failure Handling Rules

### If SRS is missing or unreadable:
- Return error section in report
- Stop requirement extraction phase

### If testcases file is missing:
- Generate report with requirements only
- Mark all as ❌ UNTESTED

### If requirement cannot be parsed:
- Mark as `REQ-UNKNOWN`
- Include in “Data Quality Issues”

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
- Overall Coverage: XX%
- Average Risk Score: XX/100

---

## 2. 📊 Coverage Matrix

| Req ID | Requirement | Test Cases | Positive | Negative | Edge | Score | Status |
|--------|------------|------------|----------|----------|------|-------|--------|
| REQ-01 | Login | TC-01, TC-02 | ✔ | ✔ | ✔ | 100 | ✅ FULL |
| REQ-02 | Reset Password | TC-03 | ✔ | ❌ | ❌ | 40 | ⚠ PARTIAL |
| REQ-03 | Upload Image | None | ❌ | ❌ | ❌ | 0 | ❌ NONE |

---

## 3. 🚨 Coverage Gaps Report

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

## 4. 🧾 Data Quality Report

- Unmapped Test Cases: TC-09, TC-12
- Duplicate Test Cases: TC-05, TC-06
- Missing Requirement IDs: 2 cases

---

## 5. 📈 Final Summary Insight

- Risk Areas: High / Medium / Low
- Most untested module: XXX
- Recommendation priority: High-risk requirements first

---