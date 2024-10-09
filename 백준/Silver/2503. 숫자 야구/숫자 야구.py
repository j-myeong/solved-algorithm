case = int(input())
hints = []
for _ in range(case):
    hints.append(input().split())

answer = 0
for hund in range(1, 10):
    for ten in range(1, 10):
        for one in range(1, 10):
            if hund == ten or ten == one or one == hund:
                continue

            counter = 0
            for hint in hints:

                strike = 0
                ball = 0

                if int(hint[0][0]) == hund:
                    strike += 1
                if int(hint[0][1]) == ten:
                    strike += 1
                if int(hint[0][2]) == one:
                    strike += 1

                if int(hint[0][0]) == ten or int(hint[0][0]) == one:
                    ball += 1
                if int(hint[0][1]) == hund or int(hint[0][1]) == one:
                    ball += 1
                if int(hint[0][2]) == hund or int(hint[0][2]) == ten:
                    ball += 1

                if strike == int(hint[1]) and ball == int(hint[2]):
                    counter += 1

            if counter == case:
                answer += 1

print(answer)