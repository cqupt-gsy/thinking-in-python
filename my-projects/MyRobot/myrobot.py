#!/usr/bin/python

__author__ = 'Mentu'


#import pairs situation before flop
from comvar import FIRSTPAIRS
from comvar import SECONDPAIRS
from comvar import THIRDPAIRS
from comvar import FOURTHPAIRS
from comvar import FIFTHPAIRS
from comvar import GOOD_COLORS
from comvar import POSITION

#import pairs situation at flop
from comvar import THREEZERO
from comvar import TWOONE
from comvar import HIGHPAIRS
from comvar import MIDDLEPAIRS
from comvar import FLOPSTRAIGHT

#import pairs situation at turn
from comvar import FOURZERO
from comvar import THREEONE
from comvar import TWOTWO
from comvar import TWOONEONE
from comvar import TURNSTRAIGHT

#import pairs situation at river
from comvar import FIVEZERO
from comvar import FOURONE
from comvar import THREETWO
from comvar import THREEONEONE
from comvar import TWOTWOONE
from comvar import TWOONEONEONE

#import pairs situation using by computer
from comvar import FOUR_OF_A_KIND
from comvar import FULL_HOUSE
from comvar import FLUSH
from comvar import STRAIGHT
from comvar import THREE_OF_A_KIND
from comvar import TWO_PAIR
from comvar import ONE_PAIR

#import all actions I can make
from comvar import ACTIONS

#import system module
from random import shuffle
from itertools import combinations

def genetercard(cards):
    '''
    parsing cards, card[color, point] => card['AS'], only use the first char in the card
    :param cards: the original cards
    :return: trasform cards
    '''
    final_cards = []
    for card in cards:
        content = card.rstrip().split(' ')
        color = content[0][0]
        point = content[1]
        if point == "10":
            rank = "T"
        else:
            rank = point
        final_cards.append(rank+color)
    return final_cards

def calFourKing(points):
    sorted_points = sorted(points)
    res = []
    counted = []
    for item in sorted_points:
        if item in counted:
            continue
        res.append(sorted_points.count(item))
        counted.append(item)
    com = sorted(res, reverse=True)
    com = com[0:2]
    return com in FOUR_OF_A_KIND

def calFullHouse(points):
    sorted_points = sorted(points)
    res = []
    counted = []
    for item in sorted_points:
        if item in counted:
            continue
        res.append(sorted_points.count(item))
        counted.append(item)
    com = sorted(res, reverse=True)
    com = com[0:2]
    return com in FULL_HOUSE

def calFlush(colors):
    sorted_colors = sorted(colors)
    res = []
    counted = []
    for item in sorted_colors:
        if item in counted:
            continue
        res.append(sorted_colors.count(item))
        counted.append(item)
    com = sorted(res, reverse=True)
    com = com[0:1]
    return com in FLUSH

def calStraight(points):
    if len(points) == 5:
        sorted_points = sorted(points)
        return sorted_points in STRAIGHT
    else:
        hands = [list(x) for x in combinations(points,5)]
        for hand in hands:
            sort = sorted(hand)
            if sort in STRAIGHT:
                return True
        return False

def calThreeKing(points):
    sorted_points = sorted(points)
    res = []
    counted = []
    for item in sorted_points:
        if item in counted:
            continue
        res.append(sorted_points.count(item))
        counted.append(item)
    com = sorted(res, reverse=True)
    com = com[0:2]
    return com == THREE_OF_A_KIND

def calTwoPairs(points):
    sorted_points = sorted(points)
    res = []
    counted = []
    for item in sorted_points:
        if item in counted:
            continue
        res.append(sorted_points.count(item))
        counted.append(item)
    com = sorted(res, reverse=True)
    com = com[0:2]
    return com == TWO_PAIR

def calOnePairs(points):
    sorted_points = sorted(points)
    res = []
    counted = []
    for item in sorted_points:
        if item in counted:
            continue
        res.append(sorted_points.count(item))
        counted.append(item)
    com = sorted(res, reverse=True)
    com = com[0:2]
    return com == ONE_PAIR

def calFlopCommoncards(points):
    sorted_points = sorted(points)
    res = []
    counted = []
    for item in sorted_points:
        if item in counted:
            continue
        res.append(sorted_points.count(item))
        counted.append(item)
    com = sorted(res, reverse=True)
    if com == THREEZERO:
        return 3
    elif com == TWOONE:
        return 2
    else:
        return 1

