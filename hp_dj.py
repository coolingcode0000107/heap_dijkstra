import os
import math
import time

from decimal import getcontext
from functools import cache, lru_cache
from time import sleep
from decimal import Decimal, getcontext
from Tools.scripts.fixcid import setreverse
import sys


from matplotlib.cbook import violin_stats



import heapq
from collections import defaultdict
n,m,s=map(int,input().split())
temp=defaultdict(list)
s-=1
for i in range(m):
    u,v,w=map(int,input().split())
    temp[u-1].append((v-1,w))
visited=[False for i in range(n)]
pos=s
res=[1e20 ]*n
res[s]=0
visited[pos]=True
current_min=1e20
priority_queue=[(0,s)]
while priority_queue:
    dist,pos=heapq.heappop(priority_queue)
    if dist>res[pos]:
        continue
    for node, weight in temp[pos]:
        if res[pos] + weight < res[node]:  # 更新距离
            res[node] = res[pos] + weight
            heapq.heappush(priority_queue, (res[node], node))
for i in range(n):
    if res[i]!=1e20:
        print(res[i],end=' ')
    else:
        print(2**31-1,end=' ')


