# A program that allows the user to type in a phrase and then outputs the acronym for that phrase.

def main():

    phrase = input("Enter a pharse:")
    acronym = ""

    for word in phrase.split():
        acronym = acronym+word[0]
    acronym = acronym.upper()

    print("The acronym of the phrase is", acronym)

main()
        
        
        
