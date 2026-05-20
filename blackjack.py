import random as rand

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = rand.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    




