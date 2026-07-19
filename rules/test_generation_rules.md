# 🧪 Test Generation Rules (Production Version)

---

## Metadata

- name: test_generation_rules
- version: 3.0.0
- category: QA / Test Design Standards
- description: Enterprise-level governance rules for generating high-quality, executable, traceable, and automation-ready manual test cases.

---

# 1. Requirement Analysis Rules

## Objective

Before generating any test case, the generator MUST fully understand the requirement.

Generating test cases without requirement analysis is prohibited.

---

## 1.1 Requirement Decomposition

Every requirement shall be decomposed into atomic functional behaviors.

**Example:**

| Requirement | Atomic Behaviors |
|-------------|-----------------|
| User can login using email and password | Enter email, Validate email format, Enter password, Validate password, Authenticate user, Navigate after login, Handle authentication failure |

Never generate test cases directly from compound requirements.

---

## 1.2 Functional Component Identification

Identify:

- Primary function
- Supporting functions
- Business validations
- System validations
- Navigation behavior
- State changes

---

## 1.3 Assumption Identification

Explicitly identify assumptions before generating test cases.

**Example:**

- User account already exists.
- User has network connectivity.
- User is using a supported application version.

Assumptions shall NOT become requirements.

---

## 1.4 Dependency Identification

Identify all dependencies.

| Category | Examples |
|----------|----------|
| Services | Authentication Service, User Profile Service, Notification Service, Backend API |
| Device | GPS, Camera, Internet Connection |
| Permissions | Device Permission |

Dependencies influence negative and integration test generation.

---

## 1.5 High Risk Analysis

Identify business risks.

| Risk Type | Examples |
|-----------|----------|
| Navigation | Incorrect navigation |
| Data | Data corruption |
| Security | Security exposure, Session inconsistency |
| Financial | Payment interruption, Duplicate transactions |

Higher business risk increases testing priority.

---

## 1.6 Regression Impact Analysis

Identify impacted modules.

**Example: Authentication Module**

| Current Module | Potential Regression Impact |
|---------------|---------------------------|
| Authentication | Login, Registration, Forgot Password, Session Management, Home Page Navigation |

Regression scope shall be included in generated test cases where applicable.

---

# 2. Test Design Rules

The generator shall internally apply professional QA test design techniques.

These techniques are reasoning mechanisms and MUST NOT be printed unless explicitly requested.

---

## 2.1 Happy Path

Generate the primary successful business flow.

Every requirement shall contain at least one Happy Path testcase.

---

## 2.2 Negative Testing

Generate invalid scenarios including:

- Invalid input
- Missing required field
- Invalid format
- Unauthorized access
- Expired session
- Invalid operation
- API failure
- Permission denied

---

## 2.3 Boundary Value Analysis (BVA)

Whenever numeric or length limits exist, generate test values at boundaries:

| Input | Min | Min-1 | Min+1 | Max-1 | Max | Max+1 |
|-------|-----|-------|-------|-------|-----|-------|
| Password length (8–50) | 8 | 7 | 9 | 49 | 50 | 51 |

---

## 2.4 Equivalence Partitioning (EP)

Group equivalent input ranges. Generate one representative test for each partition.

| Input | Invalid (Below) | Valid | Invalid (Above) |
|-------|-----------------|-------|-----------------|
| Age | <18 | 18–65 | >65 |

Do NOT generate redundant cases within the same partition.

---

## 2.5 State Transition Testing

Generate cases covering:

| Transition Type | Description |
|----------------|-------------|
| Valid | Normal allowed transition |
| Invalid | Attempting disallowed transition |
| Repeated | Performing same transition twice |
| Interrupted | Transition cut off mid-process |
| Recovery | Recovering from failed transition |

**Example:** Order: Pending → Paid → Shipped → Delivered. Attempting "Cancel Delivered Order" shall become a Negative testcase.

---

## 2.6 Decision Table Testing

Apply when multiple business conditions determine one outcome.

| Premium User | Coupon Valid | Payment Success | → Outcome |
|-------------|-------------|-----------------|-----------|
| YES | YES | YES | Discount Applied |
| YES | NO | YES | Full Price |
| NO | YES | YES | Discount Applied |
| NO | NO | NO | Payment Failed |

Generate all meaningful decision combinations.

---

## 2.7 Role-Based Testing

Generate test cases for every applicable role:

- Guest
- Registered User
- Admin
- Operator
- Driver
- Passenger

