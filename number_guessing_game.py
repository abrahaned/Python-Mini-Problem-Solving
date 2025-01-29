import random

number = random.randint(1,100)

while True:
    print('number is ',number)
    user_number = input("Guess Number Between 1 And 100 : ")
    
    if user_number.isdigit():
        
        if int(user_number) > 100 or int(user_number) < 1:
            print("Please Enter Between 1 And 100")
            continue
        
        if int(user_number) > number:
            print('Too high! Try Again')
        elif int(user_number) == number:
            print('You Right!')
            break
        else:
            print('Too low! Try Again')
            
    else:
        print("Invalid! Please Enter Number")
        