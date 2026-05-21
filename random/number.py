import random as rand 
r = rand.randint(1,100)
lives = 0
choice = input("Choose Difficulty Hard Or Easy:").lower()
if choice == "hard":
    lives = 5
else:
    lives = 10
Guessing = True
while Guessing:
    choice = int(input("Enter You Number:"))
    if choice > r:
        print("Too high")
        lives -= 1
        print(f"You have lost a life remaining lives {lives}")
    elif choice < r:
        print("Too Low")
        lives -= 1
        print(f"You have lost a life remaining lives {lives}")
    else:
        print("You have won")
        Guessing = False
    if lives == 0:
        Guessing = False
        print(f"You have lost")
