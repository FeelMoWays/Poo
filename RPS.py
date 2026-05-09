import random as rd
cpu_choices = rd.choice(["rock", "paper", "scissors"])
user_choice = rd.choice(["rock", "paper", "scissors"])
print(user_choice)
if cpu_choices == user_choice:
    print("The Game is a Tie")
elif ((cpu_choices=="rock") and (user_choice == "paper")) or ((cpu_choices == "paper") and (user_choice == "scissors")) or ((cpu_choices == "scissors") and (user_choice == "rock")):
    print("You win")
else:
    print("You Lose")






