# This program calculates the value of a full name
def main():

    name = input("Enter a full name:")
    name = "".join(name.split())
    
    value = 0
    for letter in name:
        value = value + ord((letter).lower()) - ord ("a") + 1

    print ("The value of the name is", value)

main()
    
    
