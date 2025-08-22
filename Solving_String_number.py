
s='anagram'
t='nagaram'
'''
s_count=dict()
t_count=dict()
for letter in s:
    s_count[letter]=0
print(s_count)
'''

s_count=dict()
t_count=dict()
for letter in s:
    s_count[letter]=0
for letter in t:
    t_count[letter]=0
for letter in s:
    s_count[letter]+=1
for letter in t:
    t_count[letter]+=1           
print(s_count)
print(t_count)
letters =[]
# if s_count.keys()==t_count.keys():
#     print("Keys match") 
#     keycount_verfied=0
#     for key in s_count.keys():
#         if s_count[key]==t_count[key]:
#             keycount_verfied+=1
#         else: 
#             letters.append(key)
#     if keycount_verfied==len(s_count.keys()):
#         print("Anagram")
#     else:         
#         print("Not Anagram")
#         print("Add these letters to make it an anagram",letters)
# else: 
#     print("Not an Anagram")
    

if s_count.keys()==t_count.keys():
    print("Keys match")
    break_loop=False
    for key in s_count.keys():
        if s_count[key]!=t_count[key]:
            print("Not anagram")
            break_loop=True
            break
    if break_loop==False:
        print("Anagram")        
else: 
    print("Not an Anagram")
    