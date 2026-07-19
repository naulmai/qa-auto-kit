# 📋 Test Cases Output Template

---

## 📄 Document Metadata
| Property | Details |
|----------|---------|
| **Date Generated** | [YYYY-MM-DD] |
| **Target Requirements** | [e.g., Requirement_Name.md] |
| **Test Suite** | [e.g., testcases.md] |
| **Total Test Cases** | [X] |
| **Analyzed By** | Test Case Generator Skill (v3.0.0) |

---

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
- **CSV Stability Warning**: Do not modify column names or insert secondary tables (such as Metadata) inside the main test case table block. Doing so breaks the CSV export parser script.
- Use HTML `<br>` tags for multiple test steps so it renders correctly in Markdown, but ensure the descriptions are as detailed and literal as if they were written for Excel.
- Every test case must reference exactly one primary Functional Requirement (FR ID).
- Leave Remarks empty unless required by generation rules.
- **CRITICAL DETAIL LEVEL**: The test cases must be EXTREMELY specific. Use exact wording for UI elements (e.g., "Top navigation bar titled 'Subscription' with back arrow"), specify exact visual states (e.g., "active blue background state", "light-blue pill badge"), and specify exact dynamic behaviors (e.g., "Prices dynamically recalculate and update across Basic and Premium cards in real-time"). Vague steps or expected results are NOT allowed.

---

# Test Case Table

| Test Case ID | Module | Function | FR ID | Test Case Description | Pre-Requisite | Steps Description | Test Data | Expected Result | Priority | Severity | Type | Automation Candidate | Remarks |
|--------------|--------|----------|-------|-----------------------|---------------|-------------------|-----------|-----------------|----------|----------|------|----------------------|---------|
| SIG-WELCOME-001 | Splash & Welcome | Splash Screen | Verify branded splash screen is displayed when the application launches. | Application is installed.<br>User has not launched the application. | Step 1: Launch the application.<br>Step 2: Observe the splash screen. | Device: Android 15 | The Rider logo and tagline are displayed immediately after the application launches. | High | Minor | Functional | FR-SIG-1.1 | Yes | |

---

# Column Definitions

| Column | Description |
|----------|-------------|
| **Test Case ID** | Unique identifier following the convention: MODULE-FUNCTION-### |
| **Module** | High-level business module under test. |
| **Function** | Specific feature or function being validated. |
| **FR ID** | Functional Requirement identifier mapped to the test case. |
| **Test Case Description** | Clear business scenario being validated. Must be highly descriptive. |
| **Pre-Requisite** | Required system state before executing the test. |
| **Steps Description** | Step-by-step execution instructions. One action per step using HTML `<br>` line breaks. Must mention exact interaction targets. |
| **Test Data** | Specific input values used during execution. |
| **Expected Result** | Observable and measurable application behavior after execution. Must describe exact UI/UX state mutations, copy, and layout changes. |
| **Priority** | High / Medium / Low |
| **Severity** | Critical / Major / Minor |
| **Type** | Functional / Negative / Edge / UI / Regression / Security / Performance |
| **Automation Candidate** | Yes / No |
| **Remarks** | ASSUMPTION_BASED / KNOWN_LIMITATION / OUT_OF_SCOPE / DEPENDENCY_REQUIRED / (empty) |

---

# Formatting Standards

## Test Case ID

Format

```
MODULE-FUNCTION-###
```

Examples

```
SUB-ENT-001

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
- Be extremely explicit about what to click, tap, or inspect.

Example

```
Step 1: Launch the application.<br>
Step 2: Wait until the Splash screen is displayed.<br>
Step 3: Verify the Rider logo is visible.
```

---

## Test Data

Always use realistic data. Specify exact plans, strings, or values.

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

Expected Result SHALL describe observable system behavior, including precise UI details, copy, and transitions.

### Good Examples

```
Navigates to Subscriptions Overview; recommended plan is highlighted & scrolled into view.

Top navigation bar titled "Subscription" with back arrow. Hero shows 3D piggy-bank icon, bold primary headline, and exact subheadline. Status row shows (ⓘ) "You are currently on the Free plan".

