import random

word_list = [    "Apple",    "Thunder",    "Puzzle",    "Jellyfish",    "Volcano",    "Whisper",    "Robot"]
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

  