def calTurnCommonCards(points):
    sorted_points = sorted(points)
    res = []
    counted = []
    for item in sorted_points:
        if item in counted:
            continue
        res.append(sorted_points.count(item))
        counted.append(item)
    com = sorted(res, reverse=True)
    if com == FOURZERO:
        return 5
    elif com == THREEONE:
        return 4
    elif com == TWOTWO:
        return 3
    elif com == TWOONEONE:
        return 2
    else:
        return 1

def calRiverCommoncards(points):
    sorted_points = sorted(points)
    res = []
    counted = []
    for item in sorted_points:
        if item in counted:
            continue
        res.append(sorted_points.count(item))
        counted.append(item)
    com = sorted(res, reverse=True)
    if com == FIVEZERO:
        return 7
    elif com == FOURONE:
        return 6
    elif com == THREETWO:
        return 5
    elif com == THREEONEONE:
        return 4
    elif com == TWOTWOONE:
        return 3
    elif com == TWOONEONEONE:
        return 2
    else:
        return 1

def compareHandandCommon(handcardpoints, commoncardpoins):
    temphand = sorted(handcardpoints, reverse=True)
    commons = [list(x) for x in combinations(commoncardpoins, 2)]
    for common in commons:
        if temphand == max([temphand, common]):
            return True
    return False

def compareHandandCommonTurn(handcardpoints, commoncardpoins):
    temphand = sorted(handcardpoints, reverse=True)
    commons = [list(x) for x in combinations(commoncardpoins, 2)]
    mywin = False
    for common in commons:
        if temphand == max([temphand, common]):
            mywin = True
        else:
            mywin = False
    return mywin

def calThreeStraight(points):
    commons = [list(x) for x in combinations(points, 3)]
    for hand in commons:
        sort = sorted(hand)
        if sort in FLOPSTRAIGHT:
            return True
    return False

def calFourStraight(points):
    commons = [list(x) for x in combinations(points, 4)]
    for hand in commons:
        sort = sorted(hand)
        if sort in TURNSTRAIGHT:
            return True
    return False

def calFlushTing(colors):
    sorted_points = sorted(colors)
    res = []
    counted = []
    for item in sorted_points:
        if item in counted:
            continue
        res.append(sorted_points.count(item))
        counted.append(item)
    com = sorted(res, reverse=True)
    if com == FOURONE:
        return True
    else:
        return False

def calStraightTing(points):
    commons = [list(x) for x in combinations(points, 4)]
    for hand in commons:
        sort = sorted(hand)
        handnumber = []
        for sorthand in sort:
            if sorthand == 'A':
                handnumber.append(14)
            elif sorthand == 'K':
                handnumber.append(13)
            elif sorthand == 'Q':
                handnumber.append(12)
            elif sorthand == 'J':
                handnumber.append(11)
            elif sorthand == 'T':
                handnumber.append(10)
            else:
                handnumber.append(int(sorthand))
        sortedagain = sorted(handnumber)
        first = int(sortedagain[0])
        second = int(sortedagain[1])
        third = int(sortedagain[2])
        fourth = int(sortedagain[3])
        if fourth - first == 3 or fourth - first == 4:
            firstresult = second - first
            secondresult = third - second
            thirdresult = fourth - third
            if firstresult != 0 and secondresult != 0 and thirdresult != 0:
                return True
    return False

