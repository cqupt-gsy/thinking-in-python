__author__ = 'Mentu'

#var using by human before flop
FIRSTPAIRS = ('AA', 'KK') #raise
SECONDPAIRS = ('AK', 'KA', 'AQ', 'QA', 'AJ', 'JA', 'AT', 'TA', 'QQ', 'JJ') #if flush raise else call
THIRDPAIRS = ( 'TT','99', '88', '77', '66') #call
FOURTHPAIRS = ('A6', '6A', 'A7', '7A', 'A8', '8A', 'A9', '9A', 'A2', '2A', 'A3', '3A', 'A4', '4A', 'A5', '5A',
               'KQ', 'QK', 'KJ', 'JK', 'KT', 'TK', '9K', 'K9',
               'QJ', 'JQ',  'QT', 'TQ', 'Q9', '9Q', '9J', 'J9', 'TJ', 'JT') # if flush call else check
FIFTHPAIRS = ('Q8', '8Q', '7J', 'J7', '8J', 'J8',
              'K6', '6K', 'K7', '7K', 'K8', '8K', 'K5', '5K',
              'Q6', '6Q', 'Q5', '5Q', 'J6', '6J', 'T9', '9T', '98', '89', '78', '87', '67', '76','55', '44', '33', '22') #if flush check else fold
GOOD_COLORS = ('SS', 'HH', 'CC', 'DD')



#var using by human at flop
THREEZERO = [3]
TWOONE = [2,1]
ONEONEONE = [1,1,1]
HIGHPAIRS = ['AA', 'KK', 'QQ']
MIDDLEPAIRS = ['JJ', 'TT', '99', '88', '77', '66']
LOWPAIRS = ['55', '44', '33', '22']
FLOPSTRAIGHT = (['2', '3', 'A'],
                ['2', '3', '4'],
                ['3', '4', '5'],
                ['4', '5', '6'],
                ['5', '6', '7'],
                ['6', '7', '8'],
                ['7', '8', '9'],
                ['8', '9', 'T'],
                ['9', 'J', 'T'],
                ['J', 'Q', 'T'],
                ['J', 'K', 'Q'],
                ['A', 'K', 'Q'])

#var using by human at turn
FOURZERO = [4]
THREEONE = [3,1]
TWOTWO = [2,2]
TWOONEONE = [2,1,1]
ONEONEONEONE = [1,1,1,1]
TURNSTRAIGHT = (['2', '3', '4', 'A'],
                ['2', '3', '4', '5'],
                ['3', '4', '5', '6'],
                ['4', '5', '6', '7'],
                ['5', '6', '7', '8'],
                ['6', '7', '8', '9'],
                ['7', '8', '9', 'T'],
                ['8', '9', 'J', 'T'],
                ['9', 'J', 'Q', 'T'],
                ['J', 'K', 'Q', 'T'],
                ['A', 'J', 'K', 'Q'])
#var using by human at river
FIVEZERO = [5]
FOURONE = [4,1]
THREETWO = [3,2]
THREEONEONE = [3,1,1]
TWOTWOONE = [2,2,1]
TWOONEONEONE = [2,1,1,1]
ONEONEONEONEONE = [1,1,1,1,1]


#var using by computer after flop
FOUR_OF_A_KIND = ([4,1], [4,2], [4,3])
FULL_HOUSE = ([3,2], [3,3])
FLUSH = ([7], [6], [5])
STRAIGHT = (['2', '3', '4', '5', 'A'],
            ['2', '3', '4', '5', '6'],
            ['3', '4', '5', '6', '7'],
            ['4', '5', '6', '7', '8'],
            ['5', '6', '7', '8', '9'],
            ['6', '7', '8', '9', 'T'],
            ['7', '8', '9', 'J', 'T'],
            ['8', '9', 'J', 'Q', 'T'],
            ['9', 'J', 'K', 'Q', 'T'],
            ['A', 'J', 'K', 'Q', 'T'])
THREE_OF_A_KIND = [3,1]
TWO_PAIR = [2,2]
ONE_PAIR = [2,1]


#all actions and processes
ACTIONS= ('fold', 'check', 'call', 'raise',
          'raise 40', 'raise 100', 'raise 120', 'raise 180', 'raise 240', 'raise 360',
          'all_in', 'unknown')
PROCESSES = ('seat', 'blind', 'hold', 'inquire', 'flop', 'turn', 'river', 'showdown', 'pot-win', 'game-over')
POSITION = ('button', 'small', 'big', 'bad')