Role isolation shall always be validated.

---

## 2.8 Error Guessing

Generate scenarios based on common production defects:

- Double click / Rapid tapping
- Network interruption / Timeout
- Expired token
- Duplicate submission
- Browser refresh / App resume
- Application killed

---

## 2.9 Error Handling

Validate system behavior when unexpected failures occur:

- 500 Internal Server Error
- 404 Resource Missing
- Network disconnected
- Service unavailable
- Gateway timeout
- Application restart
- Unexpected exception

---

## 2.10 Security Testing

Generate security-oriented test cases where applicable:

- Unauthorized access / Direct URL access
- Session hijacking / Invalid token / Token expiration
- Role escalation
- Input injection
- Sensitive data exposure
- Authentication bypass

---

## 2.11 Performance Testing

Generate lightweight performance validation cases:

- Splash loading time / Screen transition time
- Button responsiveness
- Repeated navigation
- API response time / Resource loading
- Cold launch / Warm launch

---

## 2.12 UI / UX Validation

Validate:

- Alignment, Consistency, Visibility
- Accessibility, Typography
- Button state, Image rendering
- Theme / Dark Mode
- Landscape Mode / Responsive behavior

---

## 2.13 Regression Testing

Generate regression cases whenever changes affect:

- Navigation / Authentication / Permission
- Business Rule / Shared Component / Common Service

Regression cases shall focus on previously working functionality.

---

# 3. Requirement Coverage Rules (ISTQB & ISO/IEC/IEEE 29119 Aligned)

## Objective

Every functional requirement shall have complete and independent test coverage. No requirement shall remain partially tested.

---

## 3.1 Minimum Coverage Criteria

According to **ISTQB** and **ISO/IEC/IEEE 29119** standards, a test suite is considered to have complete coverage only when it satisfies the following dimensions:

| Coverage Dimension | Objective & Target | Standard Criteria |
|--------------------|---------------------|-------------------|
| **✅ Requirement Coverage** | All requirements/acceptance criteria have corresponding test cases (100% traceability). | Traceability Matrix (Requirement ID ➔ Test Case ID) |
| **✅ Functional Coverage** | All functions and primary/secondary business flows are fully tested. | Happy Path, Alternative Flows |
| **✅ Risk Coverage** | High-risk areas are prioritized, mitigation is verified, and fully tested. | Risk Register ➔ Mitigation validation |
| **✅ Scenario Coverage** | Complete coverage of Happy Path, Alternative Flow, and Exception Flow. | Use Case/Scenario matrix |
| **✅ Input Coverage** | Verification of data inputs: valid, invalid, boundary values, and equivalence classes. | Equivalence Partitioning + BVA |
| **✅ Business Rule Coverage** | Every business rule, constraint, and conditional validation is verified. | Decision Table / Logic mapping |
| **✅ Non-functional Coverage** | Performance, Security, Accessibility, Usability, Compatibility (if inside scope). | Security & Performance checks |
| **✅ Regression Coverage** | A suitable regression test suite exists to protect existing features from side-effects. | Automated Regression Suite |

Coverage is evaluated as incomplete if any required dimension fails to meet its standard criteria.

---

## 3.2 Requirement Traceability

Every testcase MUST map to at least one Requirement ID.

| Requirement | Test Cases |
|-------------|-----------|
| FR-SIG-1.2 | TC-001, TC-002, TC-003 |

Every requirement shall be traceable through generated testcases.

---

## 3.3 Multiple Requirement Rule

A testcase should validate ONE primary requirement.

Avoid mapping multiple unrelated requirements into a single testcase.

Only tightly coupled requirements may be referenced together.

---

## 3.4 Missing Requirement Handling

If a requirement cannot generate any executable testcase due to insufficient information:

- Generate no speculative testcase.
- Record the issue as: **INSUFFICIENT REQUIREMENT**
- Recommend clarification.

---

# 4. Coverage Distribution Rules

## Objective

Maintain balanced testing across different testing perspectives.

Do not allow Functional Testing to dominate the entire suite.

---

## Required Distribution

| Test Type | Minimum Percentage |
|-----------|-------------------|
| Functional | ≥40% |
| Negative | ≥15% |
| Edge | ≥10% |
| UI / UX | ≥10% |
| Performance | ≥10% |
| Regression | ≥10% |
| Security | ≥5% |

---

## Validation Rule

