import random

v_file=open("english_dict.txt","r")
v_file_str=v_file.read()
v_file.close()
v_file_set=set(v_file_str.split())
word_list=list(v_file_set)
clean_list=[]
for word in word_list:
    if len(word)>4:
        clean_list.append(word.replace(".","").lower())
word_list=clean_list
        

for i in range(0,len(word_list)):
    word_list[i]=word_list[i].lower()
print (word_list)

word_index=random.randint(0,len(word_list)-1)
word = list(word_list[word_index])
word_len=len(word)
letter_count=0
num_of_tries=0
print("welcome to hang game")

while True:
    a=input("Enter a letter\n")
    if a in word:
        letter_count+=1
        word.remove(a)
        print("Letter exists in word - guess the next letter")
    else: 
        num_of_tries+=1
        print("Letter not in word - Try again")
#Success
    if letter_count == word_len:
        print("you guessed the word")
        break
    #Failure
    
    #all tries are exhausted
    if num_of_tries>word_len:
        print("Exhasuted all tries. Better luck next time!")
        break
