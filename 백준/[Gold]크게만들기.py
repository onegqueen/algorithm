import sys
from collections import deque
import queue

n,k = map(int,sys.stdin.readline().split())
num = sys.stdin.readline()
number = []

for i in num:
    number.append(str(i))

que = queue.Queue()
que.put(number[0])
limit=0

for i in range(1,len(number)):
    if(number[i]<que.peekFront()):
        continue
    while(number[i]>que.peekFront()):
        que.pop()

    que.put(number[i])

number = ''.join(number)

print(int(number))