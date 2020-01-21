# This program calculates the numeric value of a name

def main():
    name = input("Enter a name:")
    sum = 0
    for letter in name:
        sum = sum + ord(letter.lower())- ord("a") + 1

    print (" The value of the nam is :",sum)

main()
        
