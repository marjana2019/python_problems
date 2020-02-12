# A program calculates the fine for speeding
# $50 plus $5 for each addtional mph over the limit and $200 penalty over 90mph

def main():
    speed = eval(input("Enter the speed:"))
    limit = eval(input("Enter the speed limit :"))

    if speed < limit:
        print (" Speed was legal")

    else:
        penalty = 50 + 5 *(speed-limit)
        if speed>90:
           penalty =  penalty + 200

        print ("Your penalty", penalty)

main()
               

        
