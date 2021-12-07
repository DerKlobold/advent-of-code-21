with open("input.txt", "r") as input:
    depth = 0
    pos = 0
    aim = 0
    for line in input:
        line = line.split(' ')
        action = line[0][0]
        par = int(line[1].replace('\n', ''))
        if(action == 'f'):
            pos += par
            depth += aim * par
        elif(action == 'd'):
            aim += par
        elif(action == 'u'):
            aim -= par
print(depth*pos)
