import os
import json

pwr_up_dict={'3,7': 'AddCoins', '7,5': 'LifePlus', '4,7': 'Reveal_Loc', '6,6': 'Teleport'}
data_dict={'x':6,'y':12,'pwr_up':pwr_up_dict,'Life':1,'Coin':5}
#data_dict={}

def saving(data_dict):
    x=data_dict['x']
    y=data_dict['y']
    pwr_up=data_dict['pwr_up']
    Life=data_dict['Life']
    Coin=data_dict['Coin']
    g='game.txt'
    file = open(g,'w')
    file.write(str(x)+'\n')
    file.write(str(y)+'\n')
    file.write(json.dumps(pwr_up)+'\n')
    file.write(str(Life)+'\n')
    file.write(str(Coin)+'\n')
    file.close()
    return True

#saving(data_dict)


def load(data_dict={}):
    g='game.txt'
    file = open(g,'r')
    x=file.readline()
    y=file.readline()
    pwr_up=file.readline()
    Life=file.readline()
    Coin=file.readline()
    file.close()
    data_dict['x']=int(x.replace('\n',''))
    data_dict['y']=int(y.replace('\n',''))
    data_dict['pwr_up']= json.loads(pwr_up.replace('\n',''))
    data_dict['Life']=int(Life.replace('\n',''))
    data_dict['Coin']=int(Coin.replace('\n',''))
    #print(data_dict)
    ##for k in data_dict.keys():
      ##  print(k,type(data_dict[k]))
    return data_dict

#load(data_dict)


