import sys
from collections import deque
<<<<<<< HEAD
import queue
=======
>>>>>>> 85ea31cc833d62e84424f9ab68d8ffbde6dc189b

n,k = map(int,sys.stdin.readline().split())
num = sys.stdin.readline()
number = []

for i in num:
    number.append(str(i))
<<<<<<< HEAD

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
=======
number.pop(-1)#/n제거

limit = 0
index = 0
answer = []
answer.append(number[0])

for i in range(1,len(number)):
    while limit<k and len(answer)>0 and answer[-1]<number[i] :
        limit+=1
        answer.pop()
        continue
    answer.append(number[i])
    
#limit 횟수가 남았을때는 마지막에 남은것들 제거해야함 !!
while limit<k:
    limit+=1
    answer.pop()

number = ''.join(answer)
>>>>>>> 85ea31cc833d62e84424f9ab68d8ffbde6dc189b

print(int(number))