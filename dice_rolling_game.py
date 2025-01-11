import random
dice = [1,2,3,4,5,6]
playing = True

while playing:
    choice = input("Roll the dice? (y/n):").lower()
    if choice == "n":
        print('Thank You!')
        playing = False
    elif choice == "y":
        dice1 = random.choice(dice)
        dice2 = random.choice(dice)
        print(f'({dice1},{dice2})')
    else:
        print("Invalid")
