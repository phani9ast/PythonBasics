roman={"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
n=0
outlier={"IV": 	4,
    "IX":	9,
    "XL":	40,
    "XC":	90,
    "CD":	400,
    "CM":	900}
s="III"
if len(s)<2:
    print( roman[s])
else:
    s_list=list(s)
    i=0
    while i<len(s_list):
        s1=s_list[i]
        if i>=len(s_list)-1:
            n+=roman[s1]
            break
        s2=s_list[i+1]
        print(s1+s2)
        if s1+s2 in outlier:
            i+=2
            n+=outlier[s1+s2]
        else:
            n+=roman[s1]
            i+=1
print(n)