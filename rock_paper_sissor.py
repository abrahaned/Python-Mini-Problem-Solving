import random
item = ["r","p","s"]

def check_win_loose(user,comp):
    if user == comp:
        print(f"You Choose {user_choice}")
        print(f"Computer Choose {computer}")
    if user == comp:
        print("Draw")
    elif (user == "r" and comp == "s") or (user == "p" and comp == "r") or (user == "s" and comp == "p"):
        print("You Win!")
    else:
        print("You Lose!")
        
def is_quit():
    while True:
        keep_play = input("Continue ? (y/n) : ").lower()
        if keep_play == "y":
            return False
        elif keep_play == "n":
            return True
        else:
            print("Invalid! Please Enter y or n")  
              
while True:
    user_choice = input("Rock, Paper , or sissor ? (r/p/s) : ").lower()
    
    if user_choice in item:
        computer = random.choice(item)
        
        check_win_loose(user_choice,computer)
        if is_quit():
            break
            
    else:
        print("Invalid")