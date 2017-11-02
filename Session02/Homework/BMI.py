print("That's is program that calculate your BMI")
h = int(input("Enter your height (cm): "))
w = int(input("Enter your weight (kg): "))
bmi = w / ((h/100)**2)
if bmi < 16:
    print("You're severely underweight")
elif bmi < 18.5:
    print("You're underweight")
elif bmi < 25:
    print("You're normal")
elif bmi < 30:
    print("You're overweight")
else:
    print("You're obese")
