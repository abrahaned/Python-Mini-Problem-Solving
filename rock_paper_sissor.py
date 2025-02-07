# input user r,p,s
#if not contains rps invalid and try again
#if r,p,s
#get input and random for computer
#if user is r and computer is
# r > s > p > s
import random
item = ["r","p","s"]
is_continue = ["y","n"]

def check_win_loose(user,comp):
    if user == comp:
        print(f"You Choose {user_choice}")
        print(f"Computer Choose {computer}")
        print("Drew")
    else:
        if user_choice == "r":
                if comp == "p":
                    print(f"You Choose {user_choice}")
                    print(f"Computer Choose {computer}")
                    print("You Loose!")
                else:
                    print(f"You Choose {user_choice}")
                    print(f"Computer Choose {computer}")
                    print("You Win!")
        elif user_choice == "p":
                if computer == "s":
                    print(f"You Choose {user_choice}")
                    print(f"Computer Choose {computer}")
                    print("You Loose!")
                else:  
                    print(f"You Choose {user_choice}")
                    print(f"Computer Choose {computer}")
                    print("You Win!")
        elif user_choice == "s":   
            if computer == "r":
                print(f"You Choose {user_choice}")
                print(f"Computer Choose {computer}")
                print("You Loose!")
            else:
                print(f"You Choose {user_choice}")
                print(f"Computer Choose {computer}")
                print("You Win!")
        
while True:
    user_choice = input("Rock, Paper , or sissor ? (r/p/s) : ")
    
    if user_choice in item:
        computer = random.choice(item)
        
        check_win_loose(user_choice,computer)
        
        keep_play = input("Continue ? (y/n) : ")
        if keep_play in is_continue:
            if keep_play == "y":
                continue
        else:
            ("Invalid")
            
    else:
        print("Invalid")