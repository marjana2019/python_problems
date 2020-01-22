#  This program finds the cost per square inch of a pizza given its diameter an total price

import math

def area(d):
    return math.pi*(0.5*d)**2

def cost(price,d):
    return float(price)/area(d)


def main():

    price= eval(input("Enter the price of the pizza:"))
    d = eval(input("Enter the diameter of the pizza in inches:"))

    print ("The priceof the pizza per square inch is ", cost(price,d))

main()


    