def makeActionBeforeFlop_1(players, handcard, position, mybet):
    '''
    make decision before flop  [jijin]
    :param players: the rest players number
    :param handcard: cards in my hand
    :return: my action
    '''
    #not get the handcard message
    if len(handcard) == 0:
        if mybet == 0:
            return ACTIONS[2]
        else:
            return ACTIONS[0]
    #calculate my desicion
    points = handcard[0][0] + handcard[1][0]
    colors = handcard[0][1] + handcard[1][1]
    if points in FIRSTPAIRS:#-----------------------------------------------------first----------------------------------------
        if position == POSITION[3]:#bad position
            if players > 3: #4,5,6,7people left
                if mybet <= 160:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#3 people left
                if mybet <= 40:
                    return ACTIONS[4]
                elif 240 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        elif position == POSITION[0]:#button position
            if players > 5: #6,7people left
                if mybet == 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            elif 5 >= players > 2: #3,4,5people left
                if mybet == 40:
                    return ACTIONS[4]
                elif 240 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#2 people left
                if mybet <= 40:
                    return ACTIONS[4]
                elif 320 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        else: #small blind position and big blind position
            if players > 5: #6,7people left
                if mybet <= 20:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            elif 5 >= players > 2: #3,4,5people left
                if mybet <= 20:
                    return ACTIONS[4]
                elif 240 >= mybet > 20:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#1,2 people left
                if mybet <= 20:
                    return ACTIONS[4]
                else:
                    if 320 >= mybet > 20:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
    elif points in SECONDPAIRS:#-----------------------------------------------------second----------------------------------------
        if position == POSITION[3]:#bad position
            if players > 3: #4,5,6,7people left
                if colors in GOOD_COLORS:
                    if mybet <= 160:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:
                    if mybet == 40:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
            else:#3 people left
                if mybet <= 40:
                    return ACTIONS[4]
                elif 200 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        elif position == POSITION[0]:#button position
            if players > 5: #6,7people left
                if mybet == 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            elif 5 >= players > 2: #3,4,5people left
                if mybet == 40:
                    return ACTIONS[4]
                elif 200 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#2 people left
                if mybet <= 40:
                    return ACTIONS[4]
                elif 280 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        else: #small blind position and big blind position
            if players > 5: #6,7people left
                if mybet <= 20:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            elif 5 >= players > 2: #3,4,5people left
                if mybet <= 20:
                    return ACTIONS[4]
                elif 200 >= mybet > 20:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#1,2 people left
                if mybet <= 20:
                    return ACTIONS[4]
                else:
                    if 280 >= mybet > 20:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
    elif points in THIRDPAIRS:#-----------------------------------------------------third----------------------------------------
        if position == POSITION[3]:#bad position
            if players > 3: #4,5,6,7people left
                return ACTIONS[0]
            else:#3 people left
                if 160 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        elif position == POSITION[0]:#button position
            if players > 4: #5,6,7people left
                if mybet == 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            elif 4 >= players > 2: #3,4people left
                if mybet <= 160:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#2 people left
                if mybet <= 40:
                    return ACTIONS[5]
                else:
                    if 240 >= mybet > 40:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else: #small blind position and big blind position
            if players > 4: #5,6,7people left
                if mybet <= 20:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            elif 4 >= players > 2: #2,3,4people left
                if mybet <= 160:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#1,2 people left
                if mybet <= 20:
                    return ACTIONS[5]
                else:
                    if 240 >= mybet > 20:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
    elif points in FOURTHPAIRS:#-----------------------------------------------------fourth----------------------------------------
        if colors in GOOD_COLORS:
            if position == POSITION[3]:#bad position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                else:#3 people left
                    if 160 >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
            elif position == POSITION[0]:#button position
                if players > 4: #5,6,7people left
                    if mybet == 40:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                elif 4 >= players > 2: #3,4people left
                    if mybet <= 160:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:#2 people left
                    if mybet <= 40:
                        return ACTIONS[5]
                    else:
                        if 240 >= mybet > 40:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
            else: #small blind position and big blind position
                if players > 4: #5,6,7people left
                    if mybet <= 20:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                elif 4 >= players > 2: #2,3,4people left
                    if mybet <= 160:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:#1 people left
                    if mybet <= 20:
                        return ACTIONS[5]
                    else:
                        if 240 >= mybet > 20:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
        else:
            if position == POSITION[3]:#bad position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                else:#3 people left
                    if 120 >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
            elif position == POSITION[0]:#button position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                elif players == 3: #3people left
                    if mybet <= 120:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:#2 people left
                    if mybet <= 40:
                        return ACTIONS[5]
                    else:
                        if 200 >= mybet > 40:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
            else: #small blind position and big blind position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                elif 3 >= players > 1: #2,3people left
                    if mybet <= 120:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:#1 people left
                    if mybet <= 20:
                        return ACTIONS[5]
                    else:
                        if 200 >= mybet > 20:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
    elif points in FIFTHPAIRS:#-----------------------------------------------------fifth----------------------------------------
        if colors in GOOD_COLORS:
            if position == POSITION[3]:#bad position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                else:#3 people left
                    if 120 >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
            elif position == POSITION[0]:#button position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                elif players == 3: #3people left
                    if mybet <= 120:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:#2 people left
                    if mybet <= 40:
                        return ACTIONS[5]
                    else:
                        if 200 >= mybet > 40:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
            else: #small blind position and big blind position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                elif 3 >= players > 1: #2,3people left
                    if mybet <= 120:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:#1 people left
                    if mybet <= 20:
                        return ACTIONS[5]
                    else:
                        if 200 >= mybet > 20:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
        else:
            if position == POSITION[3]:#bad position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                else:#3 people left
                    if 80 >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
            elif position == POSITION[0]:#button position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                elif 3 >= players > 1: #2,3people left
                    if mybet <= 80:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:#2 people left
                    if mybet <= 40:
                        return ACTIONS[5]
                    else:
                        if 160 >= mybet > 40:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
            else: #small blind position and big blind position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                elif 3 >= players > 1: #2,3people left
                    if mybet <= 80:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:#1 people left
                    if mybet <= 20:
                        return ACTIONS[5]
                    else:
                        if 160 >= mybet > 20:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
    else:#-----------------------------------------------------seventh----------------------------------------
        if position == POSITION[3]:#bad position
            if players > 3: #4,5,6,7people left
                return ACTIONS[0]
            else:#3 people left
                if 40 >= mybet > 0:
                    return ACTIONS[5]#need to be fix????????????????????????????????????????
                else:
                    return ACTIONS[0]
        elif position == POSITION[0]:#button position
            if players > 2: #3,4,5,6,7people left
                return ACTIONS[0]
            else:#2 people left
                if mybet <= 40:
                    return ACTIONS[5]
                else:
                    if 120 >= mybet > 40:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else: #small blind position and big blind position
            if players > 1: #2,3,4,5,6,7people left
                return ACTIONS[0]
            else:#1 people left
                if mybet <= 20:
                    return ACTIONS[5]
                else:
                    if 120 >= mybet > 40:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]

