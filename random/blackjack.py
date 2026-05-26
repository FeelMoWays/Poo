import random as rand

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = rand.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
        
def compare(user_score,computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "you lose"
    elif user_score == 0:
        return "you win"
    elif user_score > 21:
        return "you lose"
    elif computer_score > 21:
        return "you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"
    




