
def is_iso(s,t):
    if len(s)==len(t) and len(set(s))==len(set(t)):
        m=dict()
        for i in range(0,len(s),1):
            key=s[i]
            value=t[i]
            #( if key already exists then get the value of Key and check against value of the run time value Return False and Exit )
            if key in m and m[key]!=value:  
                return False
            else: 
                m[key]=value
        return True                    
    else: 
        return False
x=input("Input a string s:\n")
y=input("Input a string t:\n")
v=is_iso(x,y)
if v is True:
    print("Isomorphic")
else:
     print("Not Isomorphic")

