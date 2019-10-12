with open("Day2input.txt",'r') as inputfile:
    lines = inputfile.readlines()
    # print(lines)

for line in lines:
    for other_line in lines:
        differ = 0
        for line_index in range(len(line)):
            if line[line_index] != other_line[line_index]:
                differ+=1
        if differ == 1:
            print(line,other_line)