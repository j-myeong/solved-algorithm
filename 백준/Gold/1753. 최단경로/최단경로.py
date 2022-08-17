import sys, heapq

INF = int(1e9)

input = sys.stdin.readline

tmp = input().split(' ')
n, v = int(tmp[0]), int(tmp[1])
start = int(input())

distance = [INF] * (n + 1)
graph = [[] for i in range(n + 1)]

for _ in range(v):
    tmp = input().split(' ')
    graph[int(tmp[0])].append((int(tmp[1]), int(tmp[2])))

# 다익스트라 알고리즘(최소힙 이용))
def dijkstra(start):
  q = []
  # 시작 노드
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)

    # 이미 처리된 노드였다면 무시
    # 별도의 visited 테이블이 필요없이, 최단거리테이블을 이용해 방문여부 확인
    if distance[now] < dist:
      continue
    # 선택된 노드와 인접한 노드를 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 선택된 노드를 거쳐서 이동하는 것이 더 빠른 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for idx in range(1, n + 1):
    print(distance[idx] if distance[idx] != INF else 'INF')