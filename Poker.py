import random


#? Attributes
Pot = 0
Player1_Pot = 0
Player2_Pot = 0
board, board_suites = [], []
Player1_Hand, Player1_Suites = [], []
Player2_Hand, Player2_Suites = [], []
Hand_Rankings = {'Royal Flush': 100, 'Straight Flush': 90, 'Four of a Kind': 80, 'Full House': 70, 'Flush': 60, 'Straight': 50, 'Trips': 40, 'Two Pair': 30, 'One Pair': 20, 'High Card': 10}
order = {'A': 13, 'K': 12 , 'Q': 11 , 'J' : 10, '1': 9, '0': 8 , '9': 7, '8': 6 ,'7': 5 ,'6': 4 ,'5': 3 ,'4': 2 ,'3': 1, '2': 0}

#! Combinations
pair = []
trips = []
fours = []
straight = ['AKQJ10', 'KQJ109', 'QJ1098', 'J10987', '109876', '98765','87654', '76543', '65432', '5432A']
Full_House = []
Four_Kind = []
royal_flush = ['AKQJ10']


#& Cards and Suites
cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suites = ['Heart', 'Spade', 'Club', 'Diamond']

#~ Creating Winning Combinatinos
for combos in cards:
    pair.append(combos * 2)
    trips.append(combos * 3)
    fours.append(combos * 4)


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
            Player2_Pot -= int(How_Much)
            Ask_Player1 = input('Player 1 would you like to Fold or Call? ')
        if Ask_Player1 == 'Fold':
            Player2_Pot += Pot
        elif Ask_Player1 == 'Call':
            Pot += int(How_Much)
            Player1_Pot -= int(How_Much)
            return (function)
    elif Ask_Player1 == 'Raise':
        How_Much = input('How much would you like to Raise? ')
        Pot += int(How_Much)
        Player1_Pot -= int(How_Much)
        Ask_Player2 = input('Player 2 would you like to Fold or Call? ')
        if Ask_Player2 == 'Fold':
            Player1_Pot += Pot
        elif Ask_Player2 == 'Call':
            Pot += int(How_Much)
            Player2_Pot -= int(How_Much)
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

    #! Player 1 Checking Hand Strength 
    
    for i in royal_flush:
        if i in P1_Joined and P1_Score == 0:
            if combo_suites_P1.count(combo_suites_P1[0]) > 4:
                P1_Score += Hand_Rankings['Royal Flush']
    for i in straight:
        if i in P1_Joined and P1_Score == 0:
            if combo_suites_P1.count(combo_suites_P1[0]) > 4:
                P1_Score += Hand_Rankings['Straight Flush']
    
    if P1_Score == 0:
        fullhouse_check = 0
        for i in P1_Joined:
            if P1_Joined.count(i) == 3:
                fullhouse_check += 1
            if P1_Joined.count(i) == 2:
                fullhouse_check += 1
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
    
    if P1_Score == 0:
        twopair_check = 0
        for i in P1_Joined:
            if P1_Joined.count(i) == 2:
                twopair_check += 1
        if twopair_check == 4:
            P1_Score += Hand_Rankings['Two Pair']

    for i in pair:
        if i in P1_Joined and P1_Score == 0:
            P1_Score += Hand_Rankings['One Pair']

    if P1_Score == 0:
        P1_Score += order[P1_Joined[0]]

    
    #! Player 2 Checking Hand Strength
    
    for i in royal_flush:
        if i in P2_Joined and P2_Score == 0:
            if combo_suites_P2.count(combo_suites_P2[0]) == 5:
                P2_Score += Hand_Rankings['Royal Flush']
    for i in straight:
        if i in P2_Joined and P2_Score == 0:
            if combo_suites_P2.count(combo_suites_P2[0]) == 5:
                P2_Score += Hand_Rankings['Straight Flush']
    
    for i in fours:
        if i in P2_Joined and P2_Score == 0 :
            P2_Score += Hand_Rankings['Four of a Kind']
    
    if P2_Score == 0:
        fullhouse_check = 0
        for i in P2_Joined:
            if P2_Joined.count(i) == 3:
                fullhouse_check += 1
            if P2_Joined.count(i) == 2:
                fullhouse_check += 1
        if fullhouse_check == 5:
            P2_Score += Hand_Rankings['Full House']
    
    if P2_Score == 0:
         if combo_suites_P2.count(combo_suites_P2[0]) == 5:
            P2_Score += Hand_Rankings['Flush']

    for i in straight:
        if i in P2_Joined and P2_Score == 0:
            P2_Score += Hand_Rankings['Straight']

    for i in trips:
        if i in P2_Joined and P2_Score == 0:
            P2_Score += Hand_Rankings['Trips']

    
    if P2_Score == 0:
        twopair_check = 0
        for i in P1_Joined:
            if P2_Joined.count(i) == 2:
                twopair_check += 1
        if twopair_check == 4:
            P2_Score += Hand_Rankings['Two Pair']

    for i in pair:
        if i in P2_Joined and P2_Score == 0:
            P2_Score += Hand_Rankings['One Pair']

    if P2_Score == 0:
        P2_Score += order[P2_Joined[0]]
    

    

    #! Find out who wins
    
    if P1_Score == P2_Score:
        kicker_1 = 0
        kicker_2 = 0
        for i in P1_Joined:
            if P1_Joined.count(i) > 1:
                kicker_1 += order[i]

        for i in P2_Joined:
            if P2_Joined.count(i) > 1:
                kicker_2 += order[i]
    
        
        if kicker_1 == kicker_2:
            if P1_Joined[0] > P2_Joined[0]:
                return 'Player 1 wins', P1_Score, P2_Score, P1_Joined, P2_Joined
            elif P2_Joined[0] > P1_Joined[0]:
                return 'Player 2 wins', P1_Score, P2_Score, P1_Joined, P2_Joined
            elif P1_Joined[4] > P2_Joined[4]:
                return 'Player 1 wins', P1_Score, P2_Score, P1_Joined, P2_Joined
            elif P2_Joined[4] > P1_Joined[4]:
                return 'Player 2 wins', P1_Score, P2_Score, P1_Joined, P2_Joined
        if kicker_1 > kicker_2:
            return 'Player 1 wins', P1_Score, P2_Score, P1_Joined, P2_Joined
        else:
            return 'Player 2 wins', P1_Score, P2_Score, P1_Joined, P2_Joined

    elif P1_Score > P2_Score:
        Player1_Pot += Pot
        return 'Player 1 wins this pot', P1_Score, P2_Score, P1_Joined, P2_Joined
    else:
        Player2_Pot += Pot
        return 'Player 2 wins this pot', P1_Score, P2_Score, P1_Joined, P2_Joined
    


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

def clear():
    global Pot
    Pot = 0






print(Player1())
print(Player2())
print(Actions(Flop()))
print(Actions(Turn()))
print(Actions(River()))
print(connect())
print(clear())
print(Pot)
print(Player1_Pot)
print(Player2_Pot)


