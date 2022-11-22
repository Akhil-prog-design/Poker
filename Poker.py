import random


#? Attributes
Pot = 0
Player1_Pot = 0
Player2_Pot = 0
board, board_suites = [], []
Player1_Hand, Player1_Suites = [], []
Player2_Hand, Player2_Suites = [], []
Hand_Rankings = {'Royal Flush': 10, 'Straight Flush': 9, 'Four of a Kind': 8, 'Full House': 7, 'Flush': 6, 'Straight': 5, 'Trips': 4, 'Two Pair': 3, 'One Pair': 2, 'High Card': 1}
order = {'A': 13, 'K': 12 , 'Q': 11 ,'J': 10 , '1': 9, '0': 0, '9': 8, '8': 7 ,'7': 6 ,'6': 5 ,'5': 4 ,'4': 3 ,'3': 2, '2': 1}

#! Combinations
pair = []
trips = []
fours = []
straight = ['AKQJ10', 'KQJ109', 'QJ1098', 'J10987', '109876', '98765','87654', '76543', '65432', '5432A']
Flush = []
Full_House = []
Four_Kind = []
straight_flush = []
royal_flush = ['AKQJ10']


#& Cards and Suites
cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suites = ['Heart', 'Spade', 'Club', 'Diamond']

#~ Creating Winning Combinatinos
for combos in cards:
    pair.append(combos * 2)
    trips.append(combos * 3)
    fours.append(combos * 4)

for combos in suites:
    Flush.append(combos * 5)


'''---------'''

def Actions(function):
    global Pot, Player1_Pot, Player2_Pot

    Ask_Player1 = input('Player 1 would you like to Fold, Check, or Raise? ')
    if Ask_Player1 == 'Check':
        Ask_Player2 = input('Player 2 would you like to Fold, Check, or Raise? ')
        if Ask_Player2 == 'Check':
            return (function)
        elif Ask_Player2 == 'Fold':
            Player1_Pot += Pot
        elif Ask_Player2 == 'Raise':
            How_Much = input('How much would you like to Raise? ')
            Pot += int(How_Much)
            Ask_Player1 = input('Player 1 would you like to Fold or Call? ')
        if Ask_Player1 == 'Fold':
            Player1_Pot += Pot
        elif Ask_Player1 == 'Call':
            Pot += int(How_Much)
            return (function)
    elif Ask_Player1 == 'Raise':
        How_Much = input('How much would you like to Raise? ')
        Pot += int(How_Much)
        Ask_Player2 = input('Player 2 would you like to Fold or Call? ')
        if Ask_Player2 == 'Fold':
            Player1_Pot += Pot
        elif Ask_Player2 == 'Call':
            Pot += int(How_Much)
            return (function)