def makeActionBeforeFlop_2(players, handcard, position, mybet):
    '''
    make decision before flop [baoshou]
    :param players: the rest players number
    :param handcard: cards in my hand
    :return: my action
    '''
    #not get the handcard message
    if len(handcard) == 0:
        if mybet == 0:
            return ACTIONS[2]
        else:
            return ACTIONS[0]
    #calculate my desicion
    points = handcard[0][0] + handcard[1][0]
    colors = handcard[0][1] + handcard[1][1]
    if points in FIRSTPAIRS:#-----------------------------------------------------first----------------------------------------
        if position == POSITION[3]:#bad position
            if players > 3: #4,5,6,7people left
                if mybet <= 160:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#3 people left
                if mybet <= 40:
                    return ACTIONS[4]
                elif 240 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        elif position == POSITION[0]:#button position
            if players > 5: #6,7people left
                return ACTIONS[0]
            elif 5 >= players > 2: #3,4,5people left
                if mybet == 40:
                    return ACTIONS[4]
                elif 240 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#2 people left
                if mybet <= 40:
                    return ACTIONS[4]
                elif 320 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        else: #small blind position and big blind position
            if players > 5: #6,7people left
                return ACTIONS[0]
            elif 5 >= players > 2: #2,3,4,5people left
                if mybet <= 20:
                    return ACTIONS[4]
                elif 240 >= mybet > 20:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#1 people left
                if mybet <= 20:
                    return ACTIONS[4]
                else:
                    if 320 >= mybet > 20:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
    elif points in SECONDPAIRS:#-----------------------------------------------------second----------------------------------------
        if position == POSITION[3]:#bad position
            if players > 3: #4,5,6,7people left
                if mybet <= 80:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#3 people left
                if mybet <= 40:
                    return ACTIONS[4]
                elif 200 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        elif position == POSITION[0]:#button position
            if players > 5: #6,7people left
                return ACTIONS[0]
            elif 5 >= players > 2: #3,4,5people left
                if mybet <= 200:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#2 people left
                if mybet <= 40:
                    return ACTIONS[4]
                elif 280 >= mybet > 40:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        else: #small blind position and big blind position
            if players > 5: #6,7people left
                return ACTIONS[0]
            elif 5 >= players > 2: #2,3,4,5people left
                if mybet <= 200:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:#1 people left
                if mybet <= 20:
                    return ACTIONS[4]
                else:
                    if 280 >= mybet > 20:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
    elif points in THIRDPAIRS:#-----------------------------------------------------third----------------------------------------
        if position == POSITION[3]:#bad position
            return ACTIONS[0]
        elif position == POSITION[0]:#button position
            if players > 3: #4,5,6,7people left
                return ACTIONS[0]
            else:#2 people left
                if mybet <= 40:
                    return ACTIONS[5]
                else:
                    if 80 >= mybet > 40:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else: #small blind position and big blind position
            if players > 2: #4,5,6,7people left
                return ACTIONS[0]
            else:#1 people left
                if mybet <= 20:
                    return ACTIONS[5]
                else:
                    if 80 >= mybet > 20:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
    elif points in FOURTHPAIRS:#-----------------------------------------------------fourth----------------------------------------
        if colors in GOOD_COLORS:
            if position == POSITION[3]:#bad position
                return ACTIONS[0]
            elif position == POSITION[0]:#button position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                else:#2 people left
                    if mybet <= 40:
                        return ACTIONS[5]
                    else:
                        if 80 >= mybet > 40:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
            else: #small blind position and big blind position
                if players > 2: #4,5,6,7people left
                    return ACTIONS[0]
                else:#1 people left
                    if mybet <= 20:
                        return ACTIONS[5]
                    else:
                        if 80 >= mybet > 20:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
        else:
            if position == POSITION[3]:#bad position
                return ACTIONS[0]
            elif position == POSITION[0]:#button position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                else:#2 people left
                    if mybet <= 40:
                        return ACTIONS[4]
                    else:
                        return ACTIONS[0]
            else: #small blind position and big blind position
                if players > 2: #4,5,6,7people left
                    return ACTIONS[0]
                else:#1 people left
                    if mybet <= 20:
                        return ACTIONS[4]
                    else:
                        return ACTIONS[0]
    elif points in FIFTHPAIRS:#-----------------------------------------------------fifth----------------------------------------
        if colors in GOOD_COLORS:
            if position == POSITION[3]:#bad position
                return ACTIONS[0]
            elif position == POSITION[0]:#button position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                else:#2 people left
                    if mybet <= 40:
                        return ACTIONS[4]
                    else:
                        return ACTIONS[0]
            else: #small blind position and big blind position
                if players > 2: #4,5,6,7people left
                    return ACTIONS[0]
                else:#1 people left
                    if mybet <= 20:
                        return ACTIONS[4]
                    else:
                        return ACTIONS[0]
        else:
            if position == POSITION[3]:#bad position
                return ACTIONS[0]
            elif position == POSITION[0]:#button position
                if players > 3: #4,5,6,7people left
                    return ACTIONS[0]
                else:#2 people left
                    if mybet <= 40:
                        return ACTIONS[4]
                    else:
                        return ACTIONS[0]
            else: #small blind position and big blind position
                if players > 2: #4,5,6,7people left
                    return ACTIONS[0]
                else:#1 people left
                    if mybet <= 20:
                        return ACTIONS[4]
                    else:
                        return ACTIONS[0]
    else:#-----------------------------------------------------seventh----------------------------------------
        if position == POSITION[3]:#bad position
            return ACTIONS[0]
        elif position == POSITION[0]:#button position
            if players > 1: #3,4,5,6,7people left
                return ACTIONS[0]
            else:#2 people left
                if mybet <= 40:
                    return ACTIONS[4]
                else:
                    return ACTIONS[0]
        else: #small blind position and big blind position
            if players > 1: #2,3,4,5,6,7people left
                return ACTIONS[0]
            else:#1 people left
                if mybet <= 20:
                    return ACTIONS[4]
                else:
                    return ACTIONS[0]

