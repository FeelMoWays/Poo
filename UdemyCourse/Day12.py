import random as rand
random_number = rand.randint(1,101)
choice  = input('Pick your difficulty easy or hard: ').lower()
lives = 0
if choice == 'easy':
    lives += 10
elif choice == 'hard':
    lives += 5
else:
    print("invalid input")
while lives > 0:
    guess = int(input("Pick your guess: "))
    if guess == random_number:
        print(f"You have won with {lives} remaining")
        break
    else:
        lives -= 1
        print(f'You have {lives} left')
if lives == 0:
    print(f"You have lost the number was {random_number}")