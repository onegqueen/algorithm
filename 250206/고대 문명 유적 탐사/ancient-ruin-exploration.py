import sys
from collections import deque

k,m = map(int,sys.stdin.readline().split())
board=[]
for i in range(5):
    board.append(list(map(int,sys.stdin.readline().split())))
peice = list(map(int,sys.stdin.readline().split()))

def spin(x,y):
    res = []
    for j in range(y-1,y+2):
        tmp = []
        for i in range(x+1,x-2,-1):
            tmp.append(board[i][j])
        res.append(tmp)
    return res

move = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(start,visited):
    queue = deque()
    queue.append(start)
    
    res = 0
    count = 0
    
    while queue:
        now = queue.popleft()
        print(now)
        for m in move:
            x = now[0]+m[0]
            y = now[1]+m[1]
            if x<0 or x>=5 or y<0 or y>=5 or visited[x][y]:
                continue
            
            visited[x][y]=True
            if board[start[0]][start[1]] == board[x][y]:
                queue.append((x,y))
                res+=board[x][y]
                count+=1
    
    if count>=3:
        return res
    else:
        return 0

def get_board():
    new = []
    for i in range(5):
        tmp = []
        for j in range(5):
            tmp.append(board[i][j])
        new.append(tmp)
    return new

def swap(base,target,center):
    x = center[0]
    y = center[1]

    for i in range(3):
        for j in range(3):
            base[i+x-1][j+y-1]=target[i][j]

    return base



def turn():
    spined=[]
    for i in range(1,4):
        new_board = get_board()
        for j in range(1,4):
            for s in range(3):
                tmp = spin(i,j)
                new_board=swap(new_board,tmp,(i,j))

                for p in range(5):
                    for q in range(5):
                        visited = [[False for j in range(5)]for i in range(5)]
                        res = bfs((p,q),visited)





        
        




    
