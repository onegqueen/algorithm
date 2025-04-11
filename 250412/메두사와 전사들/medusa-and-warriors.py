from collections import deque


moves = [[-1,0],[1,0],[0,-1],[0,1]]
dir_8 = [[-1,0],[1,0],[0,-1],[0,1],[-1,1],[1,1],[1,-1],[-1,-1]]

N,M = map(int,input().split())
home_r,home_c,park_r,park_c = map(int,input().split())

home = (home_r,home_c)
park = (park_r,park_c)

tmp = list(map(int,input().split()))
fight = []
for i in range(0,M*2-1,2):
    fight.append((tmp[i],tmp[i+1]))

board = []
for i in range(N):
    board.append(list(map(int,input().split())))
            

path = []
def get_path(start):
    visited = [[1e9 for i in range(N)]for j in range(N)]
    dq = deque()
    dq.append((start,[start]))
    visited[start[0]][start[1]]=0
    res = 1e9

    while dq:
        now = dq.popleft()
        dis = len(now[1])
        visited[now[0][0]][now[0][1]]=dis
        
        for move in moves:
            x = now[0][0]+move[0]
            y = now[0][1]+move[1]

            if dis<res and (x,y)==park:
                res = dis
                return now[1]+[(x,y)]

            if x<0 or x>=N or y<0 or y>=N or board[x][y]==1 or visited[x][y]<dis:
                continue
            
            dq.append(((x,y),now[1]+[(x,y)]))
    
    return []

def get_visible(d,start):
    vis = [[False for i in range(N)]for j in range(N)]
    x,y = 0,0
    l = 3

    if d == 0 :
        x,y = -1,-1
        line = start[1]

    elif d == 1:
        x,y = 1,-1
        line = start[1]
    
    elif d == 2:
        x,y = -1,-1

    elif d == 3:
        x,y = -1,+1
        
    start = (start[0]+x,start[1]+y)
    if d == 0 or d == 1:
        while start[0]>=0 and start[0]<N:
                for i in range(start[1],start[1]+l):
                    if i>=0 and i<N:
                        vis[start[0]][i] = True
                start = (start[0]+x,start[1]+y)
                l+=2
    else:
        while start[1]>=0 and start[1]<N:
                for i in range(start[0],start[0]+l):
                    if i>=0 and i<N:
                        vis[i][start[1]] = True
                start = (start[0]+x,start[1]+y)
                l+=2

    return vis

def where(pos,target):
    n = (pos[0]-1,pos[1])
    s = (pos[0]+1,pos[1])
    w = (pos[0],pos[1]-1)
    e = (pos[0],pos[1]+1)

    if target[1]==n[1] and target[0]<=n[0] : return 0
    elif target[1]==s[1] and target[0]>=s[0] : return 1
    elif target[0]==w[0] and target[1]<=w[1]: return 2
    elif target[0]==e[0] and target[1]>=e[1] : return 3
    elif target[0]<e[0] and target[1]>n[1] : return 4
    elif target[0]>e[0] and target[1]>s[1] : return 5
    elif target[0]>w[0] and target[1]<s[1] : return 6
    elif target[0]<w[0] and target[1]<n[1] :return 7

def get_hide(pos,target,vis):
    res = 0
    w = where(pos,target)
    x,y = 0,0

    start = target
    if w == 0 :
        x,y = -1,0
        l = 1
        start = (target[0]+x,target[1]+y)
        while start[0]>=0:
            if vis[start[0]][start[1]]:
                vis[start[0]][start[1]] = False
                res+=1
            start = (start[0]+x,start[1]+y)
            
    elif w == 1:
        x,y = 1,0
        l = 1
        start= (target[0]+x,target[1]+y)
        while start[0]<N:
            if vis[start[0]][start[1]]:
                vis[start[0]][start[1]] = False
                res+=1

            start = (start[0]+x,start[1]+y)

    elif w == 2:
        x,y = 0,-1
        l = 1
        start= (target[0]+x,target[1]+y)
        while start[1]>=0:
            if vis[start[0]][start[1]]:
                vis[start[0]][start[1]] = False
                res+=1

            start = (start[0]+x,start[1]+y)

    elif w == 3:
        x,y = 0,1
        l = 1
        start =(target[0]+x,target[1]+y)
        while start[1]<N:
            if vis[start[0]][start[1]]:
                vis[start[0]][start[1]] = False
                res+=1

            start = (start[0]+x,start[1]+y)

    elif w == 4:
        x,y = -1,0
        l = 2
        start =(target[0]+x,target[1]+y)
        while start[0]>=0 and start[0]<N:
            for i in range(start[1],start[1]+l):
                if i>=0 and i<N and vis[start[0]][start[1]]:
                    vis[start[0]][start[1]] = False
                    res+=1

            start = (start[0]+x,start[1]+y)
            l+=1

    elif w == 5:
        x,y = 1,0
        l = 2
        start =(target[0]+x,target[1]+y)
        while start[0]>=0 and start[0]<N:
            for i in range(start[1],start[1]+l):
                if i>=0 and i<N and vis[start[0]][start[1]]:
                    vis[start[0]][start[1]] = False
                    res+=1
            start = (start[0]+x,start[1]+y)
            l+=1
    elif w == 6:
        x,y = 1,0
        l = 2
        start =(target[0]+x,target[1]+y)
        while start[0]>=0 and start[0]<N:
            for i in range(start[1],start[1]-l,-1):
                if i>=0 and i<N and vis[start[0]][start[1]]:
                    vis[start[0]][start[1]] = False
                    res+=1
            start = (start[0]+x,start[1]+y)
            l+=1
    elif w == 7:
        x,y = -1,0
        l = 2
        start =(target[0]+x,target[1]+y)
        while start[0]>=0 and start[0]<N:
            for i in range(start[1],start[1]-l,-1):
                if i>=0 and i<N and vis[start[0]][start[1]]:
                    vis[start[0]][start[1]] = False
                    res+=1
            start = (start[0]+x,start[1]+y)
            l+=1
    
    return res
    
    
