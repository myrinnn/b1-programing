login_attempts = [("myanh", 1, "myanhhh123"),("carina", 2, "yourgirlcarina098"), ("andy", 1, "caitvyforlyfe567"), ("charla", 3, "098746"), ("isabel", 0, "oiwmxla"), ("nina", 3, "owo_owo")]

print("Checking login attempts...")

logged_in = False

while logged_in == False:
    username_attempt = input("Input username:")
    password_attempt = input("Input password:")

    user_found = False

    for username, attempts, password in login_attempts:
        if username_attempt == username:
            user_found = True
            if attempts >= 1:
                if password_attempt == password:
                    print("Login successful")
                    logged_in = True
                else:
                    print("Incorrect password")
                    attempts = attempts - 1
            else: 
                print("No more available login attempts")
                
    if user_found == False:
        print("Username not found")
                    
                
