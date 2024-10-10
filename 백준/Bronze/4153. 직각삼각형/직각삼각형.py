while True:
    triangle = list(map(int, input().split()))
    if triangle[0] == 0:
        break
    triangle.sort()
    z = triangle.pop()
    print('right' if z ** 2 == sum(list(map(lambda x: x ** 2, triangle))) else 'wrong')