Before output:

1. Calculate percentage for every category.
2. If any category is below required threshold → Generate additional testcase(s).
3. Recalculate.
4. Repeat until all thresholds are satisfied.

---

## Feature Size Rules

| Feature Size | Test Case Count |
|-------------|----------------|
| Small Feature | 15–25 Testcases |
| Medium Feature | Minimum 40 Testcases |
| Large Feature | 60–120 Testcases |
| Enterprise Feature | Generate until complete coverage is achieved |

Never stop simply because the minimum count has been reached.

Coverage completeness has higher priority than testcase count.

---

# 5. Test Priority Rules

Priority reflects business importance rather than implementation complexity.

---

## Priority Assignment

| Priority | Assign When Failure Impacts |
|----------|---------------------------|
| **High** | Core business flow, Authentication, Payment, Booking, Navigation, Security, Data integrity, Session, Critical user journey |
| **Medium** | Secondary business functions, Reporting, Filtering, Sorting, Search, Notification, Profile, Settings |
| **Low** | UI cosmetics, Animations, Branding, Visual consistency, Optional interactions, Non-critical usability improvements |

---

## Priority Consistency Rule

Testcases verifying the same business function shall generally have consistent priority.

Avoid arbitrary priority assignment.

---

# 6. Severity Rules

Severity reflects impact of failure.

---

## Severity Classification

| Severity | Failure Causes |
|----------|---------------|
| **Critical** | Application crash, Data loss, Security breach, Financial loss, Complete business interruption, System unavailable |
| **Major** | Primary feature unusable, Incorrect business logic, Navigation blocked, Validation failure, Incorrect workflow |
| **Minor** | Cosmetic issue, Alignment, Text formatting, Visual inconsistency, Minor usability inconvenience |

Severity shall NOT be determined by testcase complexity.

---

# 7. Automation Governance Rules

Automation readiness shall be evaluated during testcase generation.

---

## Automation Candidate

| Classification | Criteria |
|---------------|----------|
| **YES** (Automate) | Stable, Repeatable, Deterministic, Environment independent, High execution frequency, Suitable for regression |
| **NO** (Manual) | Requires visual judgement, Human perception, Exploratory thinking, Complex hardware interaction, Random behaviour, Subjective usability review |

---

## Automation Ratio

| Test Priority | Minimum Automation Candidate |
|--------------|------------------------------|
| High Priority Testcases | At least 80% shall be Automation Candidate = YES |

---

## Validation

Before output:

1. Calculate Automation Coverage %.
2. If Automation % < 80% → Generate or adjust testcase classification until requirement is met.

---

# 8. Duplicate Prevention Rules

Duplicate testcases are prohibited.

---

## Duplicate Definition

Two testcases are duplicates when they validate:

- Same requirement
- Same business behaviour
- Same expected outcome

using only different wording or data.

---

## Merge Rule

- Merge duplicate scenarios into a single optimized testcase.
- Never generate duplicate navigation validation.
- Never generate duplicate transition validation.
- Never generate duplicate UI rendering validation.
- Never generate duplicate state validation.

---

## Self Audit

Before output:

1. Compare every testcase against every other testcase.
2. Remove duplicates.
3. Regenerate unique scenarios if necessary.

---

# 9. Test Case Atomicity Rules

Each testcase shall validate ONE business objective.

---

## Allowed

| ✅ Atomic Test Cases |
|---------------------|
| Login with valid account |
| Password length validation |
| Forgot password navigation |

---

## Not Allowed

| ❌ Compound Test Cases |
|----------------------|
| Login + Logout + Remember Me + Session timeout in one testcase |

---

## Action Rule

- Each Step shall perform one action.
- Each Expected Result shall validate one outcome.
- Avoid compound validations.

---

# 10. Test Data Rules

Test data shall be realistic and executable.

---

## Good vs Bad Examples

| Field | ✅ Good | ❌ Bad |
|-------|--------|--------|
| Email | test.user@example.com | Valid Email |
| Password | Test@12345 | Correct Password |
| Phone | 0912345678 | Sample User |
| Vehicle | Toyota Camry | Random Data |
| Coupon | WELCOME10 | Test / ABC |

---

## Boundary Data

Whenever limits exist, generate:

- Minimum, Maximum
- Below Minimum, Above Maximum
- Invalid Format, Null, Whitespace
- Special Character, Unicode
- Duplicate, Expired

