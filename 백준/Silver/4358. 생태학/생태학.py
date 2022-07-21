import sys

eco = {}
count = 0

for line in sys.stdin:
    if line == '\n':
        break
    tmp = line.rstrip()
    count += 1
    if tmp not in eco:
        eco[tmp] = 0
    eco[tmp] += 1

sorted_key = sorted(eco)

for key in sorted_key:
    percent = round((eco[key] / count) * 100, 4)
    print(key, end=' ')
    print('%.4f' %percent)
