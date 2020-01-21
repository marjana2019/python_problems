# A certain professor gives 5 point quizzes that are graded on the scale 5-A,4-B,3-C,2-D,1-F,0-F.
#A program that accepts the grade as input and prints out the corresponding grade.

def main():
    
    score =eval(input("Enter your score:"))

    grade = "FFDCBA"[score]

    
    print("Your grade is", grade)

main()
