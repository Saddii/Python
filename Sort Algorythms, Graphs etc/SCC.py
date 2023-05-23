
#Zad1
def sortowanie(G,v,posortowane):
    G[v][0]='grey'
    for w in G[v][1]:
        if (G[w][0]=='white'):
            G[w][2]=v
            sortowanie(G,w,posortowane)
    posortowane.append(v)
    G[v][0]='black'

def TOPOLOGICAL_SORT(G):
    Q={}
    posortowane=[]
    for i in G:
        Q[i]=['white',G[i],'parrent']
    for i in G:
        if Q[i][0] == 'white':
            sortowanie(Q,i,posortowane)
    posortowane.reverse()
    return posortowane

#Zad2

def transpose(G):
    A={}
    for i in G:
        for j in G[i]:
            A[j]=[]
            A[j].append(i)
    return dict(sorted(A.items()))

def DFS_VISIT(A,v,posortowane):

    A[v][0]='grey'
    posortowane.append(v)
    for i in A[v][1]:
        if A[i][0] == 'white':
            DFS_VISIT(A,i,posortowane)
    A[v][0]='black'
    return posortowane

def DFS_VISIT2(G,v,stack):
    G[v][0]='grey'
    for w in G[v][1]:
        if (G[w][0]=='white'):
            DFS_VISIT2(G,w,stack)
    stack =stack.append(v)
    G[v][0]='black'


def STRONGLY_CONNECTET_COMPONENTS(G):
    posortowane=[]
    stack = []
    Q={}
    for i in G:
        Q[i]=['white',G[i]]
    for i in G:
        if Q[i][0] == 'white':
            DFS_VISIT2(Q,i,stack)
    Gt = transpose(G)
    R={}
    for i in Gt:
        R[i]=['white',Gt[i]]

    while stack:
        i = stack.pop()
        if R[i][0]=='white':
            pos=[]
            a=DFS_VISIT(R,i,pos)
            posortowane.append(a)

    return posortowane

#zad3
def STRONGLY_CONNECTET_COMPONENTS_L(G,lista):
    posortowane=[]
    stack = []
    Q={}
    for i in lista:
        Q[i]=['white',G[i]]
    for i in lista:
        if Q[i][0] == 'white':
            DFS_VISIT2(Q,i,stack)
    Gt = transpose(G)
    R={}
    for i in lista:
        R[i]=['white',Gt[i]]

    while stack:
        i = stack.pop()
        if R[i][0]=='white':
            pos=[]
            a=DFS_VISIT(R,i,pos)
            posortowane.append(a)

    return posortowane

#porównywanie listy list zwraca True jeśli takie same
def sublists_equal(a, b):
    return all(l for l in b if l in a)
