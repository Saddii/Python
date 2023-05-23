import random

def G_1a(n,k):
    if k> n**2:
        return None
    else:
        adjMat = [[0 for i in range(n)]for j in range(n)]
        l=k
        while l>0:
            a=random.randint(0,n-1)
            b=random.randint(0,n-1)
            if adjMat[a][b]==1:
                continue
            adjMat[a][b]=1
            l=l-1
        return adjMat

def G_1b(n,p):
    if p>1 or p<0:
        return None
    adjMat = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            a=random.random()
            if a < p:
                adjMat[i][j]=1
    return adjMat

def random_graph(num_nodes, num_edges):
    # Create a graph with all nodes, but without any edges.
    graph = {i: [] for i in range(num_nodes)}
    # Generate random node indices and link them together.
    i=num_edges
    while i>0:
        for x in range(random.randint(0,num_edges+1)):
            a=random.randint(0,num_edges+1)
            if a!=x and (a not in graph[x]) and i >0:
                graph[x].append(a)
                graph[a].append(x)
                i= i-1
    return graph
a=random_graph(5,3)
print(a)

