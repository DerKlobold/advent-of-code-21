import numpy as np

with open("input.txt", 'r') as input:
    #cols = len(input.readline())
    rows = 0
    matrix = []
    for line in input:
        line = line.replace('\n', '')
        line = list(map(lambda x: int(x), line))
        matrix.append(line)
        rows += 1

summed_list = list(np.sum(matrix, axis=0))
gamma = []
epsilon = []
for i in summed_list:
    value = (i >= rows/2)
    gamma.append(str(int(value)))
    epsilon.append(str(int(not value)))
print("Gamma: " + str(gamma))
print("Epsilon: " + str(epsilon))
result = int("".join(gamma), 2) * int("".join(epsilon), 2)
print(result)
