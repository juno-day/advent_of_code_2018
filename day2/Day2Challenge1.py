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
    len_of_word_letters = len(set(letters))
    len_of_word = len(letters)

print(two_same_letters*three_same_letters)