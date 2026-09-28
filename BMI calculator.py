print("Hello Welcome to BMI calculator")
a=float(input("Enter your Weight in Kilograms:"))
b=float(input("Enter your Height in Meters:"))
def bmi(a,b):
    return(a/(b*2))
print(f"Your BMI: {bmi(a,b)}")
def main():
        if bmi(a,b)<18.5:
            print("You are Underweight")
        elif 18.5<=bmi(a,b)<=24.9:
            print("You are Healthy")
        elif 25.0<=bmi(a,b)<=29.9:
            print("You are Overweight")
        else:
            print("You are Obese")
main()