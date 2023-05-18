import math

set = [0 for _ in range(10)]
case = list(map(int, list(input())))

for item in case: set[item] += 1

set[6] = math.ceil((set[6] + set[9]) / 2)
set[9] = set[6]

print(max(set))