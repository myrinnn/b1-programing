score = int(input("Enter your score (0-100): "))

if score >= 0 and score <= 100: 
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Rejoice. Your grade is {grade}.")
    # Bonus: print encouragement for top grades
    if grade == "A":
        print("Excellent work!")
    if grade == "F":
        print("You are a disappointment to your family.")
else: 
    print("Invalid answer. Try learning how to read.")
    