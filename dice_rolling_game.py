import random
dice = range(1,7)
playing = True

while playing:
    choice = input("Roll the dice? (y/n): ").lower().strip()
    if choice == "n":
        print('Thank You For Playing!')
        playing = False
    elif choice == "y":
        dice1 = random.choice(dice)
        dice2 = random.choice(dice)
        print(f'({dice1},{dice2})')
    else:
        print("Invalid choice! Please enter 'y' or 'n'.")


