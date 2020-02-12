# A program that calculates a persons BMI

def main():
    weight = eval(input("Enter your weight in lbs:"))
    height = eval(input("Enter your height in inches :"))

    bmi = (weight * 720)/height**2

    if bmi < 19:
        print("You are below the healthy rage")
    elif bmi <= 25:
        Print ("You are healthy ")
    else:
        print ("You are above the healthy rage")

        

main()

        
