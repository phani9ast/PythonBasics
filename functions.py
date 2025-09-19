## Function to take a file path, read the file and return text that the file has been read

def top_view(A,top_n=10):
    if len(A)<top_n:
        return sorted(A,reverse=True)
    else: 
        c=[]
        b=sorted(A,reverse=True)
        for i in range(0,top_n):
            c.append(b[i])
        return c

    # a='english_dict.txt'
    # file = open(a,"rb")
    # s=file.read()
    # file.close()
    # if s:
    #     print("File has been read successfully")
    # else: 
    #     print("File may be empthy or path incorrect")
    # return s
x=[1,3,5,7,2,10,12,51,90,28,33.41,45]

y=top_view(x,4)
print(y)
