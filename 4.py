import random

figures = ["J", "Q", "K"]
cards = [i for i in range(1,11)] + figures
colors = ["H", "S", "C", "D"]


def sum_cards(cards):
    score=0
    for card in cards:
        if card[1] in figures:
            score += 10
        else:
            score += card[1]
    return score

def play_game(extra_skill): #returns winning players number or 0 for a draw

    deck=[]
    for color in colors:
        for card in cards:
            deck.append([color,card])
    random.shuffle(deck)
    
    while extra_skill and not (deck[-1][1] in figures or deck[-1][1] == 10):
        random.shuffle(deck)
    
    #player 1
    p1=[]
    sum1=0
    while sum1<16:
        sum1=0
        p1.append(deck.pop())
        sum1 = sum_cards(p1)

    if sum1>21:
        return 2

    else:
        while extra_skill and (deck[-1][1] in figures or deck[-1][1] == 10):
            random.shuffle(deck)
        
        #player 2
        p2=[]
        sum2=0
        while sum2<16:
            sum2=0
            p2.append(deck.pop())
            sum2 = sum_cards(p2)

        if sum2>21:
            sum2=0
            
        if sum1>sum2:
            return 1
        elif sum2>sum1:
            return 2
        else:
            return 0


#mode select
m = ""
while m != "1" and m != "2":
    m = input('δώσε λειτουργία μοιρασματος("1" για κανονική, "2" για πειραγμένη): ')

extra_skill = True
if m == "1":
    extra_skill = False


#playing the games
games_won = [0, 0, 0]
for i in range(100):
    games_won[play_game(extra_skill)] += 1


print('υπήρξαν', games_won[0], 'ισοπαλίες')
print('ο πρώτος παίχτης κέρδισε', games_won[1], 'φορές')
print('ο δεύτερος παίχτης κέρδισε', games_won[2], 'φορές')

cmd_wont_close = input()
