# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:48:25 2018

@author: Connor
"""

Rules= '''Blackjack Basic Strategy
4 to 8 Decks • American Style
Dealer Hits Soft 17
Double After Split Allowed
Late Surrender Available
'''

dlr = ['2','3','4','5','6','7','8','9','10','A']
allRules = {}
    

hardData='''
Hard	2	3	4	5	6	7	8	9	10	A
Hard 5	H	H	H	H	H	H	H	H	H	H
Hard 6	H	H	H	H	H	H	H	H	H	H
Hard 7	H	H	H	H	H	H	H	H	H	H
Hard 8	H	H	H	H	H	H	H	H	H	H
Hard 9	H	Dh	Dh	Dh	Dh	H	H	H	H	H
Hard 10	Dh	Dh	Dh	Dh	Dh	Dh	Dh	Dh	H	H
Hard 11	Dh	Dh	Dh	Dh	Dh	Dh	Dh	Dh	Dh	Dh
Hard 12	H	H	S	S	S	H	H	H	H	H
Hard 13	S	S	S	S	S	H	H	H	H	H
Hard 14	S	S	S	S	S	H	H	H	H	H
Hard 15	S	S	S	S	S	H	H	H	Rh	Rh
Hard 16	S	S	S	S	S	H	H	Rh	Rh	Rh
Hard 17	S	S	S	S	S	S	S	S	S	Rs
Hard 18	S	S	S	S	S	S	S	S	S	S
Hard 19	S	S	S	S	S	S	S	S	S	S'''

HD_1 = hardData.split('\n')
ruleSet = {}

for dataRow in HD_1[2:]:
    dP =dataRow.split('\t')
    options ={}
    for decision in zip(dlr,dP[1:]):
        options[decision[0]] = decision[1] 

    ruleSet[dP[0]] = options
   
 
allRules['hard'] = ruleSet

softData='''
Soft	2	3	4	5	6	7	8	9	10	A
A2	H	H	H	Dh	Dh	H	H	H	H	H
A3	H	H	H	Dh	Dh	H	H	H	H	H
A4	H	H	Dh	Dh	Dh	H	H	H	H	H
A5	H	H	Dh	Dh	Dh	H	H	H	H	H
A6	H	Dh	Dh	Dh	Dh	H	H	H	H	H
A7	Ds	Ds	Ds	Ds	Ds	S	S	H	H	H
A8	S	S	S	S	Ds	S	S	S	S	S
A9	S	S	S	S	S	S	S	S	S	S
A10	S	S	S	S	S	S	S	S	S	S'''



HD_1 = softData.split('\n')
ruleSet = {}

for dataRow in HD_1[2:]:
    dP =dataRow.split('\t')
    options ={}
    for decision in zip(dlr,dP[1:]):
        options[decision[0]] = decision[1] 

    ruleSet[dP[0]] = options
   

 
allRules['soft'] = ruleSet


paidData='''
Pair	2	3	4	5	6	7	8	9	10	A
2,2	P	P	P	P	P	P	H	H	H	H
3,3	P	P	P	P	P	P	H	H	H	H
4,4	H	H	H	P	P	H	H	H	H	H
5,5	Dh	Dh	Dh	Dh	Dh	Dh	Dh	Dh	H	H
6,6	P	P	P	P	P	H	H	H	H	H
7,7	P	P	P	P	P	P	H	H	H	H
8,8	P	P	P	P	P	P	P	P	P	Rp
9,9	P	P	P	P	P	S	P	P	S	S
10,10	S	S	S	S	S	S	S	S	S	S
A,A	P	P	P	P	P	P	P	P	P	P'''


HD_1 = paidData.split('\n')
ruleSet = {}

for dataRow in HD_1[2:]:
    dP =dataRow.split('\t')
    options ={}
    for decision in zip(dlr,dP[1:]):
        options[decision[0]] = decision[1] 

    ruleSet[dP[0]] = options
   

allRules['pairs'] = ruleSet



import json

with open('rules.txt', 'w') as file:
     file.write(json.dumps(allRules)) # use `json.loads` to do the reverse
     






