"""
Objective: 
	Implement and adapt the Elo Rating System to multiple domains

Future Goal:
	GLICKO and/or GLICKO 2 implementation
"""
import random
import string

listPID = []

#create a random string to ID the player, ensure ID is unique
def generatePID():
    isUnique = False
    while(isUnique == False):
        PID = ''.join(random.choices(string.ascii_letters + string.digits,  k=10))
        if PID not in listPID :
            isUnique = True
            listPID.append(PID)
            return PID

class Player:
    rating = 1000
    currExpected = 0

    def __init__(self, playerID):
        self.playerID = playerID    



def expectedScore(p1, p2):
	qOfX = (10**(p1.rating / 400))
	qOfY = (10**(p2.rating / 400))

	expectedX = (qOfX / (qOfX + qOfY) )
	expectedY = (qOfY / (qOfX + qOfY) )

	p1.currExpected = expectedX
	p2.currExpected = expectedY

def main():
    p1 = Player(generatePID())
    p1.rating = 1250

    p2 = Player(getPID())
    p2.rating = 1000

    print("\nPlayerID: "+p1.playerID +" , Rating: "+ str(p1.rating))
    print("PlayerID: "+p2.playerID +" , Rating: "+ str(p2.rating))
    print("p1 ID: "+p1.playerID)


    print("TEST:")

    expectedScore(p1, p2)

    print("\tExpected Score is the players probability of winning plus half of their probability of drawing.\n")

    print("p1 expected: " + str( p1.currExpected * 100) + "%")
    print("p2 expected: " + str( p2.currExpected * 100) + "%")

main()



