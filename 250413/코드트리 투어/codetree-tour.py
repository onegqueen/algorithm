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

def sell_best_product():
    global revenues

    res = INF

    max_adv = -1
    revenues = dict(sorted(revenues.items()))
    for key,value in revenues.items():
        adv = value - cost[dests[key]]

        if adv > max_adv :
            max_adv = adv
            res = key
    
    if max_adv < 0 or res == INF:
        return -1
    else:
        revenues[res]=-1
        dests[res]=-1
        return res


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
    
    elif cmd[0] == "300":
        ID = int(cmd[1])
        revenues[ID] = -1
        dests[ID] = -1
    
    elif cmd[0] == "400":
        print(sell_best_product())
    
    elif cmd[0] =="500":
        cost = dijkstra(int(cmd[1]))


