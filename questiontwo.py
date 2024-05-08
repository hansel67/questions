import random

N, W = [int(x) for x in input().split()]
items = [[int(x) for x in input().split()] for _ in range(N)]

weights = [int(random()*(10**5)) for i in items]
values = [int(random()*(10**9)) for i in items]

items.sort(key= lambda x: v(x)/w(x))

total_weight = 0
yoshida_bag = []

i = 0

while(total_weight < W):
    yoshida_bag.append(item[i])
    i += 1
    total_weight += w(item[i])

