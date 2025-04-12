from collections import deque

moves = [[-1,0],[1,0],[0,-1],[0,1]]

N,M = map(int,input().split())

sr,sc,er,ec = map(int,input().split())
home = (sr,sc)
park = (er,ec)
tmp = list(list(map(int,input().split())))

warrier = []
for i in range(0,M*2,2):
    warrier.append((tmp[i],tmp[i+1]))

town = []
for i in range(N):
    town.append(list(map(int,input().split())))


def get_path():
    visited = [[False for i in range(N)]for j in range(N)]

    start = home
    dq = deque()
    dq.append((start,[start]))

    while dq:
        now = dq.popleft()

        node = now[0]
        path = now[1]

        if node == park:
            return path

        for move in moves:
            x = node[0]+move[0]
            y = node[1]+move[1]

            if x<0 or x>=N or y<0 or y>=N or visited[x][y] or town[x][y]==1:
                continue
            
            visited[x][y]=True
            dq.append(((x,y),path+[(x,y)]))
    
    return []

def where(pos,target):    
    if pos[1]==target[1] and pos[0]>target[0] : return 0 #상
    elif pos[1]==target[1] and pos[0]<target[0] :return 1#하
    elif pos[0]==target[0] and pos[1]>target[1] : return 2#좌
    elif pos[0]==target[0] and pos[1]<target[1] : return 3#우
    elif pos[0]>target[0] and pos[1]<target[1] : return 4#북동
    elif pos[0]<target[0] and pos[1]<target[1] : return 5#남동
    elif pos[0]<target[0] and pos[1]>target[1] : return 6#남서
    else : return 7 #북서

def get_warrier_sight(m,w,sgt,d):
    w_d = where(m,w)

    # 메두사 시야 (상)
    if d == 0:
        if w_d ==0:
            for i in range(w[0]-1,-1,-1):
                sgt[i][w[1]] = False
        elif w_d == 7:
            now = (w[0]-1,w[1])
            l = 2
            while now[0]>=0:
                for i in range(now[1],now[1]-l,-1):
                    if i>=0 and i<N:
                        sgt[now[0]][i] = False
                now = (now[0]-1,now[1])
                l+=1
        elif w_d == 4:
            now = (w[0]-1,w[1])
            l = 2
            while now[0]>=0:
                for i in range(now[1],now[1]+l):
                    if i>=0 and i<N:
                        sgt[now[0]][i] = False
                now = (now[0]-1,now[1])
                l+=1
    #메두사 시야(하)
    elif d == 1 :
        if w_d ==1:
            for i in range(w[0]+1,N):
                sgt[i][w[1]] = False
        elif w_d == 6:
            now = (w[0]+1,w[1])
            l = 2
            while now[0]<N:
                for i in range(now[1],now[1]-l,-1):
                    if i>=0 and i<N:
                        sgt[now[0]][i] = False
                now = (now[0]+1,now[1])
                l+=1
        elif w_d == 5:
            now = (w[0]+1,w[1])
            l = 2
            while now[0]<N:
                for i in range(now[1],now[1]+l):
                    if i>=0 and i<N:
                        sgt[now[0]][i] = False
                now = (now[0]+1,now[1])
                l+=1
    
    #메두사 시야(좌)
    elif d == 2 :
        if w_d ==2:
            for i in range(w[1]-1,-1,-1):
                sgt[w[0]][i] = False
        elif w_d == 7:
            now = (w[0],w[1]-1)
            l = 2
            while now[1]>=0:
                for i in range(now[0],now[0]-l,-1):
                    if i>=0 and i<N:
                        sgt[i][now[1]] = False
                now = (now[0],now[1]-1)
                l+=1
        elif w_d == 6:
            now = (w[0],w[1]-1)
            l = 2
            while now[1]>=0:
                for i in range(now[0],now[0]+l):
                    if i>=0 and i<N:
                        sgt[i][now[1]] = False
                now = (now[0],now[1]-1)
                l+=1

    #메두사 시야(우)
    elif d == 3 :
        if w_d ==3:
            for i in range(w[1]+1,N):
                sgt[w[0]][i] = False
        elif w_d == 4:
            now = (w[0],w[1]+1)
            l = 2
            while now[1]<N:
                for i in range(now[0],now[0]-l,-1):
                    if i>=0 and i<N:
                        sgt[i][now[1]] = False
                now = (now[0],now[1]+1)
                l+=1
        elif w_d == 5:
            now = (w[0],w[1]+1)
            l = 2
            while now[1]<N:
                for i in range(now[0],now[0]+l):
                    if i>=0 and i<N:
                        sgt[i][now[1]] = False
                now = (now[0],now[1]+1)
                l+=1
    
        
    return sgt

