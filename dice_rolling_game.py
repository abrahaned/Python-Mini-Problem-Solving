import random
dice = [1,2,3,4,5,6]
playing = True

while playing:
    is_keep = input("Roll the dice? (y/n):").lower()
    if is_keep == "n":
        print('Thank You!')
        playing = False
    elif is_keep == "y":
        num1 = random.choice(dice)
        num2 = random.choice(dice)
        print(f'({num1},{num2})')
    else:
        print("Invalid")
