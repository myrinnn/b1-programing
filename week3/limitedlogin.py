correct_pin = "1234"
attempts = 0
max_attempts = 3
login_successful = False
for i in range(max_attempts):
    print(f"Attempts left: {max_attempts - i}/{max_attempts}")
    entered_pin = input("Enter your PIN: ")
    if entered_pin == correct_pin:
        login_successful = True
        break 
    else:
        print("Incorrect PIN.")
if login_successful:
    print("Correct PIN. Congratulations.")
else:
    print("You are barred from this device forever. Suffer.")

    