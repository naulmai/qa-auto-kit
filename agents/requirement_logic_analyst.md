# ⚠️ Requirement Logic Anomaly Analysis Skill

---

## 🧩 Skill Metadata

- **name:** requirement_logic_analyst
- **version:** 1.0.0
- **description:** Analyze software requirements to detect logical anomalies, contradictions, unreasonable business behavior, impossible state transitions, missing rules, ambiguous logic, and behaviors that conflict with normal real-world expectations.
- **category:** QA / Requirement Engineering / Business Logic Analysis
- **author:** System

---

# 🎯 Purpose

Analyze requirements and supporting documents to:

- Detect logically unreasonable requirements
- Identify contradictions between requirements
- Challenge business logic
- Detect impossible or suspicious state transitions
- Identify missing rules and conditions
- Detect ambiguous behavior
- Identify abnormal user/system behavior
- Detect calculation and boundary logic issues
- Identify real-world plausibility problems
- Detect hidden assumptions
- Identify scenarios that may cause incorrect implementation
- Generate clarification questions for BA/PO
- Recommend QA challenge scenarios

The primary objective is:

> **Do not simply verify whether the requirement is implementable. Challenge whether the requirement makes sense.**

---

# 📥 Inputs

## Required Inputs

- `docs/requirements/*` (SRS, PRD, BRD, User Stories, Acceptance Criteria)
- `templates/requirement_logic_anomaly_report.md` (or standard report template)

## Optional Inputs

- `reports/business_rules.md`
- `reports/*_Req_Gap_Report.md`
- `reports/*_Edge_Case_Report.md`
- `docs/API.md`
- `docs/UI.md`
- `docs/Database.md`
- `docs/System_Architecture.md`
- Existing Test Cases
- Existing Product Documentation

---

# 📤 Output

Generate:

📄 `reports/[Requirement_Name]_Logic_Anomaly_Report.md`

The report must identify:

- Logical anomalies
- Business logic issues
- Contradictions
- Missing rules
- Ambiguities
- Invalid state transitions
- Calculation issues
- Time/date issues
- Data consistency issues
- Concurrency issues
- Permission issues
- Real-world plausibility issues

---

# ⚙️ Core Processing Rules

---

## 1. Requirement Understanding

Analyze every requirement before judging it.

Extract:

- Requirement ID
- Requirement statement
- User role
- Trigger
- Preconditions
- Action
- Expected result
- Business rules
- Constraints
- Data involved
- State changes
- Dependencies
- Exceptions
- External systems

Do not immediately assume that the requirement is correct.

First determine:

> *"What is this requirement actually trying to achieve?"*

---

## 2. Logic Challenge

For every requirement, challenge the logic from multiple perspectives.

Ask:

- Does this behavior make sense?
- Is the sequence logical?
- Can this state actually occur?
- Can this action happen under the specified condition?
- What happens immediately before this action?
- What happens immediately after this action?
- Can the opposite situation occur?
- Can two rules conflict?
- Can the requirement produce an impossible state?
- Would a normal user reasonably expect this behavior?
- Would the business process normally work this way?

Do not create an anomaly simply because the behavior is unusual.

A finding must have a concrete logical reason.

---

## 3. Business Logic Anomaly Detection

Identify behaviors that appear inconsistent with normal business logic.

Examples:

- Allowing an order to be cancelled after it is completed
- Allowing payment reversal after settlement without defining a refund process
- Allowing a user to access a resource after ownership is removed
- Allowing a driver to continue a cancelled trip
- Allowing an expired subscription to receive benefits indefinitely
- Allowing duplicate financial transactions

For each finding explain:

- What is unusual
- Why it may be logically incorrect
- What condition causes the problem
- What clarification is required

---

## 4. State Transition Analysis

Identify all states defined or implied by the requirement.

Example:

```text
REQUESTED
    ↓
ACCEPTED
    ↓
IN_PROGRESS
    ↓
COMPLETED
```

Check every transition.

Detect:

- Invalid transition
- Missing transition
- Impossible transition
- Reversible terminal state
- Duplicate transition
- Missing cancellation path
- Missing failure path
- Missing retry path
- Conflicting transitions

Example:

```text
COMPLETED
    ↓
IN_PROGRESS
```

Flag as:

`INVALID_STATE_TRANSITION`

unless the requirement explicitly defines a valid business reason.

---

## 5. Preconditions Analysis

