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

def is_quit():
    keep_play = input("Continue ? (y/n) : ").lower()
    if keep_play in is_continue:
        if keep_play == "y":
            return False
        else:
            return True
    else:
        ("Invalid")  
              
while True:
    user_choice = input("Rock, Paper , or sissor ? (r/p/s) : ").lower()
    
    if user_choice in item:
        computer = random.choice(item)
        
        check_win_loose(user_choice,computer)
        if is_quit():
            break
            
    else:
        print("Invalid")