import sys
from queue import PriorityQueue

n=int(input())

que = PriorityQueue()

answer = 0

for i in range(n):
    que.put(int(sys.stdin.readline()))

if n>1:
    while que.qsize()>1:
        a = que.get()
        b = que.get()
        c = a+b
        answer+=c
        que.put(c)

    print(answer)

else:
    print(answer)