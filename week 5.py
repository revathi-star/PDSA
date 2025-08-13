import numpy as np
def dijkstras_list(wlist,s): #Shortest path to a vertex from a start vertex (provided no negative edges or cycles)
    infinity=1+len(wlist.keys())*max(d for u in wlist.keys() for (v,d) in wlist[u])
    (visited,distance)=({},{})
    for v in wlist.keys():
        visited[v],distance[v]=False,infinity
    distance[s]=0
    for u in wlist.keys():
        min_dist=min([distance[v] for v in wlist.keys() if not visited[v]])
        nextv_list=[v for v in wlist.keys() if not visited[v] and distance[v]==min_dist]
        nextv=min(nextv_list)
        visited[nextv]=True
        for (v,d)in wlist[nextv]:
            if distance[v]>distance[nextv]+d:
                distance[v]=distance[nextv]+d
    return distance
dedges=[(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size=7
WL={}
for i in range(size):
    WL[i]=[]
for u,v,d in dedges:
    WL[u].append((v,d))

#print(dijkstras_list(WL,0))

def bellmanford_list(wlist,s):# shortest path from a fixed start vertex in a graph with negatve edges(but no negative cycles)
    infinity=float('inf')
    distance={}
    for v in wlist.keys():
        distance[v]=infinity
    distance[s]=0
    for i in wlist.keys():
        for u in wlist.keys():
            for (v,d) in wlist[u]:
                if distance[v]>distance[u]+d:
                    distance[v]=distance[u]+d
    return distance
dedges1=[(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]
size=8
WL1={}
for i in range(size):
    WL1[i]=[]
for u,v,d in dedges1:
    WL1[u].append((v,d))
#print(bellmanford_list(WL1,0))

def floyd_warshall(w_mat):# all pairs shortest paths (even with negative edges, but not with negative cycles)
    (rows,cols,x)=w_mat.shape #x==2 - 2dimensional array, x is dimension
    infinity=float('inf')
    SP=np.zeros(shape=(rows,cols,cols+1))#creating a zero matrix of same rows,cols and dim=cols+1 ex-8,8,8+1-8*8 matrix and 8 dimensions
    for i in range(rows):
        for j in range(cols):
            if w_mat[i,j,0]==1:
                SP[i,j,0]=w_mat[i,j,1]
            else:
                SP[i,j,0]=infinity
    for k in range(1,cols+1):
        for i in range(rows):
            for j in range(cols):#k-1 because we start k from 1
                SP[i,j,k]=min(SP[i,j,k-1],SP[i,k-1,k-1]+SP[k-1,j,k-1])#check the min of reaching - either from (i to j) or from (i to k and k to j)
    return SP[:,:,cols]#return the last dimension of the shortest path matrix

dimension=3
WM=np.zeros(shape=(size,size,dimension))
for u,v,d in dedges1:
    WM[u,v,0]=1
    WM[u,v,1]=d
#print(floyd_warshall(WM))

def prims_list(wlist):#find the MCST using adjacency list
    infinity=float('inf')
    (visited,distance,TE)=({},{},[])
    for v in wlist.keys():
        visited[v],distance[v]=False,infinity
    visited[0]=True
    for (v,d) in wlist[0]:
        distance[v]=d
    for i in range(1,len(wlist.keys())):
        min_dist=infinity
        nextv=None
        for u in wlist.keys():
            for (v,d) in wlist[u]:
                if visited[u] and (not visited[v]) and d<min_dist:
                    min_dist=d
                    nextv=v
                    nexte=(u,v)
        visited[nextv]=True
        TE.append(nexte)
        for (v,d) in wlist[nextv]:
            if not visited[v]:
                if d<distance[v]:
                    distance[v]=d
    return TE
udedges=[(0,1,10),(0,3,18),(1,3,6),(1,2,20),(2,4,8),(3,4,40)]
size=5
WL2={}
for i in range(size):
    WL2[i]=[]
for u,v,d in udedges:
    WL2[u].append((v,d))
    WL2[v].append((u,d))

#print(prims_list(WL2))

def kruskal(wlist):# finding  MCST by sorting edges and taking the minimum edge which does not form a cycle
    (edges,component,TE)=([],{},[])
    for u in wlist.keys():
        edges.extend([(d,u,v) for (v,d) in wlist[u]])
        component[u]=u 
    edges.sort()#based on 1st value of tuple-weight
    for (d,u,v) in edges:
        if component[u]!=component[v]:
            TE.append((u,v))
            c=component[u]
            for w in wlist.keys():
                if component[w]==c:
                    component[w]=component[v]
    return TE
print(kruskal(WL))