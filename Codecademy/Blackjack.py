import random as rand
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards = []
dealers_cards = []
def calculate(hands):
    score = sum(hands)
    while score > 21 and 11 in hands:
        hands.pop(hands.index(11))
        hands.append(1)
        score = sum(hands)
    return score
for i in range(2):
    player_cards.append(rand.choice(cards))
    dealers_cards.append(rand.choice(cards))
print(f"The players cards are {player_cards}")
print(f'The dealers card is {dealers_cards[0]}')
player_blackjack = sorted([10,11]) == player_cards
dealers_blackjack = sorted([10,11]) == dealers_cards
if player_blackjack and  dealers_blackjack:
    print("This game is a tie")
elif dealers_blackjack:
    print("The dealer has won")
elif player_blackjack:
    print("Player has won")
else:
    game_is_on = True
    while game_is_on:
        choice = input('Do you want to draw more cards: ').lower()
        if choice == 'yes':
            player_cards.append(rand.choice(cards))
            print(player_cards)
            if calculate(player_cards) > 21:
                print('You have lost the game')
                game_is_on = False
        elif choice == 'no':
            game_is_on = False
        else:
            print("Invalid Input")
    if calculate(player_cards) <= 21:
        while calculate(dealers_cards) < 17:
            dealers_cards.append(rand.choice(cards))
        sum_player = calculate(player_cards)
        sum_dealer = calculate(dealers_cards)
        if sum_dealer > 21:
            print("You have won")
        elif sum_player > sum_dealer:
            print("You have won")
        elif sum_player == sum_dealer:
            print("It is a draw")
        else:
            print('You have lost')