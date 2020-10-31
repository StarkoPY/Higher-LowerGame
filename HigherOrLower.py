import random

point = 0

firstCardHigh = False
firstCardLow = False
secondCardHigh = False
secondCardLow = False
userHigh = False
userLow = False
Cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

dict = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
firstCard = random.choice(Cards)

if firstCard == 1:
    print(dict[1])
elif firstCard == 11:
    print(dict[11])
elif firstCard == 12:
    print(dict[12])
elif firstCard == 13:
    print(dict[13])
else:
    print(firstCard)

userChoice = input("Enter your guess: 0 for LOWER, and 1 HIGHER: ")
int(userChoice)

if userChoice == 0:
    userLow = True
else:
    userHigh = True

secondCard = random.choice(Cards)

if firstCard > secondCard:
    firstCardHigh = True

if firstCard < secondCardLow:
    firstCardLow = True

if secondCard > firstCard:
    secondCardHigh = True

if secondCard < firstCardLow:
    secondCardLow = True

if firstCardHigh and userLow:
    point += 1

if secondCardHigh and userHigh:
    point += 1

if secondCard == 1:
    print(dict[1])
elif secondCard == 11:
    print(dict[11])
elif secondCard == 12:
    print(dict[12])
elif secondCard == 13:
    print(dict[13])
else:
    print(secondCard)

if point == 0:
    print("LOLst joe bills nibba")
if point == 1:
    print("congratz, you paid yo debt")