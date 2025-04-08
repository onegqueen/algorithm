N,M,F = map(int,input().split())

moves=[[0,1],[0,-1],[1,0],[-1,0]]

wall_pos = (-1,-1)
mcn_pos = (-1,-1)
wall_exit = (-1,-1)
exit = (-1,-1)

mizi = []
for i in range(N):
    mizi.append(list(map(int,input().split())))
    for j in range(N):
        if wall_pos == (-1,-1) and mizi[i][j] == 3:
            wall_pos = (i,j)
        if mizi[i][j] ==4:
            exit = (i,j)

wall = []
for _ in range(5):
    tmp = []
    for _ in range(M):
        tmp.append(list(map(int,input().split())))
    wall.append(tmp)

for i in range(M):
    for j in range(M):
        if wall[4][i][j]==2:
            mcn_pos = (i,j)

for i in range(wall_pos[0]-1,wall_pos[0]+M+1):
    for j in range(wall_pos[1]-1,wall_pos[1]+M+1):
        if i == wall_pos[0]-1 or j==wall_pos[1]-1 or i == wall_pos[0]+M or j==wall_pos[1]+M :
            if mizi[i][j]==0 :
                wall_exit = (i,j)

anos = []
for i in range(F):
    anos.append(list(map(int,input().split())))
    if mizi[anos[i][0]][anos[i][1]]==0:
        mizi[anos[i][0]][anos[i][1]]=5

def copy_board(target_board):
    new = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(target_board[i][j])
        new.append(tmp)
    return new

def phenom(target_board,t):
    new = copy_board(target_board)

    for a in anos:
        x = a[0]
        y = a[1]
        if t%a[3]==0:
            while new[x][y]==5:
                if a[2] == 0:
                    y+=1
                elif a[2]==1:
                    y-=1
                elif a[2]==2:
                    x+=1
                else:
                    x-=1 

            if x>=0 and x<N and y>=0 and y<N and new[x][y]==0:
                new[x][y]=5
                
    return new
        


## 시간의벽 탈출
def dfs_wall(now,t,target_board,visited):
    global wall_exit
    res = 1e9
    # print("wall",now)

    for move in moves:
        new = copy_board(target_board)
        x = now[1][0]+move[0]
        y = now[1][1]+move[1]

        z = now[0]

        if now[0] == 4:
            if x == -1:
                z = 3
                x = 0
                y = M-1-y
            elif x == M:
                z = 2
                x = 0
            
            if y == -1:
                z = 1
                y = x
                x = 0
            elif y == M:
                z = 0
                y = x
                x = 0
        
        elif now [0]==0:
            if x == -1:
                z = 4
                x = M-1-y
                y = M-1
            elif x == M:
                if wall_pos[1]+M<N and new[wall_pos[0]+(M-1-y)][wall_pos[1]+M] == 0:
                    res = min(res,t)
                continue  
            if y == -1:
                z = 2
                y = M-1
            elif y == M:
                z = 3
                y = 0
        
        elif now [0] == 2:
            if x == -1:
                z = 4
                x = M-1
            elif x == M:
                if wall_pos[0]+M<N and new[wall_pos[0]+M][wall_pos[1]+y] == 0:
                    res = min(res,t)
                continue 
            if y == -1:
                z = 1
                y = M-1
            elif y == M:
                z = 0
                y = 0
        
        elif now [0] == 1:
            if x == -1:
                z = 4
                x = y
                y = 0
                
            elif x == M:
                if wall_pos[1]-1 > 0 and new[wall_pos[0]+y][wall_pos[1]-1] == 0:
                    res = min(res,t)
                continue
                 
            if y == -1:
                z = 3
                y = M-1
            elif y == M:
                z = 2
                y = 0
        
        elif now [0] == 3:
            if x == -1:
                z = 4
                y = M-1-x
                x = 0
            elif x == M:
                if wall_pos[0]-1>0 and new[wall_pos[0]-1][wall_pos[1]+(M-1-y)] == 0:
                    res = min(res,t)
                continue
                 
            if y == -1:
                z=0
                y=M-1

            elif y == M:
                z = 1
                y = 0
            

        if not visited[z][x][y] and wall[z][x][y] == 0:
            visited[z][x][y] = True
            res = min(res,dfs_wall((z,(x,y)),t+1,phenom(new,t+1),visited))
            visited[z][x][y] = False
    
    return res

def dfs_mizi(node,t,target_board,visited):
    if target_board[node[0]][node[1]] == 4:
        return t-1

    res = 1e9

    for move in moves:
        x = node[0]+move[0]
        y = node[1]+move[1]

        if x<0 or x>=N or y<0 or y>=N or visited[x][y] or target_board[x][y] in [1,3,5]:
            continue
        
        visited[x][y] = True
        res = min(res,dfs_mizi((x,y),t+1,phenom(target_board,t+1),visited))
        visited[x][y] = False
    
    return res

wall_visited = [[[False for i in range(M)]for j in range(M)]for x in range(5)]
tmp = dfs_wall((4,mcn_pos),1,phenom(mizi,1),wall_visited)
for i in range(tmp):
    mizi = phenom(mizi,i+1)

mizi_visited = [[False for i in range(N)]for j in range(N)]
res = dfs_mizi(wall_exit,tmp+1,phenom(mizi,tmp+1),mizi_visited)

if res == 1e9:
    print(-1)
else:
    print(res)

            