def get_monster_sight(pos,d,is_test):
    monster_sight = [[False for i in range(N)]for j in range(N)]

    ## 초기 메두사 시야 조정
    if d == 0:
        now = (pos[0]-1,pos[1]-1)
        l = 3
        while now[0]>=0:
            for i in range(now[1],now[1]+l):
                if i>=0 and i<N:
                    monster_sight[now[0]][i] = True
            now = (now[0]-1,now[1]-1)
            l+=2
    
    elif d == 1:
        now = (pos[0]+1,pos[1]-1)
        l = 3
        while now[0]<N:
            for i in range(now[1],now[1]+l):
                if i>=0 and i<N:
                    monster_sight[now[0]][i] = True
            now = (now[0]+1,now[1]-1)
            l+=2
    
    elif d == 2:
        now = (pos[0]-1,pos[1]-1)
        l = 3
        while now[1]>=0:
            for i in range(now[0],now[0]+l):
                if i>=0 and i<N:
                    monster_sight[i][now[1]] = True
            now = (now[0]-1,now[1]-1)
            l+=2

    elif d == 3:
        now = (pos[0]-1,pos[1]+1)
        l = 3
        while now[1]<N:
            for i in range(now[0],now[0]+l):
                if i>=0 and i<N:
                    monster_sight[i][now[1]] = True
            now = (now[0]-1,now[1]+1)
            l+=2
    
    #전사별 시야 조정
    for i in range(N):
        for j in range(N):
            if board[i][j]>0 and monster_sight[i][j]:
                get_warrier_sight(pos,(i,j),monster_sight,d)
    
    #돌이된 전사 수
    res = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]>0 and monster_sight[i][j]:
                res+=abs(board[i][j])

    if is_test:
        return res
    
    else:
        return monster_sight

def get_best_sight(pos):
    global sight
    res = 0
    best_d = -1
    for i in range(4):
        tmp = get_monster_sight(pos,i,True)
        if tmp > res:
            res = tmp
            best_d = i

    #최적시야 조정, 돌이된 전사 수 반환
    sight = get_monster_sight(pos,best_d,False)
    return res

def move_warrier(start,pos):
    global sight

    now = start
    for move in moves:
        x = now[0]+move[0]
        y = now[1]+move[1]

        if x<0 or y<0 or x>=N or y>=N or sight[x][y]:
            continue
        
        #가까워진 경우만 변경
        if get_distance((x,y),pos) < get_distance(now,pos):
            now = (x,y)
            break
    
    for move in moves[2:]+moves[:2]:
        x = now[0]+move[0]
        y = now[1]+move[1]

        if x<0 or y<0 or x>=N or y>=N or sight[x][y]:
            continue
        
        #가까워진 경우만 변경
        if get_distance((x,y),pos) < get_distance(now,pos):
            now = (x,y)
            break
    
    #최종위치 반환
    return now
    

def set_warrier():
    global board
    for w in warrier:
        board[w[0]][w[1]]+=1

def get_distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

path = get_path()
if len(path)==0:
    print(-1)

else:
    path=path[1:]
    board = [[0 for i in range(N)] for j in range(N)]
    set_warrier()

    sight = [[False for i in range(N)]for j in range(N)]
    for nxt in path:
        # print("start:",nxt)
        # for i in range(N):
        #     print(board[i])
        # 도착한 곳이 공원
        if nxt == park:
            print(0)
            break
        
        #도착한 곳에 전사가 있다면 죽임
        if board[nxt[0]][nxt[1]] > 0:
            board[nxt[0]][nxt[1]] = 0
        
        #시야 및 돌이된 전사 수 구하기
        stone = get_best_sight(nxt)

        # print("sight")
        # for i in range(N):
        #     print(sight[i])

        #전사 움직이고 움직인 거리 구하기
        attack = 0
        dis = 0
        moved = []
        for i in range(N):
            for j in range(N):
                if board[i][j]>0 and not sight[i][j]:
                    moved.append([(i,j),(move_warrier((i,j),nxt))])
        
        for w in moved:
            past = w[0]
            now = w[1]

            cnt = board[past[0]][past[1]]
            board[now[0]][now[1]]+=cnt
            board[past[0]][past[1]]-=cnt

            dis+=(get_distance(past,now)*cnt)
            
        if board[nxt[0]][nxt[1]] > 0:
            attack += board[nxt[0]][nxt[1]]
            board[nxt[0]][nxt[1]] = 0
        
        # print("moved")
        # for i in range(N):
        #     print(board[i])
        
        print(dis,stone,attack)
            
    

    

    


    

    
    





