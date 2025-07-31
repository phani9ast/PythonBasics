import random
num = random.randint(9,350)
num_of_tries=0
##is_exit=False
print("type x to exit the game")
while True: #and not is_exit:
    if num_of_tries<5:
        user_input=input("Enter a number \n")
        if user_input == 'x':
            break
            #is_exit = True
        elif int(user_input) < num:
            print("Try a higher number")
            num_of_tries+=1
        elif int(user_input) > num:
            print("Try a lower number")
            num_of_tries+=1
        else:
            print("Bingo! You guessed the correct number ")
            num_of_tries=0
            num=random.randint(30,250)
    else:
        print("Too many tries, lets play again!")
        print("type x to exit the game")
        num=random.randint(9,350)
        num_of_tries=0
