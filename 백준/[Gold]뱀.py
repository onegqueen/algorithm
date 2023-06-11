N = int(input())
K = int(input())

board = [[0 for col in range(N+2)] for row in range(N+2)]

#apples
for i in range(K):
    x,y = map(int,input().split())
    board[x][y]=1

L = int(input())
rotate={}
for i in range(L):
    x,c = input().split()
    x=int(x)
    rotate[x]=c


#print(rotate)

#apple:1 
sec = 0
board[1][1]=-1
move = [(0,1),(1,0),(0,-1),(-1,0)]#0,1,2,3 - 오,아,왼,위
state = 0 #오른쪽 진행중
tailstate = 0 #path의 인덱스
head_x=1
head_y=1
tail_x=1
tail_y=1
path =list()

while 1:
    sec+=1
    head_x+=move[state][0]
    head_y+=move[state][1]
    if head_x == 0 or head_x==N+1 or head_y==0 or head_y==N+1 or board[head_x][head_y]==-1:
        break

    #print("head",head_x,head_y)
    path.append(state)

    if board[head_x][head_y] == 1:
        board[head_x][head_y] = -1
    elif board[head_x][head_y] == 0 :
        board[head_x][head_y] = -1
        board[tail_x][tail_y] = 0
        tail_x+=move[path[tailstate]][0]
        tail_y+=move[path[tailstate]][1]
        tailstate+=1
    
    if sec in rotate :
        if rotate[sec] == 'D':
            state+=1
            state%=4
        elif rotate[sec]=='L':
            state+=4
            state-=1
            state%=4
    
    

print(sec)