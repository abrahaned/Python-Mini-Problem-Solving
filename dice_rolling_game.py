import random

while True:
    choice = input("Roll the dice? (y/n): ").lower().strip()
    if choice == "n":
        print('Thank You For Playing!')
        break
    elif choice == "y":
        dice1,dice2 = random.randint(1,6),random.randint(1,6)
        print(f'({dice1},{dice2})')
    else:
        print("Invalid choice! Please enter 'y' or 'n'.")


