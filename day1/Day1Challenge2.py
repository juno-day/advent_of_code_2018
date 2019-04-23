import sys
with open('inputday1.txt','r') as input:
    x = input.readlines()
    print(x)
finishnum = 0
y = 0
mylist = []
done = False
while done == False:
    y=0
    for y in range(0,len(x)):
        z=str(x[y])[:len(x[y])-1]
        if z[0] == '-':
            
            z=int(z[0:])
            finishnum = finishnum + z
            
        else:
            z = int(z)
            finishnum = finishnum + z
        if finishnum in mylist:
            print(finishnum)
            sys.exit()
            quit()
        else:
            mylist.append(finishnum)
        #print(z)
        #print(finishnum,'\n')

print(finishnum)