Selected toggle renders with an active blue background state; inactive Monthly displays standard neutral grey background state. Annual displays embedded badge "Save 20%".

Prices dynamically recalculate and update across Basic and Premium cards in real-time without executing full screen reloads. Monthly toggle restores base prices.

Displays plan name "Basic Plan", light-blue pill badge "Value" anchored right. Active price format is bold blue "$9.99 /mo". CTA button explicitly reads "View more & Get Basic Now".
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

| Test Case ID | Module | Function | FR ID | Test Case Description | Pre-Requisite | Steps Description | Test Data | Expected Result | Priority | Severity | Type | Automation Candidate | Remarks |
|--------------|--------|----------|-------|-----------------------|---------------|-------------------|-----------|-----------------|----------|----------|------|----------------------|---------|
| SUB-ENT-001 | Subscriptions | Entry Points | Verify entry navigation from Post-trip recommendation card | User finishes a trip triggering usage rule. | Step 1: Click post-trip card.<br>Step 2: Check screen state. | Plan: Basic | Navigates to Subscriptions Overview; recommended plan is highlighted & scrolled into view. | High | Minor | Functional | FR-SUB-1.1 | Yes | |
| SUB-ENT-002 | Subscriptions | Entry Points | Verify entry navigation from Account Screen | User is on Account profile dashboard. | Step 1: Tap Subscriptions row option.<br>Step 2: Observe view redirect. | N/A | Opens Subscriptions Overview screen with standard vertical stacked layout. | High | Minor | Functional | FR-SUB-1.1 | Yes | |
| SUB-ENT-004 | Subscriptions | Entry Points | Verify navigation behavior with pre-selected Premium plan | Post-trip rule triggers a Premium plan recommendation. | Step 1: Click the Premium post-trip recommendation card.<br>Step 2: Check layout view focus. | Plan: Premium | Overview screen opens with Premium card highlighted and automatically centered in viewport. | High | Minor | Functional | FR-SUB-1.2 | Yes | |
| SUB-OVR-001 | Subscriptions | Overview | Verify screen typography layout and 3D piggy-bank asset rendering | User navigates to Subscriptions Overview screen. | Step 1: Inspect top nav bar and headline formatting text strings.<br>Step 2: Verify status row copy. | Status: Free plan user | Top navigation bar titled "Subscription" with back arrow. Hero shows 3D piggy-bank icon, bold primary headline, and exact subheadline. Status row shows (ⓘ) "You are currently on the Free plan". | High | Minor | UI | FR-SUB-2.1 | Yes | |
| SUB-OVR-002 | Subscriptions | Overview | Verify Billing Cycle Switch Monthly to Annual toggle state mutations | User is on Subscriptions Overview screen. | Step 1: Tap the "Annual" toggle selection item.<br>Step 2: Observe toggle background coloration states. | N/A | Selected toggle renders with an active blue background state; inactive Monthly displays standard neutral grey background state. Annual displays embedded badge "Save 20%". | High | Minor | UI | FR-SUB-2.2 | Yes | |
| SUB-OVR-003 | Subscriptions | Overview | Verify Dynamic Price Update Logic across product cards | User is on Subscriptions Overview screen. | Step 1: Tap "Annual" toggle container segment.<br>Step 2: Observe Basic and Premium price figures.<br>Step 3: Tap "Monthly" toggle segment. | N/A | Prices dynamically recalculate and update across Basic and Premium cards in real-time without executing full screen reloads. Monthly toggle restores base prices. | High | Minor | Functional | FR-SUB-2.2 | Yes | |
| SUB-OVR-004 | Subscriptions | Overview | Verify Basic Plan Card component layouts and copy elements | User is on Subscriptions Overview screen. | Step 1: Inspect header, pricing font, and CTA button text copy string on Basic card. | N/A | Displays plan name "Basic Plan", light-blue pill badge "Value" anchored right. Active price format is bold blue "$9.99 /mo". CTA button explicitly reads "View more & Get Basic Now". | High | Minor | UI | FR-SUB-2.3 | Yes | |

---

# End of Template