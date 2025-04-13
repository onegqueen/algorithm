import heapq

INF = 1e9

Q = int(input())
N,M = 0,0
graph = []
cost = []
revenues = {}
dests = {}
ids = []

def dijkstra(start):
    dis = [INF for i in range(N)]
    dis[start] = 0

    hq = []
    heapq.heapify(hq)
    hq.append((0,start))

    while hq:
        node = heapq.heappop(hq)

        for nxt in graph[node[1]]:
            if node[0]+nxt[0]<dis[nxt[1]]:
                dis[nxt[1]] = node[0]+nxt[0]
                hq.append((dis[nxt[1]],nxt[1]))
    
    return dis

def construct(info):
    for i in range(0,M*3,3):
        v,u,w = int(info[i]),int(info[i+1]),int(info[i+2])
        graph[v].append((w,u))
        graph[u].append((w,v))

    return dijkstra(0)

def set_advantages():
    global advantages,revenues,cost,dests

    for key,value in revenues.items():
        if value == -1 or cost[dests[key]]==INF:
            continue

        advantages[key] = value - cost[dests[key]]
    
    return 0

best_product = INF
advantages = {}
advantages[INF] = -1
for _ in range(Q):
    cmd = list(map(str,input().split()))
    if cmd[0] == "100":
        N = int(cmd[1])
        M = int(cmd[2])
        graph = [[]for i in range(N)]
        cost = construct(cmd[3:])

    elif cmd[0] == "200":
        ID, revenue, dest = int(cmd[1]),int(cmd[2]),int(cmd[3])
        revenues[ID] = revenue
        dests[ID] = dest
        advantages[ID] = revenues[ID] - cost[dests[ID]]

        if advantages[ID] > advantages[best_product] :
            best_product = ID
        if advantages[ID] == advantages[best_product] and best_product > ID:
            best_product = ID

    
    elif cmd[0] == "300":
        ID = int(cmd[1])
        revenues[ID] = -1
        dests[ID] = -1
        advantages[ID] = -1

        if ID == best_product:
            best_product = max(advantages,key=advantages.get)
    
    
    elif cmd[0] == "400":
        if best_product==INF or advantages[best_product]==-1:
            print(-1)
        else:
            print(best_product)
        

        revenues[best_product]=-1
        dests[best_product]=-1
        advantages[best_product]=-1
        best_product = max(advantages,key=advantages.get)

    elif cmd[0] =="500":
        cost = dijkstra(int(cmd[1]))

        best_product = INF
        advantages = {}
        advantages[INF] = -1
        set_advantages()
        best_product = max(advantages,key=advantages.get)



