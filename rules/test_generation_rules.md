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

Example

Requirement:

```
User can login using email and password.
```

Atomic Behaviors:

- Enter email
- Validate email format
- Enter password
- Validate password
- Authenticate user
- Navigate after login
- Handle authentication failure

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

Example

- User account already exists.
- User has network connectivity.
- User is using a supported application version.

Assumptions shall NOT become requirements.

---

## 1.4 Dependency Identification

Identify all dependencies.

Examples

- Authentication Service
- User Profile Service
- Notification Service
- Backend API
- Device Permission
- GPS
- Camera
- Internet Connection

Dependencies influence negative and integration test generation.

---

## 1.5 High Risk Analysis

Identify business risks.

Examples

- Incorrect navigation
- Data corruption
- Security exposure
- Session inconsistency
- Payment interruption
- Duplicate transactions

Higher business risk increases testing priority.

---

## 1.6 Regression Impact Analysis

Identify impacted modules.

Examples

Current Module

↓

Authentication

Potential Regression

- Login
- Registration
- Forgot Password
- Session Management
- Home Page Navigation

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

Whenever numeric or length limits exist, generate:

- Minimum
- Maximum
- Just below minimum
- Just above minimum

Examples

Password length

8

Generate

7

8

9

Maximum

50

Generate

49

50

51

---

## 2.4 Equivalence Partitioning (EP)

Group equivalent input ranges.

Generate one representative test for each partition.

Example

Age

Invalid

<18

Valid

18–65

Invalid

>65

Do NOT generate redundant cases within the same partition.

---

## 2.5 State Transition Testing

Generate cases covering:

Valid transition

Invalid transition

Repeated transition

Interrupted transition

Recovery transition

Example

Order

Pending

↓

Paid

↓

Shipped

↓

Delivered

Attempting

Cancel Delivered Order

shall become Negative testcase.

---

## 2.6 Decision Table Testing

Apply when multiple business conditions determine one outcome.

Example

Premium User

YES

Coupon Valid

YES

Payment Success

YES

↓

Discount Applied

Generate all meaningful decision combinations.

---

## 2.7 Role-Based Testing

Generate test cases for every applicable role.

Examples

Guest

Registered User

Admin

Operator

Driver

Passenger

Role isolation shall always be validated.

---

## 2.8 Error Guessing

Generate scenarios based on common production defects.

Examples

Double click

Rapid tapping

Network interruption

Timeout

Expired token

Duplicate submission

Browser refresh

App resume

Application killed

---

## 2.9 Error Handling

Validate system behavior when unexpected failures occur.

Examples

500 Internal Server Error

404 Resource Missing

Network disconnected

Service unavailable

Gateway timeout

Application restart

Unexpected exception

---

## 2.10 Security Testing

Generate security-oriented test cases where applicable.

Examples

Unauthorized access

Direct URL access

Session hijacking

Invalid token

Token expiration

Role escalation

Input injection

Sensitive data exposure

Authentication bypass

---

## 2.11 Performance Testing

Generate lightweight performance validation cases.

Examples

Splash loading time

Screen transition time

Button responsiveness

Repeated navigation

API response time

Resource loading

Cold launch

Warm launch

---

## 2.12 UI / UX Validation

Validate:

Alignment

Consistency

Visibility

Accessibility

Typography

Button state

Image rendering

Theme

Dark Mode

Landscape Mode

Responsive behavior

---

## 2.13 Regression Testing

Generate regression cases whenever changes affect:

Navigation

Authentication

Permission

Business Rule

Shared Component

Common Service

Regression cases shall focus on previously working functionality.

---

# 3. Requirement Coverage Rules

## Objective

Every functional requirement shall have complete and independent test coverage.

No requirement shall remain partially tested.

---

## 3.1 Minimum Coverage Requirement

Each Requirement ID (REQ / FR / BR) SHALL include:

- At least one Functional testcase
- At least one Negative OR Edge testcase
- At least one Regression testcase (if applicable)

Coverage is considered incomplete if any category is missing.

---

## 3.2 Requirement Traceability

Every testcase MUST map to at least one Requirement ID.

Example

Requirement

FR-SIG-1.2

↓

TC-001
TC-002
TC-003

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
- Record the issue as:

INSUFFICIENT REQUIREMENT

and recommend clarification.

---

# 4. Coverage Distribution Rules

## Objective

Maintain balanced testing across different testing perspectives.

Do not allow Functional Testing to dominate the entire suite.

---

## Required Distribution

Functional

>=40%

Negative

>=15%

Edge

>=10%

UI / UX

>=10%

Performance

>=10%

Regression

>=10%

Security

>=5%

---

## Validation Rule

Before output:

Calculate percentage for every category.

If any category is below required threshold:

Generate additional testcase(s).

Recalculate.

Repeat until all thresholds are satisfied.

