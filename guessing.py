import random
num = 75
while True:
    user_input=int(input("Enter a number \n"))
    if user_input < num:
        print("Try a higher number")
    elif user_input > num:
        print("Try a lower number")
    else:
        print("Bingo! You guessed the correct number ")
        num=random.randint(30,250)
    
