from collections import deque
def bfs_adj_matrix(start,matrix):
    visited=[False]*len(matrix)
    queue=deque([start])
    visited[start]=True
    while queue:
        vertex=queue.popleft()
        for j in range(len(matrix)):
            if matrix[vertex][j]==1 and not visited[j]:
                queue.append(j)
                visited[j]=True
    return visited

def bfs_list(start,list):
    queue=deque([start])
    visited={i:False for i in list}
    parent={i:None for i in list}
    level={i:-1 for i in list}
    visited[start]=True
    level[start]=0
    while queue:
        vertex=queue.popleft()
        for i in list[vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                parent[i]=vertex
                level[i]=level[vertex]+1
    return visited,level,parent
    
def dfs_matrix(start,matrix):
    visited=[False]*len(matrix)
    def explore(vertex):
        visited[vertex]=True
        for i in range(len(matrix)):
            if matrix[vertex][i]==1 and not visited[i]:
                explore(i)
    explore(start)
    return visited

def dfs_list(start,list):
    visited={i:False for i in list}
    parent={i:-1 for i in list}
    parent[start]=start 
    def explore(vertex):
        visited[vertex]=True
        for i in list[vertex]:
            if not visited[i]:
                parent[i]=vertex
                explore(i)
    explore(start)
    return visited,parent

def connected_components(list): #BFS Application
    visited={i:False for i in list}
    components={i:-1 for i in list}
    component_id=0
    for start in list:
        if not visited[start]:
            queue=deque([start])
            component_id+=1
            while queue:
                vertex=queue.popleft()
                if visited[vertex]: continue
                visited[vertex]=True
                components[vertex]=component_id
                for v in list[vertex]:
                    if not visited[v]:
                        queue.append(v)
    return components

def pre_post(list,start): #DFS Application
    visited={i:False for i in list}
    pre={i:0 for i in list}
    post={i:0 for i in list}
    cnt=1
    tree_edges=set()
    def explore(node):
        nonlocal cnt
        visited[node]=True
        pre[node]=cnt
        cnt+=1
        for v in list[node]:
            if not visited[v]:
                tree_edges.add((node,v))
                explore(v)
        post[node]=cnt
        cnt+=1
    explore(start)
    return visited,pre,post,tree_edges

def cycle_detection(list): #DFS Application
    visited,pre,post,tree_edges=pre_post(list)
    for u in list:
        for v in list[u]:
            if pre[u]<pre[v] and post[u]>post[v] and (u,v) not in tree_edges:
                return True
    return False

def topological_order(list):
    n=len(list)
    order=[]
    in_degree=[0]*n
    longest_path=[0]*n
    for u in range(n):
        for v in list[u]:
            in_degree[v]+=1
    queue=deque()
    for u in range(n):
        if in_degree[u]==0:
            queue.append(u)
            longest_path[u]==1
    while queue:
        vertex=queue.popleft()
        order.append(vertex) #Whatever you pop from the queue, you append it final order list
        for v in list[vertex]:
            in_degree[v]-=1
            longest_path[v]=max(longest_path[v],longest_path[vertex]+1)
            if in_degree[v]==0:
                queue.append(v)
    return order,max(longest_path)

