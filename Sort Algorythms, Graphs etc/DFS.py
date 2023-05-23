import time
import random
#Generowanie losowych grafów skierkowanych
def random_graph(num_nodes, num_edges):
    graph = {i: [] for i in range(num_nodes)}
    i=num_edges
    if(num_nodes*(num_nodes-1)<num_edges):
        return "num_edges out of range"
    while i>0:
            x =random.randint(0,num_nodes-1)
            a=random.randint(0,num_nodes-1)
            if a!=x and (a not in graph[x]) and i >0:
                graph[x].append(a)
                i= i-1

    return graph   


#Zad1


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
        Q[i]=['white',G[i],'start','meta','parrent']
    for i in G:
        if Q[i][0] == 'white':
            DFS_VISIT(Q,i,time)
    return Q


#zad2
def spojne_skladowe(G):
    Q=DFS(G)
    spojne_skladowe=0
    for i in Q:
        if Q[i][4]=='parrent':
            spojne_skladowe+=1
    return spojne_skladowe

#zad3
def max_odl(G):
    Q=DFS(G)
    max_odl=0
    for i in Q:
        if Q[i][2]-1>max_odl:
            max_odl=Q[i][2]-1
    return max_odl
wynik=0
for i in range(100):    
    graph=random_graph(1000,1000)
    start=time.time()
    DFS(graph)
    end= time.time()
    wynik=wynik+(end-start)

wynik=wynik/100

a=spojne_skladowe(graph)
b=max_odl(graph)

a={0:[1,2,3,4,5],
1:[0,2],
2:[0,1,3],
3:[1],
4:[0,1],
5:[2,0]}
print(a)
print(DFS(a))








        
