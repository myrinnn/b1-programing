passwords = [
"Pass123",
"SecurePassword1",
"weak",
"MyP@ssw0rd",
"NOLOWER123"
]
print("Validating passwords...")

compliant = 0
non_compliant = 0

for password in passwords:
    issues = []

    if len(password) < 8:
        issues.append("Too short")
        
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
    if not has_upper:
        issues.append("No uppercase letters")
    if not has_lower:
        issues.append("No lowercase letters")
    if not has_digit:
        issues.append("No digits")

    if len(issues) == 0:
        print("PASS: '" + password + "' - Meets all requirements")
        compliant += 1
    else:
        issue_text = ", ".join(issues)
        print("FAIL: '" + password + "' - " + issue_text)
        non_compliant += 1
print("Summary: " + str(compliant) + " compliant, " + str(non_compliant) + " non-compliant")