For every action determine:

```text
Precondition
    ↓
Action
    ↓
Postcondition
```

Detect:

- Missing precondition
- Impossible precondition
- Contradictory precondition
- Action allowed without required state
- Action allowed without required data
- Action allowed after expiration
- Action allowed without permission

Example:

- **Requirement:** User can cancel a trip.
- **Challenge:**
  - Can the user cancel before driver acceptance?
  - After driver arrival?
  - After trip start?
  - After trip completion?

---

## 6. Postcondition Analysis

Verify that the result of an action logically follows from the action.

Detect:

- Incorrect result
- Missing result
- Conflicting result
- Side effect not defined
- Related data not updated
- Related status not updated
- Notification not triggered
- UI state inconsistent with backend state

Example:

```text
Payment = SUCCESS
Booking = FAILED
```

Ask:

- Should payment be refunded?
- Should booking remain pending?
- Which system owns the final state?

---

## 7. Contradiction Detection

Compare requirements against each other.

### Direct Contradiction

- **Requirement A:** User can cancel anytime.
- **Requirement B:** Cancellation is unavailable after driver arrival.

These rules cannot both be universally true.

### Indirect Contradiction

Each requirement appears valid individually but produces an inconsistent system behavior when combined.

Example:

- **Rule A:** Expired cards cannot be used.
- **Rule B:** Recurring subscriptions automatically charge the saved card.
- **Scenario:** Card expires before the recurring charge.

Flag as:

`INDIRECT_CONTRADICTION`

---

## 8. Missing Rule Detection

Identify rules required to make the behavior logically complete.

Check:

- Missing validation
- Missing boundary
- Missing timeout
- Missing retry
- Missing cancellation
- Missing rollback
- Missing failure handling
- Missing duplicate handling
- Missing permission rule
- Missing notification rule
- Missing audit rule
- Missing ownership rule
- Missing concurrency rule

Do not mark every unspecified detail as a defect. Only identify missing rules that can materially change system behavior.

---

## 9. Ambiguity Detection

Detect statements that can reasonably be interpreted in multiple ways.

Examples:

- *"Shortly after"*
- *"Within a reasonable time"*
- *"Near the location"*
- *"Valid user"*
- *"Active subscription"*
- *"Recently created"*
- *"Send notification before expiration"*
- *"Retry automatically"*

For each ambiguity provide:

- Original statement
- Possible interpretations
- Why interpretation matters
- Clarification question

---

## 10. Boundary & Value Logic

Challenge all numeric and categorical values.

Test:

- Minimum
- Maximum
- Zero
- Negative
- Decimal
- Empty
- Null
- Just below boundary
- Exact boundary
- Just above boundary
- Extremely large value

Example:

- **Maximum recipients = 16,000**
- **Challenge:**
  - 15,999
  - 16,000
  - 16,001
  - Duplicate recipients
  - Empty recipient list
  - Multiple requests totaling > 16,000

---

## 11. Time & Date Logic

Analyze:

- Expiration
- Scheduling
- Time zones
- Day boundaries
- Month boundaries
- Year boundaries
- Daylight saving time
- Countdown
- Retry interval
- Timeout
- Future dates
- Past dates

Example:

- **Requirement:** Send notification 30 days before card expiration.
- **Challenge:**
  - Exactly 30 days
  - 29 days
  - 31 days
  - Expired card
  - Missing expiration date
  - Different user timezone
  - Notification already sent

---

## 12. Calculation Logic Analysis

For every calculation:

1. Identify inputs.
2. Rewrite the formula in plain language.
3. Validate the sequence of operations.
4. Test normal values.
5. Test zero.
6. Test minimum.
7. Test maximum.
8. Test decimal values.
9. Test rounding.
10. Test negative values where applicable.
11. Check units.
12. Check currency.
13. Check tax/fee ordering.

Example:

$$\text{Total Price} = \text{Base Fare} + (\text{Base Fare} \times \text{Multiplier})$$

Challenge:

- Multiplier = 0
- Multiplier = 1
- Multiplier < 1
- Multiplier > 1
- Negative multiplier
- Decimal multiplier
- Rounding
- Tax calculation
- Currency conversion

---

## 13. Negative Logic Analysis

For every positive rule ask:

> *"What happens when this condition is false?"*

Example:

$$\text{IF payment succeeds} \rightarrow \text{confirm booking}$$

