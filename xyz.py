
import random
import os
#from save_load_game import load, saving
import save_load_game
#save_load_game.load()

def move_by(x,y,incx, incy):
    x=x+incx
    y=y+incy
    return x,y

#add random power up locations
def rnd_pwr_loc(pwr_up,x_max,y_max,pwr_up_typ,n_pwr_up):
    for i in range(1,n_pwr_up+1):
        rand_x=random.randint(1,x_max-1)
        rand_y=random.randint(1,y_max-1)
        rand_int=random.randint(1,4)
        pwr_up_val=pwr_up_typ[rand_int]
        str_x,str_y=str(rand_x), str(rand_y)
        str_xy=str_x+','+str_y
        pwr_up[str_xy]=pwr_up_val
    return pwr_up

## Definition each power up 

def Teleport (exit_x, exit_y,x_border,y_border,within_xy=2):
    tel_x=random.randint(exit_x-within_xy,exit_x+within_xy)
    if tel_x > x_border:
        tel_x = x_border
    if tel_x < 0:
        tel_x = 0

    tel_y=random.randint(exit_y-within_xy,exit_y+within_xy)
    if tel_y > y_border:
        tel_y = y_border
    if tel_y<0:
        tel_y = 0
    return(tel_x, tel_y)

def lifeplus(c_life):
    inc_life=c_life+1
    return inc_life

def AddCoins(coin):
    coin=coin+5
    return coin

 
#assignment - add obstacles 
# Power up types
pwr_up_typ={1:'Teleport',2:'LifePlus',3:'AddCoins',4:'Reveal_Loc'}
#pwr_up_typ={1:'Reveal_Loc'}
x=0
y=0
Life=3
Coin=0

#dictionary of power up locations
pwr_up={}
#dictionary of obstacles locations
obstcle={}

x_max, y_max=8,8
exit_x, exit_y=8,6

x,y=move_by(x,y,1,1)
print(x,y)
pwr_up=rnd_pwr_loc(pwr_up,x_max, y_max,pwr_up_typ,4)
print(pwr_up)
ui=input('Type X to load Game!:')
if ui=='x':
    load_var=save_load_game.load()
    x=load_var['x']
    y=load_var['y']
    pwr_up = load_var['pwr_up']
    Life= load_var['Life']
    Coin=load_var['Coin']



while True:
    print('You are at: ',x,',',y, 'You have', Life-1, 'Lifes Left','Keep going!', 'You have earned:', Coin,'Coins') 
    print('Press v to save and exit at any time')
    lf=input('Please enter S for left and D for Right\n')
    if lf=='v':
        save_load_game.saving({'x':x, 'y':y, 'pwr_up':pwr_up, 'Life':Life, 'Coin':Coin})
        break
    ud=input('Please enter W for up and A for down\n')
    if ud == 'v':
        save_load_game.saving({'x':x, 'y':y, 'pwr_up':pwr_up, 'Life':Life, 'Coin':Coin})
        break

    inc_x,inc_y=0,0
    if ud=='w':
        inc_y=1
    elif ud=='a':
        inc_y=-1
    else:
        inc_y=0
    
    if lf=='s':
        inc_x=-1
    elif lf=='d':
        inc_x=1
    else:
        inc_x=0
    x,y=move_by(x,y,inc_x, inc_y)
    if x==exit_x and y==exit_y:
        print('Congrats! You reached the exit and won!')
        break
    curr_xy=str(x)+','+str(y)
    if curr_xy in pwr_up:
        curr_pwr_up=pwr_up[curr_xy]
        if curr_pwr_up == 'Teleport':
            print('Lucky! You got power up: ',curr_pwr_up)
            x,y=Teleport(exit_x, exit_y,x_max, y_max)
        elif curr_pwr_up == 'LifePlus':
            print('Lucky! You got power up: ', curr_pwr_up)
            Life = lifeplus(Life)
        elif curr_pwr_up == 'AddCoins':
            print('Lucky! You got power up: ', curr_pwr_up)
            Coin = AddCoins(Coin)
        elif curr_pwr_up == 'Reveal_Loc':
            print('Lucky! You got power up: ', curr_pwr_up)
            print('You can exit the game at ',exit_x, exit_y, 'Good luck!')
            


        



