with open("Day2input.txt",'r') as inputfile:
    lines = inputfile.readlines()
    print(lines)
two_same_letters_in_word = 0
three_same_letters_in_word = 0

for line in lines:
    print(line[:-1])
    uniqletters = list(set(line[0:-1]))
    print(uniqletters)
    two_same_letters = False
    three_same_letters = False
    for x in uniqletters:
        count = 0
        for y in line:
            if x==y:
                count +=1
        if count == 2:
            two_same_letters = True
        if count == 3:
            three_same_letters = True
    if three_same_letters:
        three_same_letters_in_word+=1
    if two_same_letters:
        two_same_letters_in_word+=1
print(two_same_letters_in_word*three_same_letters_in_word)
        
        
