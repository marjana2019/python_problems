# A program that classifies students based on the credits earned,
# less than 7 credits is a Freshman, at least 7 credits to be a Sophomore
#16 to be a Junior and 26 for Senior

def main():
    credit = eval(input("Enter the number of credits earned:"))

    if credit <7 :
        status = "Freshman"
    elif credit <16:
        status = "Sophomore"
    elif credit <26:
        status ="Junior"
    else:
        status = "Senior"

    print("The status of the student is ", status )

main()
    
