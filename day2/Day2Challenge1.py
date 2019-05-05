with open("Day2input.txt",'r') as inputfile:
    lines = inputfile.readlines()
    print(lines)
two_same_letters = 0
three_same_letters = 0
for line in lines:
    print(line)
    letters = []
    for x in line:
        letters.append(x)
    letters.pop()
    for x in letters:
        print(x)
        

print(two_same_letters*three_same_letters)