def connect():
    global board, Player1_Hand, Player2_Hand, Player1_Pot, Player2_Pot, Pot
    P1_Score = 0
    P2_Score = 0
    combo_P1 = ''.join(board + Player1_Hand)
    combo_P2  = ''.join(board + Player2_Hand)
    combo_suites_P1 = (board_suites+ Player1_Suites)
    combo_suites_P2 = (board_suites + Player2_Suites)
    count = 13
    P1_Best5 = []
    while count != -1:
        for i in combo_P1:
            if order[i] == count:
                P1_Best5.append(i)
        count -= 1
    count = 13
    P2_Best5 = []
    while count != -1:
        for i in combo_P2:
            if order[i] == count:
                P2_Best5.append(i)
        count -= 1
    P1_Joined = "".join(P1_Best5)
    P2_Joined = "".join(P2_Best5)

    #! Player 1
    
    for i in royal_flush:
        if i in P1_Joined and P1_Score == 0:
            if combo_suites_P1.count(combo_suites_P1[0]) > 4:
                P1_Score += Hand_Rankings['Royal Flush']
    for i in straight:
        if i in P1_Joined and P1_Score == 0:
            if combo_suites_P1.count(combo_suites_P1[0]) > 4:
                P1_Score += Hand_Rankings['Straight Flush']
    
    #TODO: Full House check
    if P1_Score == 0:
        fullhouse_check = 0
        for i in P1_Joined:
            if P1_Joined.count(i) == 3:
                fullhouse_check += 3
            if P1_Joined.count(i) == 2:
                fullhouse_check += 2
        if fullhouse_check == 5:
            P1_Score += Hand_Rankings['Full House']

    
    for i in fours:
        if i in P1_Joined and P1_Score == 0 :
            P1_Score += Hand_Rankings['Four of a Kind']
    
    if P1_Score == 0:
         if combo_suites_P1.count(combo_suites_P1[0]) > 4:
            P1_Score += Hand_Rankings['Flush']

    for i in straight:
        if i in P1_Joined and P1_Score == 0:
            P1_Score += Hand_Rankings['Straight']

    for i in trips:
        if i in P1_Joined and P1_Score == 0:
            P1_Score += Hand_Rankings['Trips']

    for i in pair:
        if i in P1_Joined and P1_Score == 0:
            P1_Score += Hand_Rankings['One Pair']

    if P1_Score == 0:
        P1_Score += order[P1_Joined[0]]

    
    #! Player 2
    
    for i in royal_flush:
        if i in P2_Joined and P2_Score == 0:
            if combo_suites_P2.count(combo_suites_P2[0]) > 4:
                P2_Score += Hand_Rankings['Royal Flush']
    for i in straight:
        if i in P2_Joined and P2_Score == 0:
            if combo_suites_P2.count(combo_suites_P2[0]) > 4:
                P2_Score += Hand_Rankings['Straight Flush']
    
    for i in fours:
        if i in P2_Joined and P2_Score == 0 :
            P2_Score += Hand_Rankings['Four of a Kind']
    
    if P2_Score == 0:
        fullhouse_check = 0
        for i in P2_Joined:
            if P2_Joined.count(i) == 3:
                fullhouse_check += 3
            if P2_Joined.count(i) == 2:
                fullhouse_check += 2
        if fullhouse_check == 5:
            P2_Score += Hand_Rankings['Full House']
    
    if P2_Score == 0:
         if combo_suites_P2.count(combo_suites_P2[0]) > 4:
            P2_Score += Hand_Rankings['Flush']

    for i in straight:
        if i in P2_Joined and P2_Score == 0:
            P2_Score += Hand_Rankings['Straight']

    for i in trips:
        if i in P2_Joined and P2_Score == 0:
            P2_Score += Hand_Rankings['Trips']

    for i in pair:
        if i in P2_Joined and P2_Score == 0:
            P2_Score += Hand_Rankings['One Pair']

    if P2_Score == 0:
        P2_Score += order[P2_Joined[0]]

    

    #TODO: for Everything above one pair if tied find who has the higher striaght, flush, etc 
    
    if P1_Score == P2_Score:
        if order[P1_Joined[0]] > order[P2_Joined[0]]:
            Player1_Pot += Pot
            return 'Player 1 wins this pot'
        else:
            Player2_Pot += Pot
            return 'Player 2 wins this pot' 
    elif P1_Score > P2_Score:
        Player1_Pot += Pot
        return 'Player 1 wins this pot' 
    else:
        Player2_Pot += Pot
        return 'Player 2 wins this pot'


'''---------------'''

def Player1():
    global Player1_Hand, Player1_Suites
    for dealing in range(0,2):
         Player1_Hand.append(random.choice(cards)) 
    for dealing in range(0,2):
        Player1_Suites.append(random.choice(suites))
    return Player1_Hand, Player1_Suites
    

def Player2():
    global Player2_Hand, Player2_Suites
    for dealing in range(0,2):
         Player2_Hand.append(random.choice(cards))
    for dealing in range(0,2):
        Player2_Suites.append(random.choice(suites))
    return Player2_Hand, Player2_Suites


def Flop():
    global board, board_suites
    for dealing in range(0,3):
        board.append(random.choice(cards))
    for dealing in range(0,3):
        board_suites.append(random.choice(suites))
    return board, board_suites

def Turn():
    global board, board_suites
    for dealing in range(0,1):
        board.append(random.choice(cards))
    for dealing in range(0,1):
        board_suites.append(random.choice(suites))
    return board, board_suites

def River():
    global board, board_suites
    for dealing in range(0,1):
        board.append(random.choice(cards))
    for dealing in range(0,1):
        board_suites.append(random.choice(suites))
    return board, board_suites






print(Player1())
print(Player2())
print(Actions(Flop()))
print(Actions(Turn()))
print(Actions(River()))
print(connect())


