# This program can encode a message into Caesar cipher

def encode(message,key):
    cipher = ""
    for letter in message:
        cipher = cipher + chr(ord(letter)+key)
    return cipher

def main():
    message = input("Enter the message to be encode:")
    key = eval(input("Enter the key to encode the message"))

    print("The encoded message is" , encode(message,key))

main()
