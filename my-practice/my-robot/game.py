#!/usr/bin/python
__author__ = 'Mentu'

#import my module
from myrobot import genetercard
from myrobot import makeActionBeforeFlop_1
from myrobot import makeActionBeforeFlop_2
from myrobot import makeActionAfterFlop
from myparser import parseProcessesmgs
from comvar import PROCESSES
from comvar import ACTIONS
from comvar import FIRSTPAIRS
from comvar import SECONDPAIRS
from comvar import THIRDPAIRS
from comvar import FOURTHPAIRS
from comvar import FIFTHPAIRS

#import system module
from socket import *
import sys
import gc


def mainflows():
    if len(sys.argv) < 6:
        print('Please run as ./game serverIP serverPort clientIP clientPort pid')
        print('for example: ./game 192.168.0.1 1024 192.168.0.2 2048 6001')
        return
    #connect to server
    serverIP, serverPort, clientIP, clientPort, pid = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
    name = 'FoZuBaoYou'
    socketobj = socket(AF_INET, SOCK_STREAM)
    socketobj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    socketobj.bind((clientIP, int(clientPort)))
    while True:
        try:
            socketobj.connect((serverIP, int(serverPort)))
        except error:
            continue
        break
    reg_msg = 'reg: %s %s \n' % (pid, name)
    socketobj.send(reg_msg.encode())
    #initial my globle info
    HAND_CARDS = []
    COMMON_CARDS = []
    HIS_ACTIONS = []
    MYPOSITION = 'bad' #my position in the game
    RESTPLAYERS = 8 #the rest players
    MYRANK = 8
    BAOSHOU = 'NO'
    HANDS = 0 #the round number
    GAME_OVER = False
    #main process
    while not GAME_OVER:
        temp = socketobj.recv(4096)
        rev_msg = temp.decode()
        all_result = parseProcessesmgs(rev_msg, pid, RESTPLAYERS, HANDS)
        processes = all_result[0]
        if PROCESSES[0] in processes:
            #seat message handle, clean the globle info
            HANDS += 1
            HAND_CARDS = []
            COMMON_CARDS = []
            HIS_ACTIONS = []
            gc.collect()
            seat_info = all_result[6]
            RESTPLAYERS = int(seat_info[0])
            MYPOSITION = seat_info[1]
            MYRANK = int(seat_info[2])
            BAOSHOU = seat_info[3]
        if PROCESSES[2] in processes:
            #hold message handle, clean the globle info
            COMMON_CARDS = []
            HIS_ACTIONS = []
            #setting my hand cards
            cards = all_result[1]
            realhandcard = genetercard(cards)
            HAND_CARDS = realhandcard[:]
        if PROCESSES[3] in processes:
            #inquire message handle, load the initial the players number and my history action
            inquire_info = all_result[2]
            playernum = int(inquire_info[0])
            his_action = inquire_info[1]
            mycallmoney = int(inquire_info[2])
            if his_action is not '':
                HIS_ACTIONS.append(his_action)
            #if my action is fold or all_in, continue
            if ACTIONS[0] in HIS_ACTIONS or ACTIONS[10] in HIS_ACTIONS:
                continue
            if MYRANK > 2 and RESTPLAYERS <= 4:
                points = HAND_CARDS[0][0] + HAND_CARDS[1][0]
                if points in FIRSTPAIRS or points in SECONDPAIRS or points in THIRDPAIRS or points in FIFTHPAIRS or points in FOURTHPAIRS:
                    if HIS_ACTIONS.count(ACTIONS[3]) < 4:
                        sendmsg = '%s \n' % ACTIONS[6]
                        socketobj.sendall(sendmsg.encode())
                        continue
                    else:
                        sendmsg = '%s \n' % ACTIONS[2]
                        socketobj.sendall(sendmsg.encode())
                        continue
                else:
                    if mycallmoney == 0:
                        sendmsg = '%s \n' % ACTIONS[2]
                        socketobj.sendall(sendmsg.encode())
                        continue
                    else:
                        sendmsg = '%s \n' % ACTIONS[0]
                        socketobj.sendall(sendmsg.encode())
                        continue
            #make action before flop
            handround = len(COMMON_CARDS)
            if  handround < 3:
                if BAOSHOU == 'NO':
                    action = makeActionBeforeFlop_1(playernum, HAND_CARDS, MYPOSITION, mycallmoney)#jijin
                else:
                    action = makeActionBeforeFlop_2(playernum, HAND_CARDS, MYPOSITION, mycallmoney)#baoshou
            else:#make action after flop
                action = makeActionAfterFlop(playernum, HAND_CARDS, COMMON_CARDS, mycallmoney)
            content = action.split(' ')
            if HIS_ACTIONS.count(ACTIONS[3]) >= 2 and content[0] == ACTIONS[3]:
                action = ACTIONS[2]
            #send my action to server
            sendmsg = '%s \n' % action
            socketobj.sendall(sendmsg.encode())
        if PROCESSES[4] in processes:
            #flop message handle, clean the history action
            HIS_ACTIONS = []
            common_cards = all_result[3]
            temp_common = genetercard(common_cards)
            COMMON_CARDS = temp_common[:]
        if PROCESSES[5] in processes:
            #turn message handle, clean the history action
            HIS_ACTIONS = []
            turn_cards = all_result[4]
            temp_turn = genetercard(turn_cards)
            COMMON_CARDS += temp_turn
        if PROCESSES[6] in processes:
            #river message handle, clean the history action
            HIS_ACTIONS = []
            river_cards = all_result[5]
            temp_river = genetercard(river_cards)
            COMMON_CARDS += temp_river
        if PROCESSES[9] in processes:
            #gameover message handle, clean the history action
            GAME_OVER = True
    socketobj.close()


if __name__ == '__main__':
    mainflows()








