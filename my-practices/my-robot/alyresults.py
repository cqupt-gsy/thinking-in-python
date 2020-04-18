__author__ = 'Mentu'

import os
import re
first = []
second = []
third = []
fourth = []
fifth = []
sixth = []
seventh = []
eighth = []

regulars=r'(.*)\.csv'
for (dirsHere, thisDir, filesHere) in os.walk('.'):
	for filename in filesHere:
		if re.match(regulars,filename):
		    for line in open(filename):
		        content = line.rstrip().split(',')
		        if content[0] == '1111':
		            first.append(content[6])
		        elif content[0] == '2222':
		            second.append(content[6])
		        elif content[0] == '3333':
		            third.append(content[6])
		        elif content[0] == '4444':
		            fourth.append(content[6])
		        elif content[0] == '5555':
		            fifth.append(content[6])
		        elif content[0] == '6666':
		            sixth.append(content[6])
		        elif content[0] == '7777':
		            seventh.append(content[6])
		        elif content[0] == '8888':
		            eighth.append(content[6])
		        else:
		            continue
diyi = first.count(' 1')
dier = first.count(' 2')
disan = first.count(' 3')
disi = first.count(' 4')
diwu = first.count(' 5')
diliu = first.count(' 6')
diqi = first.count(' 7')
diba = first.count(' 8')
print('1:[%d]; 2:[%d]; 3:[%d]; 4:[%d]; 5:[%d]; 6:[%d]; 7:[%d]; 8:[%d];' % (diyi, dier, disan, disi, diwu, diliu, diqi, diba))
scores1 = diyi*8 + dier*7 + disan*6 + disi*5 + diwu*4 + diliu*3 + diqi*2 + diba*1

diyi = second.count(' 1')
dier = second.count(' 2')
disan = second.count(' 3')
disi = second.count(' 4')
diwu = second.count(' 5')
diliu = second.count(' 6')
diqi = second.count(' 7')
diba = second.count(' 8')
print('2:[%d]; 2:[%d]; 3:[%d]; 4:[%d]; 5:[%d]; 6:[%d]; 7:[%d]; 8:[%d];' % (diyi, dier, disan, disi, diwu, diliu, diqi, diba))
scores2 = diyi*8 + dier*7 + disan*6 + disi*5 + diwu*4 + diliu*3 + diqi*2 + diba*1

diyi = third.count(' 1')
dier = third.count(' 2')
disan = third.count(' 3')
disi = third.count(' 4')
diwu = third.count(' 5')
diliu = third.count(' 6')
diqi = third.count(' 7')
diba = third.count(' 8')
print('3:[%d]; 2:[%d]; 3:[%d]; 4:[%d]; 5:[%d]; 6:[%d]; 7:[%d]; 8:[%d];' % (diyi, dier, disan, disi, diwu, diliu, diqi, diba))
scores3 = diyi*8 + dier*7 + disan*6 + disi*5 + diwu*4 + diliu*3 + diqi*2 + diba*1

diyi = fourth.count(' 1')
dier = fourth.count(' 2')
disan = fourth.count(' 3')
disi = fourth.count(' 4')
diwu = fourth.count(' 5')
diliu = fourth.count(' 6')
diqi = fourth.count(' 7')
diba = fourth.count(' 8')
print('4:[%d]; 2:[%d]; 3:[%d]; 4:[%d]; 5:[%d]; 6:[%d]; 7:[%d]; 8:[%d];' % (diyi, dier, disan, disi, diwu, diliu, diqi, diba))
scores4 = diyi*8 + dier*7 + disan*6 + disi*5 + diwu*4 + diliu*3 + diqi*2 + diba*1

diyi = fifth.count(' 1')
dier = fifth.count(' 2')
disan = fifth.count(' 3')
disi = fifth.count(' 4')
diwu = fifth.count(' 5')
diliu = fifth.count(' 6')
diqi = fifth.count(' 7')
diba = fifth.count(' 8')
print('5:[%d]; 2:[%d]; 3:[%d]; 4:[%d]; 5:[%d]; 6:[%d]; 7:[%d]; 8:[%d];' % (diyi, dier, disan, disi, diwu, diliu, diqi, diba))
scores5 = diyi*8 + dier*7 + disan*6 + disi*5 + diwu*4 + diliu*3 + diqi*2 + diba*1

diyi = sixth.count(' 1')
dier = sixth.count(' 2')
disan = sixth.count(' 3')
disi = sixth.count(' 4')
diwu = sixth.count(' 5')
diliu = sixth.count(' 6')
diqi = sixth.count(' 7')
diba = sixth.count(' 8')
print('6:[%d]; 2:[%d]; 3:[%d]; 4:[%d]; 5:[%d]; 6:[%d]; 7:[%d]; 8:[%d];' % (diyi, dier, disan, disi, diwu, diliu, diqi, diba))
scores6 = diyi*8 + dier*7 + disan*6 + disi*5 + diwu*4 + diliu*3 + diqi*2 + diba*1

diyi = seventh.count(' 1')
dier = seventh.count(' 2')
disan = seventh.count(' 3')
disi = seventh.count(' 4')
diwu = seventh.count(' 5')
diliu = seventh.count(' 6')
diqi = seventh.count(' 7')
diba = seventh.count(' 8')
print('7:[%d]; 2:[%d]; 3:[%d]; 4:[%d]; 5:[%d]; 6:[%d]; 7:[%d]; 8:[%d];' % (diyi, dier, disan, disi, diwu, diliu, diqi, diba))
scores7 = diyi*8 + dier*7 + disan*6 + disi*5 + diwu*4 + diliu*3 + diqi*2 + diba*1

diyi = eighth.count(' 1')
dier = eighth.count(' 2')
disan = eighth.count(' 3')
disi = eighth.count(' 4')
diwu = eighth.count(' 5')
diliu = eighth.count(' 6')
diqi = eighth.count(' 7')
diba = eighth.count(' 8')
print('8:[%d]; 2:[%d]; 3:[%d]; 4:[%d]; 5:[%d]; 6:[%d]; 7:[%d]; 8:[%d];' % (diyi, dier, disan, disi, diwu, diliu, diqi, diba))
scores8 = diyi*8 + dier*7 + disan*6 + disi*5 + diwu*4 + diliu*3 + diqi*2 + diba*1

print('1111: %d' % scores1)
print('2222: %d' % scores2)
print('3333: %d' % scores3)
print('4444: %d' % scores4)
print('5555: %d' % scores5)
print('6666: %d' % scores6)
print('7777: %d' % scores7)
print('8888: %d' % scores8)