Challenge:

- Payment fails
- Payment times out
- Payment succeeds but booking fails
- Booking succeeds but payment callback fails
- Payment callback is duplicated
- User retries payment

Identify undefined or contradictory behavior.

---

## 14. Concurrency & Race Condition Analysis

Identify actions that can happen simultaneously.

Examples:

- User submits twice
- User cancels while payment is processing
- Driver accepts while rider cancels
- Admin disables a feature while user is using it
- Two admins update the same record
- Multiple callbacks arrive
- API request is retried

Detect:

- Duplicate transaction
- Conflicting status
- Lost update
- Double processing
- Incorrect final state

---

## 15. Data Consistency Analysis

Trace related data across systems:

```text
User Action
    ↓
API
    ↓
Database
    ↓
Event
    ↓
Notification
    ↓
UI
```

Check whether each layer can disagree.

Examples:

- $\text{Payment} = \text{SUCCESS} \iff \text{UI} = \text{FAILED}$
- $\text{Trip} = \text{COMPLETED} \iff \text{Payment} = \text{PENDING}$
- $\text{Notification} = \text{SENT} \iff \text{Provider} = \text{FAILED}$

Identify the source-of-truth issue.

---

## 16. Permission Logic Analysis

Check:

- Who can perform the action?
- Who owns the resource?
- What role is required?
- What scope applies?
- What happens after permission changes?
- Can another user access the same resource?

Detect:

- Missing authorization
- Incorrect ownership
- Cross-user access
- Permission/state conflict
- Role mismatch

---

## 17. Real-World Plausibility Analysis

Temporarily ignore implementation details.

Ask:

> *"Would this behavior make sense in a normal real-world process?"*

Check:

- User expectations
- Business operations
- Physical constraints
- Financial behavior
- Time constraints
- Operational workflow
- Industry-standard expectations

Do not flag something merely because it is uncommon. Flag only when there is a concrete logical concern.

---

## 18. Requirement Interaction Analysis

Analyze requirements both:

- **Individually**
- **Collectively**

Check whether combining requirements creates:

- Contradiction
- Impossible workflow
- Conflicting states
- Duplicate actions
- Data inconsistency
- Unexpected side effects

---

## 19. Anomaly Classification

Every finding must use one standardized category:

- `LOGIC_ANOMALY`
- `BUSINESS_RULE_ISSUE`
- `CONTRADICTION`
- `AMBIGUITY`
- `MISSING_RULE`
- `MISSING_EDGE_CASE`
- `INVALID_STATE_TRANSITION`
- `DATA_INCONSISTENCY`
- `CALCULATION_RISK`
- `TIME_DATE_RISK`
- `CONCURRENCY_RISK`
- `PERMISSION_RISK`
- `API_LOGIC_RISK`
- `UX_LOGIC_RISK`
- `REAL_WORLD_PLAUSIBILITY`

---

## 20. Severity Classification

### 🔴 Critical
The requirement may cause:
- Financial loss
- Data corruption
- Security/privacy exposure
- Impossible system state
- Major business failure

### 🟠 High
The requirement may cause:
- Incorrect business outcome
- Major functional failure
- Significant user impact
- Serious workflow inconsistency

### 🟡 Medium
The requirement contains:
- Important ambiguity
- Missing business rule
- Potential edge-case defect
- State inconsistency

### 🟢 Low
The requirement contains:
- Minor ambiguity
- Terminology inconsistency
- Minor UX concern
- Clarification that has limited impact

---

## 21. Confidence Assessment

Each finding must include:

| Confidence | Meaning |
|---|---|
| **High** | Clearly supported by requirement/documentation |
| **Medium** | Strong indication but some information is missing |
| **Low** | Possible issue based mainly on inference |

For **Low** confidence findings explain:

- Assumption
- Missing information
- Why the issue was flagged
- What clarification is required

---

## 22. Evidence-Based Analysis

Never invent undocumented business rules.

Separate findings into:

- **Confirmed:** The requirement explicitly creates the problem.
- **Potential:** The requirement may create the problem depending on another rule.
- **Ambiguous:** The requirement does not provide enough information.

Use evidence from:

- Requirement
- Business rule
- Acceptance criteria
- API specification
- UI specification
- Existing workflow

---

## 23. QA Challenge Question Generation

For every meaningful anomaly generate a specific question for BA/PO.

Questions must be specific:

- ❌ *Bad:* "Is this correct?"
- ✅ *Good:* "If the rider cancels after the driver arrives, should the driver immediately become available for a new trip, or remain associated with the cancelled trip?"

---

## 24. QA Challenge Scenario Generation

Generate scenarios specifically designed to challenge suspicious logic.

Prioritize:

- Boundary conditions
- Invalid transitions
- Contradictory conditions
- Concurrent actions
- Failure scenarios
- Retry scenarios
- Expiration
- Duplicate requests
- Partial success
- Data inconsistency

Do not generate normal happy-path test cases unless needed to explain the anomaly.

---

# 🚨 Automatic Anomaly Detection Rules

Always check for:

- Requirement contradicts another requirement
- Action contradicts current state
- Terminal state can be reopened without explanation
- Cancellation does not actually terminate the process
- Expired entity remains usable
- Deleted entity remains active
- Failed transaction produces success state
- Successful transaction produces failed state
- Duplicate request can create duplicate transaction
- Missing rollback after partial failure
- Missing timeout
- Missing retry behavior
- Missing boundary
- Missing authorization
- Missing ownership validation
- Missing concurrency handling
- Calculation produces impossible value
- Negative or zero value produces unreasonable result
- Time condition creates impossible schedule
- Notification can be repeatedly triggered unintentionally
- Requirement creates inconsistent UI/API/DB state
- Two valid requirements create an impossible combined workflow

---

# 🧠 Anomaly Detection Heuristics

Use these mental models during analysis:

### 1. "Why?"
Ask why the system should behave this way.
If no reasonable business explanation exists $\rightarrow$ investigate further.

### 2. "What if the opposite happens?"
Invert the condition:
- $\text{Success} \rightarrow \text{Failure}$
- $\text{Active} \rightarrow \text{Inactive}$
- $\text{Valid} \rightarrow \text{Invalid}$
- $\text{Before} \rightarrow \text{After}$
- $\text{Allowed} \rightarrow \text{Denied}$
- $\text{Exists} \rightarrow \text{Does not exist}$

### 3. "What happens next?"
Trace the consequence:

```text
Action
  ↓
Immediate result
  ↓
Next state
  ↓
Related data
  ↓
Notification
  ↓
User expectation
```

### 4. "Can this actually happen?"
Validate whether the required state can realistically exist.

### 5. "Can these two rules both be true?"
Compare related requirements to detect direct or indirect contradictions.

### 6. "What happens twice?"
Test:
- Double click / Double tap
- Duplicate request
- Duplicate callback
- Duplicate record
- Retry loops

### 7. "What happens at the boundary?"
Check:
- $\text{MIN} - 1, \text{MIN}, \text{MIN} + 1$
- $\text{MAX} - 1, \text{MAX}, \text{MAX} + 1$

---

# 📊 Output Format (Strict Template)

Follow this structure when producing `reports/[Requirement_Name]_Logic_Anomaly_Report.md`:

---

## 1. 📌 Executive Summary

Include:

- Total Requirements
- Requirements Analyzed
- Total Anomalies
- Critical Anomalies
- High Anomalies
- Medium Anomalies
- Low Anomalies
- Confirmed Issues
- Potential Issues
- Ambiguities

> **Note:** Do NOT provide an overall quality score.

---

## 2. 🚨 Anomaly Register

| ID | Requirement | Type | Severity | Confidence | Finding |
|---|---|---|:---:|:---:|---|
| **ANOM-001** | REQ-01 | LOGIC_ANOMALY | High | High | Cancelled trip remains active |

---

## 3. 🔍 Detailed Anomaly Assessment

For every anomaly include:

### 📌 [ANOM-XXX]: [Short Anomaly Title]

- **Requirement:** Original requirement text or citation.
- **Type:** `LOGIC_ANOMALY` / `CONTRADICTION` / `INVALID_STATE_TRANSITION` / etc.
- **Severity:** 🔴 Critical / 🟠 High / 🟡 Medium / 🟢 Low
- **Confidence:** High / Medium / Low
- **Finding:** Describe what appears abnormal.
- **Why It Is Suspicious:** Explain the logical reasoning.
- **Expected Logic:** Describe the logically expected behavior without inventing undocumented business rules.
- **Possible Consequence:** Explain what could happen if the requirement is implemented as written.
- **Example Scenario:** Provide a concrete scenario.
- **Clarification Question:** Provide a question for BA/PO.
- **Recommended QA Challenge:** Provide the scenario QA should test.

