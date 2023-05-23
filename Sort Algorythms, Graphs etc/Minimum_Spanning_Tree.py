import math
import random
import copy
#Generowanie losowych grafów skierkowanych z wagami
def random_graph(num_nodes, num_edges):
    graph = {i: [[],[]] for i in range(num_nodes)}
    i=num_edges
    if(num_nodes*(num_nodes-1)<num_edges):
        return "num_edges out of range"
    while i>0:
            x =random.randint(0,num_nodes-1)
            a=random.randint(0,num_nodes-1)
            waga=random.randint(0,20)
            if a!=x and (a not in graph[x][0]) and i >0:
                graph[x][0].append(a)
                graph[a][0].append(x)
                graph[x][1].append(waga)
                graph[a][1].append(waga)
                i= i-1
    A=[]
    for i in graph:
        if graph[i][0]==[]:
            A.append(i)
    for i in A:
        graph.pop(i)
            

    return graph 
def DFS_VISIT(G,v,time):
    time= time+1
    G[v][2]=time
    G[v][0]='grey'
    for w in G[v][1]:
        if (G[w][0]=='white'):
            G[w][4]=v
            DFS_VISIT(G,w,time)
    time=time+1
    G[v][3]=time
    G[v][0]='black'  
def DFS(G):
    Q={}
    time=0
    for i in G:
        Q[i]=['white',G[i][0],'start','meta','parrent']
    for i in G:
        if Q[i][0] == 'white':
            DFS_VISIT(Q,i,time)
    return Q

G=random_graph(3,3)
print(G)


def spojny(G):
    Q=DFS(G)
    x=0
    for i in Q:
        if Q[i][4]== 'parrent':
            x+=1
    if x>1:
        return False
    else:
        return True


def w(u,r):
    for i in range(len(G[u][1])):
        if G[u][1][i] in G[r][1]:
            return G[u][1][i]
def extract_min(Q):
    min=math.inf
    for i in Q:
        for j in range(len(Q[i][1])):
            if Q[i][1][j] < min:
                min = Q[i][1][j]
                indeks = [i,j]
    x=Q[indeks[0]][0].pop(indeks[1])
    b=Q[indeks[0]][1].pop(indeks[1])
    y=Q[x][0].index(indeks[0])
    Q[x][0].pop(y)
    Q[x][1].pop(y)

    return x

extract_min(G)
print(G)


def MST_PRIM(G,r):
    if spojny(G)==False:
        return "Graf nie spoójny"
    
    H={}
    for i in G:
        H[i]=[math.inf,'parrent']
    H[r]=[0,-1]
    Q=copy.deepcopy(G)
    
    while Q:
        X=[]
        for i in Q:
            if len(Q[i][0])<1:
                X.append(True)
            else:
                X.append(False)
        if all(X):
            break
            
        u=extract_min(Q)
        for v in G[u][0]:
            if v in Q and w(u,v)< H[v][0]:
                H[v][1]=u
                H[v][0]=w(u,v)
    return H




print(MST_PRIM(G,0))