def makeActionAfterFlop(players, handcards, commoncards, mybet):
    #not get the commoncards message
    if len(commoncards) == 0:
        if mybet == 0:
            return ACTIONS[2]
        else:
            return ACTIONS[0]
    #calculate my desicion
    if len(commoncards) == 3:
        action = makeActionatFlop(players, handcards, commoncards, mybet)
    elif len(commoncards) == 4:
        action = makeActionatTurn(players, handcards, commoncards, mybet)
    else:
        action = makeActionatRiver(players, handcards, commoncards, mybet)
    return action


def makeActionatFlop(players, handcards, commoncards, mybet, minplayers=3, scaremoney=360):
    allcardpoints = handcards[0][0] + handcards[1][0] + commoncards[0][0] + commoncards[1][0] + commoncards[2][0]
    allcardcolors = handcards[0][1] + handcards[1][1] + commoncards[0][1] + commoncards[1][1] + commoncards[2][1]
    handcardpoints = handcards[0][0] + handcards[1][0]
    commoncardpoints = commoncards[0][0] + commoncards[1][0] + commoncards[2][0]
    commoncardcolors = commoncards[0][1] + commoncards[1][1] + commoncards[2][1]
    straight = calStraight(allcardpoints)
    flush = calFlush(allcardcolors)
    fourking = calFourKing(allcardpoints)
    fullhouse = calFullHouse(allcardpoints)
    threeking = calThreeKing(allcardpoints)
    twopairs = calTwoPairs(allcardpoints)
    onepairs = calOnePairs(allcardpoints)
    if straight and flush:
        if mybet == 0:
            return ACTIONS[1]
        else:
            return ACTIONS[8]
    elif fourking:
        if mybet == 0:
            return ACTIONS[1]
        else:
            return ACTIONS[8]
    elif fullhouse:
        situation = calFlopCommoncards(commoncardpoints)
        if situation == 3:
            if handcardpoints in HIGHPAIRS:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[8]
                    else:
                        return ACTIONS[2]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[1]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[8]
                else:
                    return ACTIONS[2]
    elif flush:
        if 'A' in handcardpoints or 'K' in handcardpoints or 'Q' in handcardpoints:
            if mybet == 0:
                return ACTIONS[1]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[8]
                else:
                    return ACTIONS[2]
        else:
            if mybet == 0:
                return ACTIONS[6]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
    elif straight:
        situation = calFlopCommoncards(commoncardcolors)
        if situation == 3:
            if players > minplayers:
                if 240 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else:
            temppoints = sorted(commoncardpoints)
            if temppoints in FLOPSTRAIGHT:
                if compareHandandCommon(handcardpoints, commoncardpoints):
                    if mybet == 0:
                        return ACTIONS[1]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[8]
                        else:
                            return ACTIONS[2]
                else:
                    if mybet == 0:
                        return ACTIONS[6]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[8]
                    else:
                        return ACTIONS[2]
    elif threeking:
        situation = calFlopCommoncards(commoncardpoints)
        if situation == 3:
            if players > minplayers:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if mybet <= 120:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        elif situation == 2:
            if mybet == 0:
                return ACTIONS[6]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        else:
            tempcolors = calFlopCommoncards(commoncardcolors)
            temppoints = sorted(commoncardpoints)
            if tempcolors == 3 or temppoints in FLOPSTRAIGHT:
                if players > minplayers:
                    if mybet == 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:
                    if mybet == 0:
                        return ACTIONS[6]
                    else:
                        if 200 >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
            else:
                if handcardpoints in HIGHPAIRS:
                    if mybet == 0:
                        return ACTIONS[1]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[8]
                        else:
                            return ACTIONS[2]
                else:
                    if mybet == 0:
                        return ACTIONS[6]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
    elif twopairs:
        if players > minplayers:
            if mybet == 0:
                return ACTIONS[1]
            else:
                return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[6]
            else:
                if 140 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
    elif onepairs:
        if players > minplayers:
            if mybet == 0:
                return ACTIONS[1]
            else:
                return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[6]
            else:
                if 100 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
    else:
        flushT = calFlushTing(allcardcolors)
        straightT = calStraightTing(allcardpoints)
        if flushT and straightT:
            if players > minplayers:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if 160 >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        elif flushT:
            if players > minplayers:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if 140 >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        elif straightT:
            if players > minplayers:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if 100 >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else:
            if players > minplayers:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    return ACTIONS[0]

