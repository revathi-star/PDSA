inf=float('inf')
import heapq
def dijkstras(wlist,start):
    visited={i:False for i in wlist}
    distance={i:inf for i in wlist}
    distance[start]=0
    heap=[(distance[start],start)]
    while len(heap)>0:
        nextv=heapq.heappop(heap)[1]
        if visited[nextv]:
            continue
        visited[nextv]=True
        for v in wlist[nextv]:
            d=wlist[nextv][v]
            if not visited[v] and distance[v]>distance[nextv]+d:
                distance[v]=distance[nextv]+d
                heapq.heappush(heap,(distance[v],v))
    return distance

def bellman_ford(wlist,src):
    distance={i:inf for i in wlist}
    distance[src]=0
    for _ in range(len(wlist)-1):
        for u in wlist:
            for v in wlist[u]:
                d=wlist[u][v]
                distance[v]=min(distance[v],distance[u]+d)
    for u in wlist:
        for v in wlist[u]:
            d=wlist[u][v]
            assert distance[v]==distance[u]+d,'The Graph has negative cycles'
    return distance

def floyd_warshall(wlist):
    distance={i:{j:inf for j in wlist}for i in wlist}
    for u in wlist:
        for v in wlist[u]:
            distance[u][v]=wlist[u][v]
    for i in wlist:
        distance[i][i]==0
    for i in wlist:
        for j in wlist:
            for k in wlist:
                distance[j][k]=min(distance[j][k],distance[j][i]+distance[i][k])
    return distance

def prim(wlist):
    visited={i:False for i in wlist}
    distance={i:inf for i in wlist}
    parent={i:None for i in wlist}
    src=list(wlist.keys())[0]
    distance[src]=0
    heap=[]
    heapq.heappush(heap,(0,src))
    while len(heap)>0:
        nextv=heapq.heappop(heap)[1]
        if visited[nextv]: continue
        visited[nextv]=True
        for v in wlist[nextv]:
            d=wlist[nextv][v]
            if not visited[v] and distance[v]>d:
                distance[v]=d
                parent[v]=nextv
                heapq.heappush(heap,(distance[v],v))
    mst=[]
    for u in parent:
        if u==src:
            continue
        mst.append([u,parent[u],wlist[parent[u]][u]])
    return mst

class DisjointSET:
    def __init__(self,wlist):
        self.parent={i:i for i in wlist}
        self.members={i:[i] for i in wlist}
        self.size={i:1 for i in wlist}
    
    def is_same_set(self,a,b):
        return self.parent[a]==self.parent[b]
    
    def union_set(self,a,b):
        if self.is_same_set(a,b):
            return
        x,y=self.parent[a],self.parent[b]
        if self.size[x]<self.size[y]:
            x,y=y,x
        for i in self.members[y]:
            self.parent[i]=x
            self.members[x].append(i)
        self.size[x]+=self.size[y]
        del self.members[y]
        return
    
def krushkal(wlist):
    set=DisjointSET([i for i in wlist])
    edges=[]
    for u in wlist:
        for v in wlist[u]:
            d=wlist[u][v]
            edges.append((d,u,v))
    edges.sort()
    mst=[]
    for (d,u,v)in edges:
        if set.is_same_set(u,v):continue
        mst.append((u,v,d))
        set.union_set(u,v)
    return mst

