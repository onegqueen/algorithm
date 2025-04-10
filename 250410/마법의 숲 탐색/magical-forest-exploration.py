from collections import deque

direction = [[-1,0],[0,1],[1,0],[0,-1]]
spot = [[1,0],[0,-1],[0,0],[0,1],[-1,0]]
R,C,K = map(int,input().split())

golams = []
for _ in range(K):
    c,d = map(int,input().split())
    golams.append((c,d))

forest = [[0 for i in range(C)]for j in range(R+3)]

def spin(dr,pos):
    e = (pos[0],pos[1]+1)
    s = (pos[0]+1,pos[1])
    w = (pos[0],pos[1]-1)
    n = (pos[0]-1,pos[1])
    if dr == 3:
        forest[w[0]][w[1]-1]=forest[w[0]][w[1]]
        forest[w[0]][w[1]]=0
        forest[n[0]][n[1]-1]=forest[n[0]][n[1]]
        forest[n[0]][n[1]]=0
        forest[pos[0]][pos[1]-1]=forest[pos[0]][pos[1]]
        forest[pos[0]][pos[1]]=0
        forest[s[0]][s[1]-1]=forest[s[0]][s[1]]
        forest[s[0]][s[1]]=0
        forest[e[0]][e[1]-1]=forest[e[0]][e[1]]
        forest[e[0]][e[1]]=0
        return (pos[0],pos[1]-1)
        
    elif dr == 1:
        forest[e[0]][e[1]+1]=forest[e[0]][e[1]]
        forest[e[0]][e[1]]=0
        forest[n[0]][n[1]+1]=forest[n[0]][n[1]]
        forest[n[0]][n[1]]=0
        forest[pos[0]][pos[1]+1]=forest[pos[0]][pos[1]]
        forest[pos[0]][pos[1]]=0
        forest[s[0]][s[1]+1]=forest[s[0]][s[1]]
        forest[s[0]][s[1]]=0
        forest[w[0]][w[1]+1]=forest[w[0]][w[1]]
        forest[w[0]][w[1]]=0
        return (pos[0],pos[1]+1)
        

def move(pos,exit_d):
    prev = 5

    while pos[0]+1<R+2 :
        e = (pos[0],pos[1]+1)
        s = (pos[0]+1,pos[1])
        w = (pos[0],pos[1]-1)
        n = (pos[0]-1,pos[1])
        
        if forest[w[0]+1][w[1]] == 0 and forest[s[0]+1][s[1]]==0 and forest[e[0]+1][e[1]]==0:
            pos = (pos[0]+1,pos[1])
        
        #서쪽이동 
        elif w[1]-1>=0 and forest[n[0]][n[1]-1] == 0 and forest[w[0]][w[1]-1] == 0 and forest[s[0]][s[1]-1]==0 and forest[w[0]+1][w[1]-1]==0 and forest[s[0]+1][s[1]-1]==0: 
            pos = (pos[0]+1,pos[1]-1)
            exit_d=(exit_d-1)%4
            
        #동쪽이동
        elif e[1]+1<C and forest[n[0]][n[1]+1] == 0 and forest[e[0]][e[1]+1] == 0 and forest[s[0]][s[1]+1]==0 and forest[s[0]+1][s[1]+1]==0 and forest[e[0]+1][e[1]+1]==0:
            pos = (pos[0]+1,pos[1]+1)
            exit_d=(exit_d+1)%4

        else:
            break

    return (pos,exit_d)

def bfs(start,visited,vis_id):
    dq = deque()
    dq.append(start)
    res = 0
    while dq:
        now = dq.popleft()
        target = abs(forest[now[0]][now[1]])

        for m in direction:
            x = now[0]+m[0]
            y = now[1]+m[1]

            if (x>0 and x<=R+2 and y>0 and y<C) and forest[x][y]!=0 and ((abs(forest[x][y])==target) or forest[now[0]][now[1]]==-target) and visited[x][y]!=vis_id:
                visited[now[0]][now[1]]=vis_id
                dq.append((x,y))
                res = max(res,x-2)
            
    
    return res


ans = 0
idx = 1
visited_id = 1
visited = [[0 for i in range(C)]for j in range(R+3)]
for g in golams:
    pos = (1,g[0]-1)

    pos,exit = move(pos,g[1])
    if pos[0]-1<=2:
        forest = [[0 for i in range(C)]for j in range(R+3)]
        idx+=1
        continue

    exit = (pos[0]+direction[exit][0],pos[1]+direction[exit][1])
    for s in spot:
        if forest[pos[0]+s[0]][pos[1]+s[1]]==0:
            forest[pos[0]+s[0]][pos[1]+s[1]] = idx
    forest[exit[0]][exit[1]] = -idx

    ans+=bfs(pos,visited,visited_id)
    
    idx+=1
    visited_id+=1

print(ans)





