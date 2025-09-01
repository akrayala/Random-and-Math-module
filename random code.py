import random 
Computer_choice = random.randint(1,5) 
print("I will generate a number between 1 to 5 and you have to guest the number one digit at a time. The game ends when you get one right awnser")
playing = True
while playing:
    user_choice = int(input("Give your best choice"))
    if Computer_choice == user_choice:
        print("You win the game")
        break
    else:
        print("Your guess isn't right try again")
        print(f"Computer choice is{Computer_choice}")
