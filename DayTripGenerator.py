import sys
import random

dest = ["Roswell", "Suwanee", "Marietta", "Savannah", "Columbus", "Augusta", "Buckhead"]
rest = ["Italian", "Chinese", "Korean", "Vietnamese", "Mexican", "Pizza"]
transport = ["Car", "Bus", "Helicoptor", "Bi-plane", "Uber/Taxi"]
entertain = ["Concert", "Pub Crawl", "Museum", "Wildlife Center", "Theatre"]
randomList = [random.choice(dest), random.choice(rest), random.choice(transport), random.choice(entertain)]

def confirmedList(randomList):
    print("Confrimed Day Trip\n"+
          "Destination(1): " + randomList[0]+
          "\nResturant(2): " + randomList[1]+
          "\nMode of Transport(3): " + randomList[2]+
          "\nEntertainment(4): " + randomList[3]+"\n")
    return 0

def printFunc(randomList):    
    print("Destination(1): " + randomList[0]+
          "\nResturant(2): " + randomList[1]+
          "\nMode of Transport(3): " + randomList[2]+
          "\nEntertainment(4): " + randomList[3])
    i = int(input("\nEnter numbers 1 - 4 to randomize the respective line or 0 to confirm your trip: "))
    print("\n")

    if i == 0: 
        return confirmedList(randomList)        
    elif i == 1:
        randomList[i-1] = random.choice(dest)
        return printFunc(randomList)
    elif i == 2:
        randomList[i-1] = random.choice(rest)
        return printFunc(randomList)
    elif i == 3:
        randomList[i-1] = random.choice(transport)
        return printFunc(randomList)
    elif i == 4:
        randomList[i-1] = random.choice(entertain)
        return printFunc(randomList)
    else: return printFunc(randomList)

printFunc(randomList)