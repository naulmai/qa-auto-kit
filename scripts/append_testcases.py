import re

file_path = 'reports/Driver_Registration_Testcases.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# New Exhaustive Test Cases to add
new_cases = [
    # Boundary/Negative for Sign In
    ['REG-LGI-008', 'Registration', 'SignIn', 'FR-AUTH-1.1', 'Verify phone input ignores alphabetical characters', 'On Sign In', 'Step 1: Type abcXYZ into Phone Number field', 'abcXYZ', 'Field remains empty or strips non-numeric characters automatically.', 'Medium', 'Minor', 'UI', 'Yes', ''],
    ['REG-LGI-009', 'Registration', 'SignIn', 'FR-AUTH-1.1', 'Verify phone input ignores special characters', 'On Sign In', 'Step 1: Type @#$%^&* into Phone Number field', '@#$%^&*', 'Field remains empty or strips special characters.', 'Medium', 'Minor', 'UI', 'Yes', ''],
    ['REG-LGI-010', 'Registration', 'SignIn', 'FR-AUTH-1.1', 'Verify Sign In button remains disabled for incomplete phone number', 'On Sign In', 'Step 1: Enter valid password<br>Step 2: Enter exactly 7 digits in Phone field', 'Pass: Valid1!<br>Phone: 1234567', 'Sign In button remains visually disabled.', 'Medium', 'Minor', 'UI', 'Yes', ''],
    
    # Session Approval Edge Cases
    ['REG-DEV-008', 'Registration', 'SignIn', 'FR-AUTH-1.6.2', 'Verify Push Notification Approval Timeout', 'Push received on Device B', 'Step 1: On Device B ignore the push notification for 60 seconds<br>Step 2: Observe Device A state', 'Timeout: 60s', 'Device A displays approval timeout error and remains blocked. Device B session remains active.', 'High', 'Major', 'Edge', 'Yes', ''],
    ['REG-DEV-009', 'Registration', 'SignIn', 'FR-AUTH-1.6.2', 'Verify App Kill during Device Swap Approval', 'Push received on Device B', 'Step 1: On Device A force close the app while waiting for approval<br>Step 2: On Device B tap Yes It is me', 'App killed', 'Device B session is still terminated. Next launch of Device A requires a fresh login/OTP challenge.', 'High', 'Major', 'Edge', 'Yes', ''],
    
    # Support Assisted Recovery Edge Cases
    ['REG-REC-013', 'Registration', 'Support', 'FR-AUTH-1.5.6', 'Verify Stripe SDK cancellation routing', 'In Stripe SDK', 'Step 1: Tap Cancel or Back button inside the Stripe Identity SDK modal', 'User cancel', 'SDK closes gracefully and returns user to the OTP / Escalated Lockout screen.', 'Medium', 'Minor', 'UI', 'Yes', ''],
    ['REG-REC-014', 'Registration', 'Support', 'FR-AUTH-1.5.8.1', 'Verify Try Again preserves token and does not prompt recapture', 'On Upload Failed', 'Step 1: Network drops causing failure<br>Step 2: Reconnect network<br>Step 3: Tap Try Again', 'Network on', 'Upload resumes using previously captured images without re-triggering the camera.', 'High', 'Major', 'Edge', 'Yes', ''],
    
    # Sign Up Validations
    ['REG-SGN-009', 'Registration', 'SignUp', 'FR-AUTH-2.1', 'Verify very long phone numbers are truncated', 'On Sign Up', 'Step 1: Paste a 20 digit numeric string into Phone Number field', 'Paste 20 digits', 'Input is automatically truncated to the maximum allowed length (e.g. 15 digits).', 'Medium', 'Minor', 'Boundary', 'Yes', ''],
    ['REG-SGN-010', 'Registration', 'SignUp', 'FR-AUTH-2.3.1', 'Verify consecutive quick taps on Continue do not dispatch multiple OTPs', 'Unregistered number', 'Step 1: Enter valid number and check Terms<br>Step 2: Tap Continue button 5 times rapidly', 'Rapid taps', 'Only one OTP request is dispatched to the backend (Button debounce validation).', 'Medium', 'Minor', 'Edge', 'Yes', ''],
    
    # OTP Validations
    ['REG-OTP-011', 'Registration', 'OTP', 'FR-AUTH-3.1', 'Verify OTP entry accepts copy-paste', 'On OTP screen', 'Step 1: Copy 6-digit code<br>Step 2: Paste into the first OTP input box', 'Paste OTP', 'The 6 digits populate across all 6 input boxes automatically.', 'Medium', 'Minor', 'UI', 'Yes', ''],
    ['REG-OTP-012', 'Registration', 'OTP', 'FR-AUTH-3.3', 'Verify Resend Timer exact boundary expiration', 'Timer running', 'Step 1: Wait exactly until timer hits 00:00<br>Step 2: Tap Resend Code immediately', 'Exact 0s', 'Resend API is triggered successfully without race condition blockage.', 'Medium', 'Minor', 'Boundary', 'Yes', ''],
    
    # Rate Limiting Boundary
    ['REG-OTP-013', 'Registration', 'OTP', 'FR-AUTH-3.6.1', 'Verify 24-hour rate limit expiration resets counter', 'Phone limited', 'Step 1: Wait 24 hours and 1 minute since first request<br>Step 2: Request OTP', 'Wait 24h1m', 'Request is accepted as the rolling 24-hour window drops the oldest request.', 'High', 'Major', 'Boundary', 'No', 'API_TEST_ONLY'],
    ['REG-OTP-014', 'Registration', 'OTP', 'FR-AUTH-3.6.2', 'Verify 1-hour IP rate limit expiration resets counter', 'IP limited', 'Step 1: Wait 1 hour and 1 minute since first request<br>Step 2: Request OTP', 'Wait 1h1m', 'Request is accepted as the rolling 1-hour window clears.', 'High', 'Major', 'Boundary', 'No', 'API_TEST_ONLY'],
    
    # Password Boundaries
    ['REG-PWD-008', 'Registration', 'Password', 'FR-AUTH-4.3', 'Verify exact boundary of 256 characters for password', 'On Create Pass', 'Step 1: Paste a 256 character valid password string', '256 chars', 'Password accepted and all checkmarks turn green.', 'Low', 'Minor', 'Boundary', 'Yes', ''],
    ['REG-PWD-009', 'Registration', 'Password', 'FR-AUTH-4.3', 'Verify exact boundary of 257 characters for password', 'On Create Pass', 'Step 1: Paste a 257 character string', '257 chars', 'Input is truncated to 256 characters OR system displays length error.', 'Low', 'Minor', 'Boundary', 'Yes', ''],
    ['REG-PWD-010', 'Registration', 'Password', 'FR-AUTH-4.3', 'Verify absence of number prevents signup', 'On Create Pass', 'Step 1: Enter password missing a number', 'Pass: Abcdefg!', 'Checklist item 1 number remains grey. Button disabled.', 'Medium', 'Minor', 'Negative', 'Yes', ''],
    ['REG-PWD-011', 'Registration', 'Password', 'FR-AUTH-4.3', 'Verify absence of special character prevents signup', 'On Create Pass', 'Step 1: Enter password missing special char', 'Pass: Abcdefg1', 'Checklist item 1 special character remains grey. Button disabled.', 'Medium', 'Minor', 'Negative', 'Yes', ''],
    
    # Forgot Password Boundaries
    ['REG-RST-007', 'Registration', 'ForgotPass', 'FR-AUTH-5.4', 'Verify 5 incorrect OTPs in reset triggers exactly 5 min cooldown', 'On Reset OTP', 'Step 1: Fail OTP 5 times<br>Step 2: Wait 4m 59s and attempt input<br>Step 3: Wait 5m 01s and attempt input', 'Timing check', 'Input blocked at 4m 59s. Input accepted at 5m 01s.', 'High', 'Major', 'Boundary', 'Yes', ''],
]

# Generate rows
new_rows = []
for case in new_cases:
    new_rows.append('| ' + ' | '.join(case) + ' |')

# Insert into table
# Table ends at EOF, just append
content += '\n' + '\n'.join(new_rows) + '\n'

# Update Metadata Total Test Cases
content = re.sub(r'\|\s*\*\*Total Test Cases\*\*\s*\|\s*\d+\s*\|', '| **Total Test Cases** | 64 |', content)

# Update Edge Case Summary
edge_summary = '''| EDGE-001 | Edge Case Report | IP Cycling Rate Limit Bypass | REG-OTP-006, REG-OTP-010, REG-OTP-014 |
| EDGE-002 | Edge Case Report | Session Approval Rejection Delay | REG-DEV-006, REG-DEV-008 |
| EDGE-003 | Edge Case Report | Network Drop During Stripe Upload | REG-REC-004, REG-REC-011, REG-REC-014 |
| EDGE-004 | Edge Case Report | Persistent Lockout on App Kill | REG-LCK-005, REG-DEV-009 |'''
content = re.sub(r'\| EDGE-001.*?\| EDGE-004.*?\n', edge_summary + '\n', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Successfully added {len(new_cases)} edge/boundary test cases. Total is now 64.')
