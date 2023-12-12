import sys
sys.setrecursionlimit(2500)

def union(u,v):
    u=find(u)
    v=find(v)
    parent[u]=v

def find(u):
    while(u!=parent[u]):
        u=parent[u]
        
    return u

g=int(sys.stdin.readline())
p=int(sys.stdin.readline())
gi =[]
parent =[]
answer = 0
for i in range(g+1):
    parent.append(i)

state = True
for i in range(p):
    gi.append(int(sys.stdin.readline()))

    docking = find(gi[i]) # 부모를 찾음
    if state==True and docking !=0 :
        union(docking,docking-1)
        answer+=1
    else : 
        state = False

    

print(answer)
