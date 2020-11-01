import random

point = 0
while 0 < 1:
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

    userChoice = input("Enter your guess: 0 for LOWER, and any number for HIGHER: ")
    int(userChoice)

    if userChoice == '0':
        userLow = True
    else:
        userHigh = True

    secondCard = random.choice(Cards)

    if firstCard > secondCard:
        firstCardHigh = True
        secondCardLow = True

    elif secondCard > firstCard:
        secondCardHigh = True
        firstCardLow = True


    if firstCardHigh and userLow:
        point += 1000000000

    elif firstCardLow and userHigh:
        point += 1000000000000000

    elif firstCardHigh and userHigh:
        point -= 100000000000

    elif firstCardLow and userLow:
        point -= 10000000

    elif secondCardHigh and userLow:
        point -= 1000

    elif secondCardLow and userHigh:
        point += 10000

    elif secondCardLow and userLow:
        point += 100000

    elif secondCardHigh and userHigh:
        point += 10
    else:
        print(point)



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

    if point <= 0:
        print("LOLst joe bills nibba]\n")
    if point >= 1:
        print("congratz, you paid yo debt\n")
    point = 0