def makeActionatTurn(players, handcards, commoncards, mybet, minplayers=3, scaremoney=360):
    allcardpoints = handcards[0][0] + handcards[1][0] + commoncards[0][0] + commoncards[1][0] + commoncards[2][0] + commoncards[3][0]
    allcardcolors = handcards[0][1] + handcards[1][1] + commoncards[0][1] + commoncards[1][1] + commoncards[2][1] + commoncards[3][1]
    handcardpoints = handcards[0][0] + handcards[1][0]
    commoncardpoints = commoncards[0][0] + commoncards[1][0] + commoncards[2][0] + commoncards[3][0]
    commoncardcolors = commoncards[0][1] + commoncards[1][1] + commoncards[2][1] + commoncards[3][1]
    straight = calStraight(allcardpoints)
    flush = calFlush(allcardcolors)
    fourking = calFourKing(allcardpoints)
    fullhouse = calFullHouse(allcardpoints)
    threeking = calThreeKing(allcardpoints)
    twopairs = calTwoPairs(allcardpoints)
    onepairs = calOnePairs(allcardpoints)
    if straight and flush:
        temppoints = sorted(commoncardpoints)
        three = calThreeStraight(commoncardpoints)
        if temppoints in TURNSTRAIGHT or three:
            if compareHandandCommon(handcardpoints, commoncardpoints):
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[8]
                    else:
                        return ACTIONS[2]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[1]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[8]
                else:
                    return ACTIONS[2]
    elif fourking:
        situation = calTurnCommonCards(commoncardpoints)
        if situation == 5:
            if 'A' in handcardpoints or 'K' in handcardpoints or 'Q' in handcardpoints:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[8]
                    else:
                        return ACTIONS[2]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        elif situation == 4:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[8]
                    else:
                        return ACTIONS[2]
        elif situation == 3:
            if 'AA' == handcardpoints:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[8]
                    else:
                        return ACTIONS[2]
            else:
                if compareHandandCommonTurn(handcardpoints, commoncardpoints):
                    if mybet == 0:
                        return ACTIONS[1]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[8]
                        else:
                            return ACTIONS[2]
                else:
                    if mybet == 0:
                        return ACTIONS[6]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[1]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[8]
                else:
                    return ACTIONS[2]
    elif fullhouse:
        situation = calTurnCommonCards(commoncardpoints)
        if situation == 4:
            if handcardpoints in HIGHPAIRS:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[8]
                    else:
                        return ACTIONS[2]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        elif situation == 3:
            if 'A' in handcardpoints or 'K' in handcardpoints or 'Q' in handcardpoints:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[8]
                    else:
                        return ACTIONS[2]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[1]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[8]
                else:
                    return ACTIONS[2]
    elif flush:
        if 'A' in handcardpoints or 'K' in handcardpoints or 'Q' in handcardpoints:
            if mybet == 0:
                return ACTIONS[1]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[8]
                else:
                    return ACTIONS[2]
        else:
            if mybet == 0:
                return ACTIONS[6]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
    elif straight:
        situation = calTurnCommonCards(commoncardcolors)
        if situation == 5 or situation == 4:
            if players > minplayers:
                if 240 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else:
            temppoints = sorted(commoncardpoints)
            three = calThreeStraight(commoncardpoints)
            if temppoints in TURNSTRAIGHT or three:
                if compareHandandCommon(handcardpoints, commoncardpoints):
                    if mybet == 0:
                        return ACTIONS[1]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[8]
                        else:
                            return ACTIONS[2]
                else:
                    if mybet == 0:
                        return ACTIONS[6]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[8]
                    else:
                        return ACTIONS[2]
    elif threeking:
        situation = calTurnCommonCards(commoncardpoints)
        if situation == 4:
            if players > minplayers:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if mybet <= 200:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        elif situation == 2:
            if mybet == 0:
                return ACTIONS[6]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        else:
            tempcolors = calTurnCommonCards(commoncardcolors)
            three = calThreeStraight(commoncardpoints)
            temppoints = sorted(commoncardpoints)
            if tempcolors == 5 or temppoints in TURNSTRAIGHT or three:
                if players > minplayers:
                    if mybet == 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:
                    if mybet == 0:
                        return ACTIONS[1]
                    else:
                        if 200 >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
    elif twopairs:
        if players > minplayers:
            if mybet == 0:
                return ACTIONS[1]
            else:
                return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[1]
            else:
                if 140 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
    elif onepairs:
        if players > minplayers:
            if mybet == 0:
                return ACTIONS[1]
            else:
                return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[1]
            else:
                if 100 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
    else:
        if players > minplayers:
            if mybet == 0:
                return ACTIONS[1]
            else:
                return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[1]
            else:
                return ACTIONS[0]


