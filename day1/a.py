with open("day1_input.txt", "r") as input:
    count = 0
    prev = 2147483647
    for line in input:
        curr = int(line)
        if (curr > prev):
            count += 1
        prev = curr
print(count)
