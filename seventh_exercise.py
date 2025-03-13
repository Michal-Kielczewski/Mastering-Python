kg = float(input("Enter your weight in kg: "))
m = float(input("Enter your height in meters: "))
m2 = m*m
bmi = kg/m2
bmi = round(bmi, 2)

if bmi < 16:
    print(f"Your BMI is {bmi}, you are severely underweight")
elif 16 <= bmi < 18.4:
    print(f"Your BMI is {bmi}, you are underweight")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi}, you are normal weight")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi}, you are overweight")
elif 30 <= bmi < 34.9:
    print(f"Your BMI is {bmi}, you are Moreately Obese")
elif 35 <= bmi < 39.9:
    print(f"Your BMI is {bmi}, you are Severely Obese")
else:
    print(f"Your BMI is {bmi}, you are Morbidly Obese")

