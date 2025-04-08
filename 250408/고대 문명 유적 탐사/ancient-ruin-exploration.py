import sys
from collections import deque

k,m = map(int,sys.stdin.readline().split())
board=[]
for i in range(5):
    board.append(list(map(int,sys.stdin.readline().split())))
peice = list(map(int,sys.stdin.readline().split()))

def spin(x,y,s):
    target = []
    for i in range(x-1,x+2):
        tmp = []
        for j in range(y-1,y+2):
            tmp.append(board[i][j])
        target.append(tmp)
    
    for _ in range(s):
        res = []
        for j in range(0,3):
            tmp = []
            for i in range(2,-1,-1):
                tmp.append(target[i][j])
            res.append(tmp)
        target = res

    return target

move = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(start,visited,target_board):
    queue = deque()
    queue.append(start)
    
    res = []
    while queue:
        now = queue.popleft()
        
        for m in move:
            x = now[0]+m[0]
            y = now[1]+m[1]
            
            if x<0 or x>=5 or y<0 or y>=5 or visited[x][y] or target_board[x][y]!=target_board[now[0]][now[1]]:
                continue

            visited[x][y]=True
            queue.append((x,y))
            res.append((x,y))

    if len(res)>=3:
        return res
    else:
        return []

def get_board():
    global board

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
    global idx
    global board

    res_board = []
    flag = True

    cnt = 0
    get = []
    
    ans = 0
    for s in range(3):
        for i in range(1,4):
            for j in range(1,4):
                base_board = get_board()
                tmp = spin(j,i,s+1)
                new_board=swap(base_board,tmp,(j,i))

                res = []

                for a in range(5):
                    for b in range(5):
                        if (a,b) in res:
                            continue

                        visited = [[False for x in range(5)]for y in range(5)]
                        res+=bfs((a,b),visited,new_board)



                res.sort(key=lambda x : x[1] -x[0])
                if len(res)>cnt:
                    cnt = len(res)
                    get = res
                    res_board = new_board

    ans += cnt

    while get:
        # print(get,idx)
        # for x in range(5):
        #     print(res_board[x])

        for g in get:
            if idx >= len(peice):
                return 0
            res_board[g[0]][g[1]] = peice[idx]
            idx+=1
        
        
        res = []

        for a in range(5):
            for b in range(5):
                if (a,b) in res:
                    continue

                visited = [[False for x in range(5)]for y in range(5)]
                res+=bfs((a,b),visited,res_board)

        res.sort(key=lambda x : x[1] -x[0])
        get = res
        ans+=len(get)

    
    board = res_board
    return ans


idx = 0
for i in range(k):
    tmp = turn()
    if tmp == 0:
        break
    
    print(tmp,end = " ")

print()
        




    