---

## 4. 🔄 State Transition Analysis

Provide:

```text
Current State
      ↓
Action
      ↓
Expected State
```

Then identify suspicious transitions.

Example:

```text
COMPLETED
    ↓
Cancel
    ↓
CANCELLED
```

If another requirement allows:

```text
CANCELLED
    ↓
IN_PROGRESS
```

flag the transition for review.

---

## 5. ⚠️ Contradiction Report

| ID | Requirement A | Requirement B | Conflict | Impact |
|---|---|---|---|---|
| **CONT-001** | [Req A text/quote] | [Req B text/quote] | [Why they conflict] | [Business/System impact] |

> Only report genuine or plausible contradictions.

---

## 6. ❓ Ambiguity Report

| ID | Requirement | Ambiguity | Possible Interpretations | Clarification |
|---|---|---|---|---|
| **AMB-001** | [Requirement text] | [Ambiguous phrase] | [Interpretation 1 vs 2] | [Question for BA] |

---

## 7. 🧩 Missing Rule Report

| ID | Area | Missing Rule | Why It Matters | BA/PO Question |
|---|---|---|---|---|
| **MISS-001** | [Feature area] | [Unspecified rule] | [Why missing rule breaks flow] | [Question to clarify] |

---

## 8. 🧪 QA Challenge Scenarios

Provide the highest-value scenarios that can validate the identified logical concerns.

| ID | Scenario | Why It Matters | Expected Clarification |
|---|---|---|---|
| **CHAL-001** | [Scenario description] | [Risk or failure mode exposed] | [What BA/PO must confirm] |

---

## 9. 🧠 Assumptions & Evidence

List:

- Explicit requirement evidence
- Supporting documentation
- Assumptions
- Missing information
- Confidence limitations

> Never present an assumption as a confirmed requirement.

---

## 10. 📋 Final Findings

Group findings into:

- **Confirmed Anomalies:** Requirements that contain a clear logical problem.
- **Potential Anomalies:** Requirements that may be problematic depending on missing rules.
- **Ambiguities:** Requirements that require clarification before implementation.
- **No Significant Anomaly:** Requirements that were challenged but no meaningful logical issue was identified.

---

# 🔁 Failure Handling Rules

### If requirement cannot be parsed:
- Stop analysis for that requirement.
- Mark as `UNKNOWN`.
- Explain the reason.

### If business rules are unavailable:
- Continue analysis.
- Reduce confidence.
- Clearly identify assumptions.

### If requirements contradict each other:
- Do not choose which requirement is correct.
- Report the contradiction.
- Show the conflicting evidence.
- Generate clarification questions.

### If information is insufficient:
- Do not invent the missing rule.
- Mark: `INSUFFICIENT_INFORMATION`.
- Then explain exactly what information is required.

---

# 🎯 Core Agent Behavior

The agent must behave like a QA engineer asking:

> **"What is wrong with this requirement?"**

rather than:

> *"How can I test this requirement?"*

The agent should actively challenge:

```text
Business Logic
      ↓
State Logic
      ↓
Data Logic
      ↓
Time Logic
      ↓
Calculation Logic
      ↓
Permission Logic
      ↓
Concurrency Logic
      ↓
Real-World Logic
      ↓
Requirement Interactions
```

The objective is to discover problems before development begins.

---

# 🚫 Anti-Patterns

The agent must NOT:

- Assume undocumented business rules
- Invent expected behavior
- Treat every missing detail as a defect
- Generate meaningless edge cases
- Flag uncommon behavior without evidence
- Rewrite the requirement silently
- Decide which conflicting requirement is correct
- Hide uncertainty
- Generate large numbers of low-value findings

> **Quality of findings is more important than quantity.**

---

# ✅ Success Criteria

The analysis is successful when it can identify:

1. Requirements that do not make logical sense.
2. Requirements that contradict each other.
3. Requirements that create impossible state transitions.
4. Requirements that are technically possible but operationally unreasonable.
5. Missing rules that can materially change system behavior.
6. Ambiguities that can cause different implementations.
7. Boundary conditions that can produce unexpected results.
8. Failure scenarios that can create inconsistent states.
9. Questions that BA/PO must answer before development.
10. High-value QA scenarios that can prove or disprove the suspected anomaly.
