# Reserved keywords in Python
# for, if, elif ,else, while, try, except, class, def, return, import, in, is, not, and, or, None, True, False
 
# you cannot use reserved keywords as variable names
# you cannot use numbers at the beginning of a variable name
 
# common datatypes in Python
# int is 5 # 32 bit integer or 64 bit integer depending on the system, 16 bit and 8bit
# float is 5.0 # 64 bit or 32 bit
# bool True or False
# str "hello world" 'hello world'
 
# common data-structure types
# list [1, 4 ,5, 6, 7, 8, 9]
# set {1, "hello", 5.0, 6}
# dict {"orange":"apple", "bannana":"pinaple"}
# tuples (1, 2, 3, 4.5, "hello", True, None) immutable,
 
# # # for loops, if statements, while loops, conditional statements, and, or, ==, !=, <, > , <=, >=, %(Mod)
 
 
# my_dict = {"orange": "hello world", "bannana": ["pinaple", "mango"]}
 
# my_set = set()
# my_set.add(1)
# my_set.add("hello")
# my_set.add(5.0)
# my_set.add(1)
 

## Calculate the area
'''h=5
w=10
area=h*w
print(area)

#Create a list and iterate though it and print each item
L1=[1,4,7,10,12,24,85,100,120]
for i in range(0,len(L1)+1,1):
    print(i)
    '''
##
L1=[1,4,7,10,12,24,24,85,100,120]
'''
a=0
#print(sum(L1))
for i in range(0,len(L1),2):
    a=a+L1[i]
print(a)  '''
    
## Lets start by adding even values
'''
sum1=0
## We need to get all the even values from the list
for i in range(0,len(L1),1): #unpack and list
    if L1[i]%2==0: #check for even values for each element in list
        sum1=sum1+L1[i]
print(sum1)
   

## Sum of even and odd 

sum_even=0
sum_odd=0
for i in range(0,len(L1),1):
    if L1[i]%2==0:
        sum_even=sum_even+L1[i]
    else:
        sum_odd=sum_odd+L1[i]
print(sum_even)
print(sum_odd)

if sum(L1)==sum_even+sum_odd:
    print("Sum is correct")
else: 
    print("Sum is incorrect")
L1.append(145)
## Sum of even and odd values till half of the list
sum_even=0
sum_odd=0
for i in range(0,round(len(L1)/2),1):
    if L1[i]%2==0:
        sum_even=sum_even+L1[i]
    else:
        sum_odd=sum_odd+L1[i]
print(len(L1))
print("round:",round(len(L1)/2))
print("floor:",len(L1)//2)
print(sum_even)
print(sum_odd)

Temp = L1(K)	
L1(K)	L1(i)
L1(i)	Temp


## reverse the list L1=[1,4,7,10,12,24,24,85,100,120]

i=0
k=len(L1)-1
print(L1)
while i<len(L1)//2:
    print(L1[i], L1[k])
    temp=L1[k]
    L1[k]=L1[i]
    L1[i]=temp
    i+=1
    k-=1

print(L1)xxxxxx

## Max value of an array
i=0
max=L1[0]

while i<len(L1):
    if L1[i]>max:
        max=L1[i]
    print(max)
    i+=1
print(max)


a='This  is a Python Class' 
count=0
prev=None
for letter in a:
    if letter==' ' and prev==' ':
        count+=1  
    prev=letter 
print(count)

##Array
a=['This is a python class','Taught by Mostafa','Student is Phani']

word_count=0
for i in range(0,len(a),1):
    count=0
    for letter in a[i]:
        if letter==' ':
            count+=1
    word_count+=count+1
print(word_count)'''

##Matrix
a=[[1,3,7,3,2,9],[10,15,12,30],[100,230,120]]
sum_1=0
##for i in range(0,len(a),1):
    ##for x in a[i]:
       ## print(x)
    ##for x in range(0,len(a[i]),1):
     ##   print(x)
  ##      sum_1+=a[i][x]
##print(s)
for ls in a:
    for number in ls:
        sum_1+=number
print(sum_1)

## Commiting until this line to git - Commit 2