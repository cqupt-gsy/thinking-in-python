#!/usr/bin/python

__author__ = 'Mentu'

from comvar import PROCESSES
from comvar import ACTIONS
from comvar import POSITION


def parseProcessesmgs(rev_msg, pid, restplayer, hands):
    content = rev_msg.rstrip().split('\n')
    all_processes = []
    hand_cards = []
    inqueiry_info = []
    common_cards = []
    turn_cards = []
    river_cards = []
    seat_info = []
    result = []
    for index in range(len(content)):
        item = content[index].rstrip().split('/')
        if item[0] == PROCESSES[0]:
            all_processes.append(PROCESSES[0])
            begin = index + 1
            myposition = ''
            restplayers = 0
            mymoney = 0
            othersmoney = []
            for n in range(begin, len(content)):
                info = content[n].rstrip().split(' ')
                if info[0] == '/seat':
                    break
                restplayers += 1
                if info[0] == 'button:':
                    if info[1] == pid:
                        myposition = POSITION[0]
                        mymoney = int(info[2]) + int(info[3])
                    else:
                        other = int(info[2]) + int(info[3])
                        othersmoney.append(other)
                if info[0] == 'small':
                    if info[2] == pid:
                        myposition = POSITION[1]
                        mymoney = int(info[3]) + int(info[4])
                    else:
                        other = int(info[3]) + int(info[4])
                        othersmoney.append(other)
                if info[0] == 'big':
                    if info[2] == pid:
                        myposition = POSITION[2]
                        mymoney = int(info[3]) + int(info[4])
                    else:
                        other = int(info[3]) + int(info[4])
                        othersmoney.append(other)
                if info[0] == pid:
                    myposition = POSITION[3]
                    mymoney = int(info[1]) + int(info[2])
                if info[0] != pid and info[0] != 'button:' and info[0] != 'small' and info[0] != 'big':
                    other = int(info[1]) + int(info[2])
                    othersmoney.append(other)
            myrank = 1
            for others in othersmoney:
                if others >= mymoney:
                    myrank += 1
            othersmoney = sorted(othersmoney)
            baoshou = 'NO'
            if myrank == 1:
                if mymoney - (hands/restplayer)*60 + 4000 > othersmoney[0]:
                    baoshou = 'YES'
                else:
                    baoshou = 'NO'
            seat_info.append(restplayers)
            seat_info.append(myposition)
            seat_info.append(myrank)
            seat_info.append(baoshou)
        elif item[0] == PROCESSES[2]:
            all_processes.append(PROCESSES[2])
            hand_cards.append(content[index+1])
            hand_cards.append(content[index+2])
        elif item[0] == PROCESSES[3]:
            all_processes.append(PROCESSES[3])
            begin = index + 1
            actionedplayers = 0 #inquiry info players total number
            liveplayers = 0 #make action except fold
            blindplayers = 0 #check if this is the first inquiry info
            his_action = ''
            maxbet = 0
            mybet = 0
            for n in range(begin, len(content)):
                info = content[n].rstrip().split(' ')
                if info[0] == 'total':
                    break
                actionedplayers += 1
                if info[4] != ACTIONS[0] and info[4] != 'blind':
                    liveplayers += 1
                    if maxbet < int(info[3]):
                        maxbet = int(info[3])
                if info[4] == 'blind':
                    blindplayers += 1
                    if maxbet < int(info[3]):
                        maxbet = int(info[3])
                if info[0] == pid:
                    his_action = info[4]
                    mybet = int(info[3])
            if blindplayers > 0:#before flop, calculate rest of player numbers
                actionedplayers = actionedplayers - blindplayers - liveplayers
                leftplayers = restplayer - actionedplayers - 1  #rest players
            else:
                leftplayers = liveplayers - 1 #rest players
            mycallmoney = maxbet - mybet
            inqueiry_info.append(leftplayers)
            inqueiry_info.append(his_action)
            inqueiry_info.append(mycallmoney)
        elif item[0] == PROCESSES[4]:
            all_processes.append(PROCESSES[4])
            common_cards.append(content[index+1])
            common_cards.append(content[index+2])
            common_cards.append(content[index+3])
        elif item[0] == PROCESSES[5]:
            all_processes.append(PROCESSES[5])
            turn_cards.append(content[index+1])
        elif item[0] == PROCESSES[6]:
            all_processes.append(PROCESSES[6])
            river_cards.append(content[index+1])
        elif item[0] == PROCESSES[9]:
            all_processes.append(PROCESSES[9])
        else:
            continue
    result.append(all_processes)
    result.append(hand_cards)
    result.append(inqueiry_info)
    result.append(common_cards)
    result.append(turn_cards)
    result.append(river_cards)
    result.append(seat_info)
    return result
















