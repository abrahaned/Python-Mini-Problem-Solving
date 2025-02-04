# input user r,p,s
#if not contains rps invalid and try again
#if r,p,s
#get input and random for computer
#if user is r and computer is
# r > s > p > s
import random
item = ["r","p","s"]
is_continue = ["y","n"]

while True:
    user_choice = input("Rock, Paper , or sissor ? (r/p/s) : ")
    if user_choice in item:
        computer = random.choice(item)
        if user_choice == computer:
            print(f"You Choose {user_choice}")
            print(f"Computer Choose {computer}")
            print("Drew")
            keep_play = input("Continue? (y/n)")
            if keep_play in is_continue:
                if keep_play == "y":
                    continue
                else:
                    break
            else:
                print("Invalid")
        else:
            if user_choice == "r":
                if computer == "p":
                    print(f"You Choose {user_choice}")
                    print(f"Computer Choose {computer}")
                    print("You Loose!")
                    keep_play = input("Continue? (y/n)")
                    if keep_play in is_continue:
                        if keep_play == "y":
                            continue
                        else:
                            break
                    else:
                        print("Invalid")
                else:
                    print(f"You Choose {user_choice}")
                    print(f"Computer Choose {computer}")
                    print("You Win!")
            elif user_choice == "p":
                    if computer == "r":
                        print(f"You Choose {user_choice}")
                        print(f"Computer Choose {computer}")
                        print("You Win!")
                        keep_play = input("Continue? (y/n)")
                        if keep_play in is_continue:
                            if keep_play == "y":
                                continue
                            else:
                                break
                        else:
                            print("Invalid")
                    else:
                        print(f"You Choose {user_choice}")
                        print(f"Computer Choose {computer}")
                        print("You Loose!")
                        keep_play = input("Continue? (y/n)")
                        if keep_play in is_continue:
                            if keep_play == "y":
                                continue
                            else:
                                break
                        else:
                            print("Invalid")
            elif user_choice == "s":
                if computer == "p":
                        print(f"You Choose {user_choice}")
                        print(f"Computer Choose {computer}")
                        print("You Win!")
                        keep_play = input("Continue? (y/n)")
                        if keep_play in is_continue:
                            if keep_play == "y":
                                continue
                            else:
                                break
                        else:
                            print("Invalid")
                else:
                    print(f"You Choose {user_choice}")
                    print(f"Computer Choose {computer}")
                    print("You Loose!")
                    keep_play = input("Continue? (y/n)")
                    if keep_play in is_continue:
                        if keep_play == "y":
                            continue
                        else:
                            break
                    else:
                        print("Invalid")       

    else:
        print("Invalid")
        continue