---

# 11. Expected Result Standards

Expected Result shall always describe observable system behaviour.

---

## Good vs Bad Examples

| ✅ Acceptable | ❌ Unacceptable |
|--------------|----------------|
| User is redirected to the Sign In screen | Works correctly |
| Error message "Invalid Email Address" is displayed below the Email field | Displays properly |
| Login button becomes disabled | Successful |
| Splash screen disappears after configured timeout | Pass |
| Session token is invalidated | Correct behaviour |
| Database record is created | As expected |
| API returns HTTP 401 | No issue |

Expected Result shall be: Observable, Measurable, Verifiable, Deterministic, Unambiguous.

---

# 12. Output Format Rules

## Objective

Generate test cases in a standardized structure suitable for:

- Manual execution
- Excel import
- Test Management Tools
- Automation planning
- Peer review

---

## Output Structure

Each testcase SHALL contain:

| Column | Description |
|--------|-------------|
| TC_ID | Unique identifier: MODULE-FUNCTION-### |
| Module | High-level business module |
| Feature | Specific feature under test |
| Test Scenario | Business scenario description |
| Preconditions | Required system state |
| Test Steps | Step-by-step actions (one per step) |
| Test Data | Specific input values |
| Expected Result | Observable outcome |
| Priority | High / Medium / Low |
| Severity | Critical / Major / Minor |
| Test Type | Functional / Negative / Edge / UI / Regression / Security / Performance |
| Requirement Reference | FR/REQ/BR ID |
| Automation Candidate | Yes / No |
| Remarks | ASSUMPTION_BASED / KNOWN_LIMITATION / OUT_OF_SCOPE / DEPENDENCY_REQUIRED / (empty) |

---

## TC_ID Convention

| Format | Examples |
|--------|----------|
| `[MODULE]-[FEATURE]-[NUMBER]` | SIG-WELCOME-001, AUTH-LOGIN-015, PROFILE-UPDATE-008 |

Numbers shall be sequential. Never reuse an existing TC_ID.

---

## Test Step Rules

Each step SHALL contain exactly ONE user action.

| ✅ Good | ❌ Bad |
|--------|--------|
| Step 1: Launch application | Launch app and login |
| Step 2: Tap "Get Started" | |
| Step 3: Enter email address | |

---

## Step Writing Standard

Every step shall start with an action verb:

Launch, Navigate, Tap, Click, Select, Enter, Verify, Open, Close, Refresh, Swipe, Choose

---

## HTML Line Break Rule

When output is intended for Excel, multiple steps inside one cell SHALL use `<br>` instead of semicolons.

**Example:**
```
Step 1: Launch App<br>Step 2: Tap Get Started<br>Step 3: Verify Sign In screen
```

---

## Remarks Rules

Only use Remarks when necessary.

| Allowed Values |
|----------------|
| ASSUMPTION_BASED |
| KNOWN_LIMITATION |
| OUT_OF_SCOPE |
| DEPENDENCY_REQUIRED |
| (empty) |

---

# 13. Review Governance Rules

Before output, perform an internal QA review.

The generated suite shall satisfy all quality standards.

---

## Review Criteria

Verify:

- Business correctness
- Requirement coverage
- Requirement traceability
- Test data quality
- Expected Result quality
- Automation suitability
- Coverage distribution
- Priority consistency
- Severity consistency
- Duplicate detection
- Atomicity
- Output format

---

## Review Principle

- Never skip review.
- Never output raw draft testcases.
- Only reviewed testcases may be returned.

---

# 14. Pre-Output Validation Checklist

The generator MUST validate the complete suite before producing output.

---

## Coverage Validation

- ✓ Every requirement has testcases
- ✓ Every requirement has Functional coverage
- ✓ Every requirement has Negative or Edge coverage
- ✓ Regression coverage exists where applicable

---

## Distribution Validation

- ✓ Functional ≥ 40%
- ✓ Negative ≥ 15%
- ✓ Edge ≥ 10%
- ✓ UI ≥ 10%
- ✓ Performance ≥ 10%
- ✓ Security ≥ 5%
- ✓ Regression ≥ 10%

---

## Automation Validation

- ✓ High Priority Automation Ratio ≥ 80%

---

## Duplicate Validation

- ✓ No duplicate scenarios
- ✓ No duplicate navigation validation
- ✓ No duplicate state validation
- ✓ No duplicated Expected Result