def makeActionatRiver(players, handcards, commoncards, mybet, minplayers=3, scaremoney=360):
    allcardpoints = handcards[0][0] + handcards[1][0] + commoncards[0][0] + commoncards[1][0] + commoncards[2][0] + commoncards[3][0] + commoncards[4][0]
    allcardcolors = handcards[0][1] + handcards[1][1] + commoncards[0][1] + commoncards[1][1] + commoncards[2][1] + commoncards[3][1] + commoncards[4][1]
    handcardpoints = handcards[0][0] + handcards[1][0]
    commoncardpoints = commoncards[0][0] + commoncards[1][0] + commoncards[2][0] + commoncards[3][0] + commoncards[4][0]
    commoncardcolors = commoncards[0][1] + commoncards[1][1] + commoncards[2][1] + commoncards[3][1] + commoncards[4][1]
    straight = calStraight(allcardpoints)
    flush = calFlush(allcardcolors)
    fourking = calFourKing(allcardpoints)
    fullhouse = calFullHouse(allcardpoints)
    threeking = calThreeKing(allcardpoints)
    twopairs = calTwoPairs(allcardpoints)
    onepairs = calOnePairs(allcardpoints)
    if straight and flush:
        temppoints = sorted(commoncardpoints)
        three = calThreeStraight(commoncardpoints)
        four = calFourStraight(commoncardpoints)
        if temppoints in STRAIGHT or three or four:
            if compareHandandCommon(handcardpoints, commoncardpoints):
                return ACTIONS[8]
            else:
                if mybet == 0:
                    if restplayser <= 4 and baoshou == 'NO':
                        return ACTIONS[7]
                    else:
                        return ACTIONS[6]
                else:
                    return ACTIONS[2]
        else:
            return ACTIONS[8]
    elif fourking:
        situation = calRiverCommoncards(commoncardpoints)
        if situation == 6:
            if 'A' in handcardpoints or 'K' in handcardpoints or 'Q' in handcardpoints:
                return ACTIONS[8]
            else:
                if players > minplayers:
                    if 240 >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:
                    if mybet == 0:
                        return ACTIONS[6]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
        elif situation == 5:
            if handcardpoints in HIGHPAIRS or 'A' in handcardpoints or 'K' in handcardpoints or 'Q' in handcardpoints:
                return ACTIONS[8]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        elif situation == 4:
            return ACTIONS[8]
        elif situation == 3:
            if handcardpoints in HIGHPAIRS:
                return ACTIONS[8]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else:
            return ACTIONS[8]
    elif fullhouse:
        situation = calRiverCommoncards(commoncardpoints)
        if situation == 5:
            if handcardpoints in HIGHPAIRS:
                return ACTIONS[8]
            else:
                if players > minplayers:
                    if 240 >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:
                    if mybet == 0:
                        return ACTIONS[6]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
        elif situation == 4 or situation == 3:
            if handcardpoints in HIGHPAIRS or 'A' in handcardpoints or 'K' in handcardpoints or 'Q' in handcardpoints:
                return ACTIONS[8]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else:
            return ACTIONS[8]
    elif flush:
        situation = calRiverCommoncards(commoncardcolors)
        if situation == 7 or situation == 6:
            if players > minplayers:
                if 240 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else:
            if 'A' in handcardpoints or 'K' in handcardpoints or 'Q' in handcardpoints:
                return ACTIONS[8]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
    elif straight:
        situation = calRiverCommoncards(commoncardcolors)
        if situation == 6 or situation == 5 or situation == 4:
            if players > minplayers:
                if 200 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[6]
                else:
                    if scaremoney >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        else:
            temppoints = sorted(commoncardpoints)
            three = calThreeStraight(commoncardpoints)
            four = calFourStraight(commoncardpoints)
            if temppoints in STRAIGHT or three or four:
                if compareHandandCommon(handcardpoints, commoncardpoints):
                    return ACTIONS[8]
                else:
                    if players > minplayers:
                        if 200 >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
                    else:
                        if mybet == 0:
                            return ACTIONS[6]
                        else:
                            if scaremoney >= mybet > 0:
                                return ACTIONS[2]
                            else:
                                return ACTIONS[0]
            else:
                return ACTIONS[8]
    elif threeking:
        situation = calRiverCommoncards(commoncardpoints)
        if situation == 4:
            if players > minplayers:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    return ACTIONS[0]
            else:
                if mybet == 0:
                    return ACTIONS[1]
                else:
                    if 200 >= mybet > 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
        elif situation == 2:
            if mybet == 0:
                return ACTIONS[6]
            else:
                if scaremoney >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
        else:
            tempcolors = calRiverCommoncards(commoncardcolors)
            three = calThreeStraight(commoncardpoints)
            four = calFourStraight(commoncardpoints)
            if tempcolors == 6 or tempcolors== 5 or tempcolors == 4 or three or four:
                if players > minplayers:
                    if mybet == 0:
                        return ACTIONS[2]
                    else:
                        return ACTIONS[0]
                else:
                    if mybet == 0:
                        return ACTIONS[1]
                    else:
                        if 200 >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
            else:
                if handcardpoints in HIGHPAIRS:
                    return ACTIONS[6]
                else:
                    if mybet == 0:
                        return ACTIONS[6]
                    else:
                        if scaremoney >= mybet > 0:
                            return ACTIONS[2]
                        else:
                            return ACTIONS[0]
    elif twopairs:
        if players > minplayers:
            if mybet == 0:
                return ACTIONS[1]
            else:
                return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[6]
            else:
                if 140 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
    elif onepairs:
        if players > minplayers:
            if mybet == 0:
                return ACTIONS[1]
            else:
                return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[6]
            else:
                if 100 >= mybet > 0:
                    return ACTIONS[2]
                else:
                    return ACTIONS[0]
    else:
        if players > minplayers:
            if mybet == 0:
                return ACTIONS[1]
            else:
                return ACTIONS[0]
        else:
            if mybet == 0:
                return ACTIONS[6]
            else:
                return ACTIONS[0]