---

## Feature Size Rules

Small Feature

15–25 Testcases

Medium Feature

Minimum 40 Testcases

Large Feature

60–120 Testcases

Enterprise Feature

Generate until complete coverage is achieved.

Never stop simply because the minimum count has been reached.

Coverage completeness has higher priority than testcase count.

---

# 5. Test Priority Rules

Priority reflects business importance rather than implementation complexity.

---

## High Priority

Assign HIGH when failure would impact:

Core business flow

Authentication

Payment

Booking

Navigation

Security

Data integrity

Session

Critical user journey

---

## Medium Priority

Assign MEDIUM when failure impacts:

Secondary business functions

Reporting

Filtering

Sorting

Search

Notification

Profile

Settings

---

## Low Priority

Assign LOW when failure impacts:

UI cosmetics

Animations

Branding

Visual consistency

Optional interactions

Non-critical usability improvements

---

## Priority Consistency Rule

Testcases verifying the same business function shall generally have consistent priority.

Avoid arbitrary priority assignment.

---

# 6. Severity Rules

Severity reflects impact of failure.

---

## Critical

Failure causes:

Application crash

Data loss

Security breach

Financial loss

Complete business interruption

System unavailable

---

## Major

Failure causes:

Primary feature unusable

Incorrect business logic

Navigation blocked

Validation failure

Incorrect workflow

---

## Minor

Failure causes:

Cosmetic issue

Alignment

Text formatting

Visual inconsistency

Minor usability inconvenience

---

Severity shall NOT be determined by testcase complexity.

---

# 7. Automation Governance Rules

Automation readiness shall be evaluated during testcase generation.

---

## Automation Candidate

Mark YES when testcase is:

Stable

Repeatable

Deterministic

Environment independent

High execution frequency

Suitable for regression

---

## Manual Candidate

Mark NO when testcase requires:

Visual judgement

Human perception

Exploratory thinking

Complex hardware interaction

Random behaviour

Subjective usability review

---

## Automation Ratio

High Priority Testcases

At least

80%

shall be

Automation Candidate = YES

---

## Validation

Before output:

Calculate:

Automation Coverage %

If

Automation %

<80%

Generate or adjust testcase classification until requirement is met.

---

# 8. Duplicate Prevention Rules

Duplicate testcases are prohibited.

---

## Duplicate Definition

Two testcases are duplicates when they validate:

Same requirement

Same business behaviour

Same expected outcome

using only different wording or data.

---

## Merge Rule

Merge duplicate scenarios into a single optimized testcase.

Never generate duplicate navigation validation.

Never generate duplicate transition validation.

Never generate duplicate UI rendering validation.

Never generate duplicate state validation.

---

## Self Audit

Before output:

Compare every testcase against every other testcase.

Remove duplicates.

Regenerate unique scenarios if necessary.

---

# 9. Test Case Atomicity Rules

Each testcase shall validate ONE business objective.

---

## Allowed

Login with valid account

Password length validation

Forgot password navigation

---

## Not Allowed

Login

+

Logout

+

Remember Me

+

Session timeout

in one testcase.

---

## Action Rule

Each Step shall perform one action.

Each Expected Result shall validate one outcome.

Avoid compound validations.

---

# 10. Test Data Rules

Test data shall be realistic and executable.

---

## Good Examples

Email

test.user@example.com

Password

Test@12345

Phone

0912345678

Vehicle

Toyota Camry

Coupon

WELCOME10

---

## Invalid Examples

Valid Email

Correct Password

Sample User

Random Data

Test

ABC

---

## Boundary Data

Whenever limits exist:

Generate:

Minimum

Maximum

Below Minimum

Above Maximum

Invalid Format

Null

Whitespace

Special Character

Unicode

Duplicate

Expired

---

# 11. Expected Result Standards

Expected Result shall always describe observable system behaviour.

---

## Acceptable

User is redirected to the Sign In screen.

Error message

"Invalid Email Address"

is displayed below the Email field.

Login button becomes disabled.

Splash screen disappears after configured timeout.

Session token is invalidated.

Database record is created.

API returns HTTP 401.

---

## Unacceptable

Works correctly

Displays properly

Successful

Pass

Correct behaviour

As expected

No issue

---

Expected Result shall be:

Observable

Measurable

Verifiable

Deterministic

Unambiguous
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

- TC_ID
- Module
- Feature
- Test Scenario
- Preconditions
- Test Steps
- Test Data
- Expected Result
- Priority
- Severity
- Test Type
- Requirement Reference
- Automation Candidate
- Remarks

---

## TC_ID Convention

Format

[MODULE]-[FEATURE]-[NUMBER]

Examples

SIG-WELCOME-001

AUTH-LOGIN-015

PROFILE-UPDATE-008

Numbers shall be sequential.

