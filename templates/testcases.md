# 📋 Test Cases Output Template

---

## Purpose

This template defines the standard output structure for generated manual test cases.

The generated test suite shall be:

- Executable
- Traceable
- Excel-ready
- Peer-review ready
- Automation planning ready

This template defines **output format only**. All generation logic and validation rules are governed by `rules/test_generation_rules.md`.

---

# Output Rules

- Generate ONE test case per row.
- Follow the exact column order.
- Do not add, remove, or reorder columns.
- Use HTML `<br>` tags for multiple test steps.
- Every test case must reference exactly one primary Functional Requirement (FR ID).
- Leave Remarks empty unless required by generation rules.

---

# Test Case Table

| Test Case ID | Module | Function | FR ID | Test Case Description | Pre-Requisite | Steps Description | Test Data | Expected Result | Priority | Type | Automation Candidate |
|---------------|--------|----------|-------|-----------------------|---------------|-------------------|-----------|-----------------|----------|------|----------------------|
| SIG-WELCOME-001 | Splash & Welcome | Splash Screen | FR-SIG-1.1 | Verify branded splash screen is displayed when the application launches. | Application is installed.<br>User has not launched the application. | Step 1: Launch the application.<br>Step 2: Observe the splash screen. | Device: Android 15 | The Rider logo and tagline are displayed immediately after the application launches. | High | Functional | Yes |

---

# Column Definitions

| Column | Description |
|----------|-------------|
| **Test Case ID** | Unique identifier following the convention: MODULE-FUNCTION-### |
| **Module** | High-level business module under test. |
| **Function** | Specific feature or function being validated. |
| **FR ID** | Functional Requirement identifier mapped to the test case. |
| **Test Case Description** | Clear business scenario being validated. |
| **Pre-Requisite** | Required system state before executing the test. |
| **Steps Description** | Step-by-step execution instructions. One action per step using HTML `<br>` line breaks. |
| **Test Data** | Specific input values used during execution. |
| **Expected Result** | Observable and measurable application behavior after execution. |
| **Priority** | High / Medium / Low |
| **Type** | Functional / Negative / Edge / UI / Regression / Security / Performance |
| **Automation Candidate** | Yes / No |

---

# Formatting Standards

## Test Case ID

Format

```
MODULE-FUNCTION-###
```

Examples

```
SIG-WELCOME-001

AUTH-LOGIN-001

PROFILE-UPDATE-005

BOOKING-CANCEL-012
```

Test Case IDs shall be unique.

---

## Steps Description

Rules

- One action per step.
- Every step begins with **Step X:**
- Multiple steps use HTML `<br>`.

Example

```
Step 1: Launch the application.<br>
Step 2: Wait until the Splash screen is displayed.<br>
Step 3: Verify the Rider logo is visible.
```

---

## Test Data

Always use realistic data.

Examples

```
Email:
test.user@example.com

Password:
Test@12345

Phone:
0912345678

Coupon:
WELCOME10

Vehicle:
Toyota Camry
```

Avoid

```
Valid Email

Correct Password

Sample Data

ABC

123
```

---

## Expected Result

Expected Result SHALL describe observable system behavior.

### Good Examples

```
Splash screen is displayed immediately after application launch.

Welcome screen is displayed after the configured splash duration.

The "Get Started" button is enabled.

Error message "Invalid Email Address" is displayed below the Email field.

API returns HTTP 401 Unauthorized.

Session token is removed from local storage.
```

### Bad Examples

```
Works correctly.

Success.

Pass.

Expected behavior.

No issue.
```

---

# Priority

Allowed values

```
High

Medium

Low
```

---

# Test Type

Allowed values

```
Functional

Negative

Edge

UI

Regression

Security

Performance
```

---

# Automation Candidate

Allowed values

```
Yes

No
```

Automation suitability shall follow the rules defined in:

```
rules/test_generation_rules.md
```

---

# Example Output

| Test Case ID | Module | Function | FR ID | Test Case Description | Pre-Requisite | Steps Description | Test Data | Expected Result | Priority | Type | Automation Candidate |
|---------------|--------|----------|-------|-----------------------|---------------|-------------------|-----------|-----------------|----------|------|----------------------|
| SIG-WELCOME-001 | Splash & Welcome | Splash Screen | FR-SIG-1.1 | Verify branded splash screen is displayed when launching the application. | Application is installed.<br>User is on the device home screen. | Step 1: Launch the application.<br>Step 2: Observe the splash screen. | Device: Android 15 | The Rider logo and tagline are displayed immediately after application launch. | High | Functional | Yes |
| SIG-WELCOME-002 | Splash & Welcome | Welcome Screen | FR-SIG-1.2 | Verify the splash screen automatically transitions to the Welcome screen after the configured duration. | Splash screen is displayed. | Step 1: Wait until the configured splash duration expires. | Splash Duration: 3 seconds | The Welcome screen is displayed automatically without user interaction. | High | Functional | Yes |
| SIG-WELCOME-003 | Splash & Welcome | Welcome Screen | FR-SIG-1.4 | Verify tapping the "Get Started" button navigates to the Sign In screen. | Welcome screen is displayed. | Step 1: Tap the "Get Started" button. | N/A | The Sign In screen is displayed. | High | Functional | Yes |

---

# End of Template