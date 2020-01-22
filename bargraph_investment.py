# This program draws a bar graph showing the future value of 10 years of an investment.

from graphics import *

def main():

    principal = eval(input("Enter a principal value for investment:"))

    apr = eval(input("Enter an  annual interest rate :"))

    win = GraphWin("Investment Chart", 320,240)
    win.setBackground("white")

    Text(Point(20,230),"0.0K").draw(win)
    Text(Point(20,180),"2.5K").draw(win)
    Text(Point(20,130),"5.0K").draw(win)
    Text(Point(20,80),"7.5K").draw(win)
    Text(Point(20,30),"10K").draw(win)

    height = principal * 0.02
    bar = Rectangle(Point(40,230), Point(65,230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range (1,11):
        principal = principal * (1+ apr)

        height = principal * 0.02
        xll = year*25+40
        bar = Rectangle(Point(xll,230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    input("Press <Enter> to quit")
    win.close()

main()

                    
    
    
