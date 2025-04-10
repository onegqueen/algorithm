from collections import deque

direction = [[-1,0],[0,1],[1,0],[0,-1]]
spot = [[1,0],[0,-1],[0,0],[0,1],[-1,0]]
R,C,K = map(int,input().split())

golams = []
for _ in range(K):
    c,d = map(int,input().split())
    golams.append((c,d))

forest = [[0 for i in range(C)]for j in range(R+2)]

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

    while pos[0]+1<R+1 :
        e = (pos[0],pos[1]+1)
        s = (pos[0]+1,pos[1])
        w = (pos[0],pos[1]-1)
        n = (pos[0]-1,pos[1])

        exit = (pos[0]+direction[exit_d][0],pos[1]+direction[exit_d][1])
        #print(pos,exit)

        if forest[w[0]+1][w[1]] == 0 and forest[s[0]+1][s[1]]==0 and forest[e[0]+1][e[1]]==0:
            for s in spot :
                forest[pos[0]+s[0]+1][pos[1]+s[1]] = forest[pos[0]+s[0]][pos[1]+s[1]]
                forest[pos[0]+s[0]][pos[1]+s[1]] = 0
            exit = (exit[0]+1,exit[1])
            pos = (pos[0]+1,pos[1])
        
        #서쪽이동 
        elif w[1]-1>0 and forest[n[0]][n[1]-1] == 0 and forest[w[0]][w[1]-1] == 0 and forest[s[0]][s[1]-1]==0 and forest[w[0]+1][w[1]-1]==0 and forest[s[0]+1][s[1]-1]==0: 
            forest[exit[0]][exit[1]] = forest[pos[0]][pos[1]]
            exit_d = (exit_d-1)%4
            exit = (pos[0]+direction[exit_d][0],pos[1]+direction[exit_d][1])
            forest[exit[0]][exit[1]] = -forest[pos[0]][pos[1]]
            pos = spin(3,pos)
            exit = (exit[0],exit[1]-1)

            e = (pos[0],pos[1]+1)
            s = (pos[0]+1,pos[1])
            w = (pos[0],pos[1]-1)
            n = (pos[0]-1,pos[1])
            
            for s in spot :
                forest[pos[0]+s[0]+1][pos[1]+s[1]] = forest[pos[0]+s[0]][pos[1]+s[1]]
                forest[pos[0]+s[0]][pos[1]+s[1]] = 0
            exit = (exit[0]+1,exit[1])
            pos = (pos[0]+1,pos[1])
        
        #동쪽이동
        elif e[1]+1<C and forest[n[0]][n[1]+1] == 0 and forest[e[0]][e[1]+1] == 0 and forest[s[0]][s[1]+1]==0 and forest[s[0]+1][s[1]+1]==0 and forest[e[0]+1][e[1]+1]==0:
            
            forest[exit[0]][exit[1]] = forest[pos[0]][pos[1]]
            exit_d = (exit_d+1)%4
            exit = (pos[0]+direction[exit_d][0],pos[1]+direction[exit_d][1])
            forest[exit[0]][exit[1]] = -forest[pos[0]][pos[1]]
            pos = spin(1,pos)
            exit = (exit[0],exit[1]+1)

            e = (pos[0],pos[1]+1)
            s = (pos[0]+1,pos[1])
            w = (pos[0],pos[1]-1)
            n = (pos[0]-1,pos[1])
            
            
            for s in spot :
                forest[pos[0]+s[0]+1][pos[1]+s[1]] = forest[pos[0]+s[0]][pos[1]+s[1]]
                forest[pos[0]+s[0]][pos[1]+s[1]] = 0
            exit = (exit[0]+1,exit[1])
            pos = (pos[0]+1,pos[1])

        else:
            break

    return (pos,exit)

def bfs(start,visited):
    dq = deque()
    dq.append(start)
    res = 0
    while dq:
        now = dq.popleft()
        visited[now[0]][now[1]]=True
        target = abs(forest[now[0]][now[1]])

        if now[0]-1> res:
            res = now[0]-1

        for m in direction:
            x = now[0]+m[0]
            y = now[1]+m[1]

            if (x>0 and x<=R+1 and y>0 and y<C) and forest[x][y]!=0 and ((abs(forest[x][y])==target) or forest[now[0]][now[1]]==-target) and not visited[x][y]:
                dq.append((x,y))
            
    
    return res


ans = 0
idx = 1
for g in golams:
    pos = (1,g[0]-1)
    exit = (pos[0]+direction[g[1]][0],pos[1]+direction[g[1]][1])
    for s in spot:
        forest[pos[0]+s[0]][pos[1]+s[1]] = idx
    forest[exit[0]][exit[1]] = -forest[pos[0]][pos[1]]

    pos,exit = move(pos,g[1])
   
    if pos[0]==1:
        forest = [[0 for i in range(C)]for j in range(R+2)]
        idx+=1
        continue

    
    visited = [[False for i in range(C)]for j in range(R+2)]
    ans+=bfs(pos,visited)
    
    idx+=1

print(ans)