import random
import time
#Generowanie losowych grafów
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

#Zadanie 1  BFS(G,s) zwraca słownik punktów w drzewie przeszukiwań, ich odległość od s oraz przodka każdego punktu.
class punkt:
    def __init__(self, odleglosc,rodzic):
        self.odleglosc = odleglosc
        self.rodzic = rodzic

    def display(self):
        return [self.odleglosc,self.rodzic]

def BFS(G, s): 
    visited = []
    queue = []
    Q={}
    Q["{0}".format(s)]=[0,0]
    visited.append(s)
    queue.append(s)
    odleglosc=0
    
    while queue:
        przodek = queue.pop(0) 
        odleglosc=0
        for neighbour in G[przodek]:
            if neighbour not in visited:
                odleglosc=Q["{0}".format(przodek)][0]
                pkt=punkt(odleglosc+1,przodek)
                Q["{0}".format(neighbour)]=pkt.display()
                visited.append(neighbour)
                queue.append(neighbour)
    return Q

#Zadanie 2 lista sąsiedztwa
def BFS2_lista(G, s):

    if(len(G[s])==0):
        return {s:[]} 
    
    visited = []
    queue = []
    Q = {i: [] for i in range(len(G))}
    
    visited.append(s)
    queue.append(s)

    while queue:
        m = queue.pop(0) 
        for neighbour in G[m]:
            if( neighbour not in Q[m]):
                Q[m].append(neighbour)
            if(m not in Q[neighbour]):
                Q[neighbour].append(m)
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    for i in range(len(Q)):
        if Q[i]==[]:
            Q.pop(i)     
    return Q


#Zadanie 2 macierze sąsiedztwa
def BFS2_macierz(G, s):

    if(len(G[s])==0):
        return {s:[]} 
    
    visited = []
    queue = []
    Q = [[0 for i in range(len(G))]for j in range(len(G))]
    
    visited.append(s)
    queue.append(s)

    while queue:
        m = queue.pop(0) 
        for neighbour in G[m]:
            Q[neighbour][m]=1
            Q[m][neighbour]=1
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    return Q

# Funkcja do zadania 3a. 
def PRINT_PATH(G, s, v):
    explored = []
    queue = []
    queue.append([s])
     
    if s == v:
        print([s])
        return
     
    while queue:
        path = queue.pop(0)
        path1 = path[-1] #ostatni element path

        if path1 not in explored:
            neighbours = G[path1]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == v:
                    print("Najkrotsza sciezka = ", new_path)
                    return
            explored.append(path1)
 
    print("Brak sciezki")
    return



# Funkcja do zadania 3b. 
def PRINT_PATH2(G, v, w):
    explored = []
    queue = []
    queue.append([w])
     
    if v == w:
        print([v])
        return
     
    while queue:
        path = queue.pop(0)
        path1 = path[-1] #ostatni element path

        if path1 not in explored:
            neighbours = G[path1]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == v:
                    print("Najkrotsza sciezka","od",w,"do",v,"=", new_path)
                    return
            explored.append(path1)

a={1:[1,3],2:[1],3:[2]}


for i in range(4):
    print(i)

