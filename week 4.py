#Adjacency matrix
def get_adj_matrix(V,E):
    size=len(V)
    import numpy as np
    amat=np.zeros(shape=(size,size))
    for (u,v) in E:
        amat[u][v]=1
    return amat 
#Adjacency list
def get_adj_list(V,E):
    size=len(V)
    alist={}
    for i in range(size):
        alist[i]=[]
    for (u,v) in E:
        alist[u].append(v)
    return alist

V=[0,1,2,3,4]
E=[(0,1),(0,2),(1,3),(1,4),(2,4),(2,3),(3,4)]
# print(get_adj_matrix(V,E))
# print(get_adj_list(V,E))

class Queue:
    def __init__(self):
        self.queue=[]

    def isempty(self):
        return self.queue==[]
    
    def enqueue(self,v):
        self.queue.append(v)

    def dequeue(self):
        v=None
        if not self.isempty():
            v=self.queue[0]
            self.queue=self.queue[1:]
        return v

    def __str__(self):
        return str(self.queue)
    
#Implementation of BFS using Adjacency List
def BFSList(AList,start_vertex):
    visited={}
    for each_vertex in AList.keys():
        visited[each_vertex]=False
    q=Queue()
    visited[start_vertex]=True
    q.enqueue(start_vertex)
    while (not q.isempty()):
        curr_vertex=q.dequeue()
        #adj of current vertex
        for adj_vertex in AList[curr_vertex]:
            if not visited[adj_vertex]:
                visited[adj_vertex]=True
                q.enqueue(adj_vertex)
    return visited
AList = {0:[1,2],1:[3,4],2:[4,3],3:[4],4:[]}
# print(BFSList(AList,0))

#Parent and Level info using BFS
def BFS_parent_info_level_no(AList,start_vertex):
    level,parent={},{}
    for each_vertex in AList.keys():
        level[each_vertex]=-1
        parent[each_vertex]=-1
    q=Queue()
    level[start_vertex]=0
    q.enqueue(start_vertex)
    while (not q.isempty()):
        current_vertex=q.dequeue()
        for adj_vertex in AList[current_vertex]:
            if level[adj_vertex]==-1:
                level[adj_vertex]=level[current_vertex]+1
                parent[adj_vertex]=current_vertex
                q.enqueue(adj_vertex)
    return (level,parent)
# print(BFS_parent_info_level_no(AList,0))

#Implementation to find componenets of a graph (using BFS)
def componenets(Alist):
    component={}
    compid,seen=(0,0)

    for v in Alist.keys():
        component[v]=-1
    
    while (seen<max(AList.keys())):
        startv=min(i for i in Alist.keys() if component[i]==-1)
        visited=BFSList(Alist,startv)
        for v in visited.keys():
            if visited[v]:
                seen+=1
                component[v]=compid
        compid+=1

    return component
AList1={0:[1],1:[2],2:[0],3:[4,6],4:[3,7],5:[3,7],6:[5],7:[4,8],8:[5,9],9:[8]}
#print(componenets(AList1))

#Topological sorting using BFS
def toposortlist(AList):
    (indegree,toposort)=({},[])
    zerodegreeq=Queue()
    for u in AList.keys():
        indegree[u]=0
    for u in AList.keys():
        for v in AList[u]:
            indegree[v]+=1
    for u in AList.keys():
        if indegree[u]==0:
            zerodegreeq.enqueue(u)
    while (not zerodegreeq.isempty()):
        curr_vertex=zerodegreeq.dequeue()
        toposort.append(curr_vertex)
        indegree[curr_vertex]-=1
        for adj_vertex in AList[curr_vertex]:
            indegree[adj_vertex]-=1
            if indegree[adj_vertex]==0:
                zerodegreeq.enqueue(adj_vertex)
    return toposort

AList3={0:[2,3,4],1:[2,7],2:[5],3:[5,7],4:[7],5:[6],6:[7],7:[]}
#print(toposortlist(AList3))

#Longest path on DAG using BFS
def longestpathlist(AList):
    (indegree,lpath)=({},{})
    for u in AList.keys():
        (indegree[u],lpath[u])=(0,0)
    for u in AList.keys():
        for v in AList[u]:
            indegree[v]+=1
    zerodegreeq=Queue()
    for u in AList.keys():
        if indegree[u]==0:
            zerodegreeq.enqueue(u)
    while (not zerodegreeq.isempty()):
        curr_vertex=zerodegreeq.dequeue()
        indegree[curr_vertex]-=1
        for adj_vertex in AList[curr_vertex]:
            indegree[adj_vertex]-=1
            lpath[adj_vertex] = max(lpath[curr_vertex] + 1, lpath[adj_vertex])
            if indegree[adj_vertex]==0:
                zerodegreeq.enqueue(adj_vertex)
    return lpath
# print(longestpathlist(AList3))

class Stack:
    def __init__(self):
        self.stack=[]

    def isempty(self):
        return self.stack==[]

    def push(self,v):
        self.stack.append(v)

    def pop(self):
        v=None
        if not self.isempty():
            v=self.stack.pop()
        return v
    
    def __str__(self):
        return str(self.stack)
    
def DFSList(AList,start_vertex):
    visited={}
    for each_vertex in AList.keys():
        visited[each_vertex]=False
    st=Stack()
    st.push(start_vertex)
    while (not st.isempty()):
        current_vertex=st.pop()
        if not visited[current_vertex]:
            visited[current_vertex]=True
            for adj_vertex in AList[current_vertex]:
                if not visited[adj_vertex]:
                    st.push(adj_vertex)
    return visited

# print(DFSList(AList,0))

#Pre and Post numbering using DFS 
(visited, pre, post)=({},{},{})
def DFSinitPrePost(Alist):
    for each_vertex in Alist.keys():
        visited[each_vertex]=False
        (pre[each_vertex],post[each_vertex])=(-1,-1)
def DFSListPrePost(Alist,v,count):
    visited[v]=True
    pre[v]=count
    count+=1
    for adj_vertex in Alist[v]:
        if not visited[adj_vertex]:
            count=DFSListPrePost(Alist,adj_vertex,count)
    post[v]=count
    count+=1
    
    return count
AList2={0:[1,4],1:[0],2:[],3:[],4:[0,8,9],5:[],6:[],7:[],8:[4,9],9:[8,4]}
DFSinitPrePost(AList2)
#print(DFSListPrePost(AList2,0,0))
#print(visited)
#print(pre)
#print(post)