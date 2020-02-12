# simulation of a racquetball game

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummery(winsA, winsB)

def printIntro():

    print ("This program simulates a game of racquetball between two")


def getInputs():
    a = eval(input("Whats the probability that player A wins a serve?"))
    b = eval(input("whats the probability that player B wins a serve?"))
    n = eval(input("how many games to simulate?"))

    return a, b, n

def simNGames(n, probA, probB):
    winsA= winsB = 0
    for i in range (n):
        scoreA,ScoreB = simOneGame(probA,probB)
        if scoreA> scoreB:
            winsA = winssA+1
        else:
            winsB = winsB+1
    return winsA, winsB
            

def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver (scoreA,ScoreB):
        if serving == "A":
            if random()<probA:
               scoreA = scoreA+ 1
            else:
                serving = "B"

        else:
            if random ()< probB:
                scoreB = ScoroeB +1

            else:
                serving = "A"

    return scoreA, scoreB

def gameOver(a,b):

    return a==15 or b==15

def printSummery(winsA, winsB):
    n = winsA+winsB
    print ("Games simulated", n)
    print ("wins for A ", winsA)
    print("wins for B", winsB)

main()



            
    
