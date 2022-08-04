import heapq, sys

input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    x = int(input())
    heapq.heappush(heap, x)

for _ in range(n):
    print(heapq.heappop(heap))