Never reuse an existing TC_ID.

---

## Test Step Rules

Each step SHALL contain exactly ONE user action.

Good

Step 1:
Launch application

Step 2:
Tap "Get Started"

Step 3:
Enter email address

Bad

Launch app and login.

---

## Step Writing Standard

Every step shall start with an action verb.

Examples

Launch

Navigate

Tap

Click

Select

Enter

Verify

Open

Close

Refresh

Swipe

Choose

---

## HTML Line Break Rule

When output is intended for Excel,

multiple steps inside one cell SHALL use

<br>

instead of semicolons.

Example

Step 1: Launch App<br>
Step 2: Tap Get Started<br>
Step 3: Verify Sign In screen

---

## Remarks Rules

Only use Remarks when necessary.

Allowed values

ASSUMPTION_BASED

KNOWN_LIMITATION

OUT_OF_SCOPE

DEPENDENCY_REQUIRED

Otherwise leave empty.

---

# 13. Review Governance Rules

Before output, perform an internal QA review.

The generated suite shall satisfy all quality standards.

---

## Review Criteria

Verify:

Business correctness

Requirement coverage

Requirement traceability

Test data quality

Expected Result quality

Automation suitability

Coverage distribution

Priority consistency

Severity consistency

Duplicate detection

Atomicity

Output format

---

## Review Principle

Never skip review.

Never output raw draft testcases.

Only reviewed testcases may be returned.

---

# 14. Pre-Output Validation Checklist

The generator MUST validate the complete suite before producing output.

---

## Coverage Validation

✓ Every requirement has testcases.

✓ Every requirement has Functional coverage.

✓ Every requirement has Negative or Edge coverage.

✓ Regression coverage exists where applicable.

---

## Distribution Validation

✓ Functional >= 40%

✓ Negative >= 15%

✓ Edge >= 10%

✓ UI >= 10%

✓ Performance >= 10%

✓ Security >= 5%

✓ Regression >= 10%

---

## Automation Validation

✓ High Priority Automation Ratio >= 80%

---

## Duplicate Validation

✓ No duplicate scenarios

✓ No duplicate navigation validation

✓ No duplicate state validation

✓ No duplicated Expected Result

---

## Quality Validation

✓ Testcases are atomic

✓ Test data is realistic

✓ Expected Result is measurable

✓ No vague wording

✓ Traceability complete

---

## Output Validation

✓ Correct column order

✓ TC_ID unique

✓ Markdown table valid

✓ Steps formatted correctly

✓ Remarks valid

---

# 15. Self Audit Engine

Before returning the final output, perform a complete self-audit.

---

## Audit Sequence

Step 1

Requirement Coverage Audit

↓

Step 2

Coverage Distribution Audit

↓

Step 3

Duplicate Detection Audit

↓

Step 4

Priority Audit

↓

Step 5

Severity Audit

↓

Step 6

Automation Audit

↓

Step 7

Expected Result Audit

↓

Step 8

Output Format Audit

↓

Step 9

Final Approval

---

## Failure Handling

If ANY audit fails:

DO NOT produce output.

Automatically:

Identify failed area

↓

Regenerate affected testcase(s)

↓

Recalculate statistics

↓

Repeat validation

↓

Only return output after ALL audits pass.

**CRITICAL RULE**: When executing the Self-Audit loop, you MUST output your internal audit reasoning inside an `<audit_trace> ... </audit_trace>` XML block before printing the final Markdown table. This ensures the loop resolves correctly.

---

# 16. Quality Gates

The following Quality Gates are mandatory.

---

## Gate 1

Requirement Understanding

PASS required

---

## Gate 2

Requirement Traceability

PASS required

---

## Gate 3

Coverage Distribution

PASS required

---

## Gate 4

Duplicate Detection

PASS required

---

## Gate 5

Expected Result Quality

PASS required

---

## Gate 6

Automation Governance

PASS required

---

## Gate 7

Output Format

PASS required

---

If any Quality Gate fails,

generation SHALL restart from the affected stage.

---

# 17. AI Regeneration Rules

The generator SHALL automatically regenerate output when:

Coverage is incomplete.

Duplicate testcases are detected.

Automation ratio is below target.

Requirement mapping is missing.

Expected Result is ambiguous.

Test data is unrealistic.

Output format is invalid.

Regression coverage is missing.

The regenerated output shall replace the previous version.

---

# 18. Execution Principles

The generator SHALL:

Think before generating.

Generate before validating.

Validate before reviewing.

Review before approving.

Approve before output.

---

Generation order SHALL be:

Requirement Analysis

↓

Requirement Decomposition

↓

Test Design

↓

Test Case Generation

↓

Requirement Traceability

↓

Coverage Validation

↓

Quality Validation

↓

Self Audit

↓

Final Approval

↓

Output

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

# End of Test Generation Rules