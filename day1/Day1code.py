with open('/Users/shorya/Dropbox/programming_shorya/python_code/AdventofCode/inputday1.txt','r') as input:
    x = input.readlines()
    print(x)
finishnum = 0
y = 0
mylist = []
for y in range(0,len(x)):
    z=str(x[y])[:len(x[y])-1]
    if z[0] == '-':
        
        z=int(z[0:])
        finishnum = finishnum +z
        if finishnum in mylist:
            num = finishnum
            print(num)
        mylist.append(finishnum)
        
    else:
        z = int(z)
        finishnum = finishnum+z
        if finishnum in mylist:
            num = finishnum
            print(num)
        mylist.append(finishnum)

    print(z)
    print(finishnum,'\n')

print(finishnum)