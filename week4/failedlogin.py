login_attempts = [
("alice", "success"),
("bob", "fail"),
("bob", "fail"),
("charlie", "success"),
("bob", "fail"),
("alice", "fail")
]

print("Checking login attempts...")

fails = {}

for username, status in login_attempts:
    if status == "fail":
        if username in fails:
            fails[username] += 1
        else:
            fails[username] = 1
            
for username in fails:
    if fails[username] >= 3:
        print("ALERT: User '" + username + "' has 3 or more failed login attempts")
        print("Security check complete")




                    
                
