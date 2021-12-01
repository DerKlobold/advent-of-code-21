count = 0
sonarList = []
with open("day1_input.txt", "r") as input:
    for line in input:
        sonarList.append(int(line))

# for index, item in enumerate(sonarList):
#    print(f"item: {item}, index: {index}")
for i in range(len(sonarList)-3):
    a = sonarList[i]
    b = sonarList[i+3]
    if(b > a):
        count += 1
print(count)
