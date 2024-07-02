from queue import PriorityQueue

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    pq.put(int(input()))

if n == 1:
    print(0)
elif n == 2:
    print(pq.get() + pq.get())
else:
    answer = 0
    while True:
        count = pq.get() + pq.get()
        answer += count
        if pq.empty(): break
        pq.put(count)
    print(answer)