# A program that accepts the exam score and finds out the grade

def main():

    score = eval(input("Enter the exam score:"))

    if score<60:
        grade = "F"
    elif score<70:
        grade = "D"
    elif score<80:
        grade = "C"
    elif score<90:
        grade = "B"

    else:
        grade = "A"

    print ("The grade is ", grade)

main()
        