---

## Quality Validation

- ✓ Testcases are atomic
- ✓ Test data is realistic
- ✓ Expected Result is measurable
- ✓ No vague wording
- ✓ Traceability complete

---

## Output Validation

- ✓ Correct column order
- ✓ TC_ID unique
- ✓ Markdown table valid
- ✓ Steps formatted correctly
- ✓ Remarks valid

---

# 15. Self Audit Engine

Before returning the final output, perform a complete self-audit.

---

## Audit Sequence

| Step | Audit |
|------|-------|
| 1 | Requirement Coverage Audit |
| 2 | Coverage Distribution Audit |
| 3 | Duplicate Detection Audit |
| 4 | Priority Audit |
| 5 | Severity Audit |
| 6 | Automation Audit |
| 7 | Expected Result Audit |
| 8 | Output Format Audit |
| 9 | Final Approval |

---

## Failure Handling

If ANY audit fails:

1. DO NOT produce output.
2. Identify failed area.
3. Regenerate affected testcase(s).
4. Recalculate statistics.
5. Repeat validation.
6. Only return output after ALL audits pass.

**CRITICAL RULE**: When executing the Self-Audit loop, you MUST output your internal audit reasoning inside an `<audit_trace> ... </audit_trace>` XML block before printing the final Markdown table. This ensures the loop resolves correctly.

---

# 16. Quality Gates

The following Quality Gates are mandatory.

| Gate | Check | Requirement |
|------|-------|-------------|
| Gate 1 | Requirement Understanding | PASS required |
| Gate 2 | Requirement Traceability | PASS required |
| Gate 3 | Coverage Distribution | PASS required |
| Gate 4 | Duplicate Detection | PASS required |
| Gate 5 | Expected Result Quality | PASS required |
| Gate 6 | Automation Governance | PASS required |
| Gate 7 | Output Format | PASS required |

If any Quality Gate fails, generation SHALL restart from the affected stage.

---

# 17. AI Regeneration Rules

The generator SHALL automatically regenerate output when:

- Coverage is incomplete.
- Duplicate testcases are detected.
- Automation ratio is below target.
- Requirement mapping is missing.
- Expected Result is ambiguous.
- Test data is unrealistic.
- Output format is invalid.
- Regression coverage is missing.

The regenerated output shall replace the previous version.

---

# 18. Execution Principles

The generator SHALL:

1. Think before generating.
2. Generate before validating.
3. Validate before reviewing.
4. Review before approving.
5. Approve before output.

---

## Generation Order

| Step | Phase |
|------|-------|
| 1 | Requirement Analysis |
| 2 | Requirement Decomposition |
| 3 | Test Design |
| 4 | Test Case Generation |
| 5 | Requirement Traceability |
| 6 | Coverage Validation |
| 7 | Quality Validation |
| 8 | Self Audit |
| 9 | Final Approval |
| 10 | Output |

---

## Mandatory Principles

- Never hallucinate requirements.
- Never invent undocumented functionality.
- Never skip validation.
- Never skip self-audit.
- Never output duplicate testcases.
- Never output partially covered requirements.
- Never use vague wording.
- Always maintain end-to-end traceability.
- Always generate deterministic and review-ready test cases.

---

## Token Limit / Large Suite Handling

If the generated test suite is too large to fit in a single AI response (e.g., > 40 test cases), automatically pause at a safe boundary and output:
**"Part 1 completed. Type CONTINUE to generate the next batch."**
Ensure no test case is cut off in the middle of the table.

---

# 19. CSV & Excel Integration Standards

## Objective
Ensure the generated Markdown table can be cleanly converted to a standard CSV file without column shifting or import errors in spreadsheet software or test case managers (like Jira Xray or TestRail).

## Formatting Rules
- **No unquoted commas inside cells**: If an input cell or expected result contains commas, do not use commas directly if possible. Alternatively, ensure the converter script quotes the fields.
- **Enforce HTML `<br>` for line breaks**: Do not use semicolons `;` or real newlines inside table cells for step separation. Use exact `<br>` tag strings to allow clean conversion.
- **Escape double quotes**: If a test step or text string contains a double quote (`"`), it must be escaped as `""` inside the markdown cell to prevent CSV parsing issues.
- **Strict Column Count Alignment**: The generated table must strictly maintain the 12-column layout. Adding or removing columns on specific rows is prohibited.

---

# End of Test Generation Rules