import sys

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

n = int(input())
points = []
for i in range(n):
    points.append([int(i) for i in input().split()])

ans = 1000000000000000000
for i in range(len(points)):
    for j in range(i+1, len(points)):
        ans = min(ans, dist(points[i], points[j]))
print(ans)
