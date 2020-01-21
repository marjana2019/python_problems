# 100 point exams that are graded on a scale 90-100:A,80-89:B,70-79:C,60-69:D,<60:F.
#Write a program thet accepts the score as input and prints out the grade as output


def main():
    score = eval(input("Enter your score:"))

    grade = 60*"F"+10*"D"+10*"C"+10*"B"+11"A"

    finalgrade = grade[score]

    print("Your grade is", finalgrade)

main()