path = get_path(home)[1:-1]

for i in range(N):
    for j in range(N):
        if (i,j) in fight:
            if board[i][j] == 1:
                board[i][j] = -1
            else:
                board[i][j] = board[i][j]-1
    


if not path :
    print(-1)

else:
    monster = home
    for nxt in path:
        monster=nxt
        stone = 0
        dis = 0
        attack = 0
        # print("start",monster)
        # for a in range(N):
        #     print(board[a])

        if board[nxt[0]][nxt[1]] < 0:
            board[nxt[0]][nxt[1]]-=board[nxt[0]][nxt[1]]

        hide_cnt = 0
        visible = [[False for i in range(N)]for j in range(N)]
        for i in range(4):
            vis = get_visible(i,monster)
            res = 0
            for f in fight:
                if vis[f[0]][f[1]]:
                    get_hide(monster,f,vis)

            for x in range(N):
                for y in range(N):
                    if board[x][y]<0 and vis[x][y]:
                        res+=abs(board[x][y])
            
            if res>hide_cnt:
                hide_cnt=res
                for x in range(N):
                    for y in range(N):
                        visible[x][y]=vis[x][y]
        
        # print("hide",hide_cnt)
        # for a in range(N):
        #     print(board[a])
        # for a in range(N):
        #     print(visible[a])

        fight = []
        tmp = []  
        for x in range(N):
            for y in range(N):
                if visible[x][y] and board[x][y]<0:
                    stone+=abs(board[x][y])
                    fight.append((x,y))
                    continue

    
                elif board[x][y]<0:
                    nxt_x = x
                    nxt_y = y
                    now_d = abs(monster[0]-x)+abs(monster[1]-y)
                    for m in moves:
                        xm = x+m[0]
                        ym = y+m[1]

                        if xm >=0 and xm<N and ym>=0 and ym<N and not visible[xm][ym]:
                            nxt_d = abs(monster[0]-xm)+abs(monster[1]-ym)
                            if nxt_d<now_d:
                                nxt_x = xm
                                nxt_y = ym
                                break
                    
                    res_x = nxt_x
                    res_y = nxt_y
                    now_d = abs(monster[0]-nxt_x)+abs(monster[1]-nxt_y)
                    for m in moves[2:]+moves[:2]:
                        xm = nxt_x+m[0]
                        ym = nxt_y+m[1]

                        if xm >=0 and xm<N and ym>=0 and ym<N and not visible[xm][ym]:
                            nxt_d = abs(monster[0]-xm)+abs(monster[1]-ym)
                            if nxt_d<now_d:
                                res_x = xm
                                res_y = ym
                                break
                    
                    #print(x,y,nxt_x,nxt_y,res_x,res_y)
                    if (res_x,res_y) == monster:
                        dis = dis + ((abs(x-res_x)+abs(y-res_y))*abs(board[x][y]))
                        attack+=1
                        board[x][y]-=board[x][y]
                    
                    else:
                        dis = dis + ((abs(x-res_x)+abs(y-res_y))*abs(board[x][y]))
                        fight.append((res_x,res_y))
                        tmp.append([x,y,res_x,res_y])
        for t in tmp:
            if(t[0],t[1])==(t[2],t[3]):continue
            board[t[2]][t[3]] += board[t[0]][t[1]]
            board[t[0]][t[1]]-=board[t[0]][t[1]]

        # print("end")
        # for a in range(N):
        #     print(board[a])
        # for a in range(N):
        #     print(visible[a])
        print(dis,stone,attack)
        

                        
    print(0)                        

#거리,돌,전사

