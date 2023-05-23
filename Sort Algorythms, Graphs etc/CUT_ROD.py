import time
import math
import random


#Zad1-------------------------------------------------------------------------------------

#Generuje tablice wielkości n z losowymi cenami długości pręta, pierwszy indeks ignorujemy

def generator(n):
    X=[0]
    for i in range(n):
        X.append(random.randint(1,50))
    return X


#ignorujemy pierwszy indeks 
def CUT_ROD(p,n):
    if n==0:
        return 0
    else: 
        q=-math.inf
        for i in range(1,n+1):
            q=max(q,CUT_ROD(p,n-i)+p[i])
    return q

#Dla tablic wielkości ~20 algorytm działa w rozsądnym czasie 
#arr = [0, 1, 5, 8, 9, 10, 17, 17, 20 ]
#print(CUT_ROD(arr,len(arr)-1)) #przykładowe wywołanie 

#Zad2-----------------------------------------------------------------------------------------------

def MEMORIZED_CUT_ROD_KOSZT(p): #p[0]=0 zwraca koszt 
    lst =[0]+ [-math.inf] *(len(p)-1)
    return CUT_ROD_KOSZT(p,len(p)-1,lst)
def CUT_ROD_KOSZT(p,j,r):
    if r[j]>=0:
        return (r[j])
    else:
        if j==0:
            return (0,0)
        else: 
            q=-math.inf
            for i in range(1,j+1):
                q=max(q,CUT_ROD_KOSZT(p,j-i,r)+p[i])

            r[j]=q
            return (q)    

#arr = [0, 1, 5, 8, 9, 10, 17, 17, 20 ]
#print(MEMORIZED_CUT_ROD_KOSZT(arr)) #przykładowe wywołanie


def MEMORIZED_CUT_ROD_OPTYMALNE(p): #p[0]=0 zwraca listę długości na które trzeba pociąc pręt
    optymalne=[0]+[0]*(len(p)-1)
    lst =[0]+ [-math.inf] *(len(p)-1)
    return CUT_ROD2(p,len(p)-1,lst,optymalne)[1]
def CUT_ROD2(p,j,r,optymalne):
    if r[j]>=0:
        return (r[j],optymalne[j])
    else:
        if j==0:
            return (0,0)
        else: 
            q=-math.inf
            for i in range(1,j+1):
                a=CUT_ROD2(p,j-i,r,optymalne)
                if q<a[0]+p[i]:
                    q=a[0]+p[i]
                    if a[1]==0:
                        o=[i]
                    else:
                        o=a[1]+[i]
            r[j]=q
            optymalne[j]=o
            return (q,o)  

#arr = [0, 1, 5, 8, 9, 10, 17, 17, 20 ]
#print(MEMORIZED_CUT_ROD_OPTYMALNE(arr)) #przykładowe wywołanie


#--------------------------------------------------------------------------------
#CZAS CUT_ROD VS MEMORIZED_CUT_ROD
"""
v=generator(20)
a=time.time()
CUT_ROD(v,len(v)-1)
a= time.time()-a
b=time.time()
MEMORIZED_CUT_ROD_KOSZT(v)
b=time.time()-b
print(a,b)
"""
#czas CUT_ROD dla tablicy n= 20 ~~ 0.5384414196014404
#Czas MEMORIZED_CUT_ROD_KOSZT n=20 ~~ 0.0009980201721191406
#----------------------------------------------------------------
        



#zad3-----------------------------------------------------------------

def CUT_ROD_ITERACJA_KOSZT(p): #p[0]=0, zwraca optymalny koszt pociętego pręta
    lst =[0]+ [-math.inf] *(len(p)-1)
    return CUT_ROD3_KOSZT(p,lst)
def CUT_ROD3_KOSZT(p,r):
    r[0]=0
    for j in range (1,len(p)):
        q=-math.inf
        for i in range(1,j+1):
            if r[j-i]+p[i]>q:
                q=r[j-i]+p[i]
        r[j]=q
    return r

#arr = [0, 1, 5, 8, 9, 10, 17, 17, 20 ]
#print(CUT_ROD_ITERACJA_KOSZT(arr))

def CUT_ROD_ITERACJA_OPTYMALNE(p): #p[0]=0, zwraca listę długości na które trzeba pociąc pręt
    optymalne=[0]+[0]*(len(p)-1)
    lst =[0]+ [-math.inf] *(len(p)-1)
    return CUT_ROD3_OPTYMALNE(p,lst,optymalne)
def CUT_ROD3_OPTYMALNE(p,r,s):
    r[0]=0
    for j in range (1,len(p)):
        q=-math.inf
        for i in range(1,j+1):
            if r[j-i]+p[i]>q:
                q=r[j-i]+p[i]
                if s[j-i]== 0:
                    s[j]=[j]
                else:
                    s[j]=s[j-i]+[i]
        r[j]=q
    return s[len(s)-1]

#arr = [0, 1, 5, 8, 9, 10, 17, 17, 20 ]
#print(CUT_ROD_ITERACJA_OPTYMALNE(arr))




