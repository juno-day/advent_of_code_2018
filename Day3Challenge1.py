# Pathlib
# From Pathlib import Path
# get script's directory
# cd to script's directory

import re
with open('input3.txt','r') as input:
    claims = input.readlines()
    # print(claims)
taken_coords = []
overlapping = []
x = 0
for claim in claims:
    coords = re.search(".+@ (\d+),(\d+)",claim)
    size = re.search(".+: (\d+)x(\d+)",claim)
    
    for height in range(0,int(size.groups()[1])):
        for length in range(0,int(size.groups()[0])):
            coord = [int(coords.groups()[0])+length,int(coords.groups()[1])-height]
            if coord in taken_coords and coord not in overlapping:
                overlapping.append(coord)
            else:
                taken_coords.append(coord)
    x+=1
    print("done "+str(x))
print(len(overlapping))