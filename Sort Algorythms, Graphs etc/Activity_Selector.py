import math 

#zad1

def R_ACTIVITY_SELECTOR(s,f,k,n):
    def Selector(s,f,k,n):
        f[-1]=-math.inf
        n=len(f)-1
        m=k+1
        while m<=n and s[m]<f[k]:
            m=m+1
        if m<=n:
            return [m] + Selector(s,f,m,len(f)-1)
        else:
            return []
    k=-1
    n=len(f)-1
    a=Selector(s,f,k,n)
    return a

def ACTIVITY_SELECTOR(s,f):
    n=len(s)
    A=[0]
    k=0
    for m in range(1,n):
        if s[m]>=f[k]:
            A.append(m)
            k=m
    return A


#zad2

def R_ACTIVITY_SELECTOR2(s,f,k,n):
    k=-1
    n=len(f)-1
    def Selector2(s,f,n,k):
        m=k-1
        while m>n and f[m]>s[k]:
            m=m-1
        if m>=n:
            return [k] + Selector2(s,f,m,-1)
        else:
            return []
    a= Selector2(s,f,k,n)
    a.reverse()
    return a

def ACTIVITY_SELECTOR2(s,f):
    n=len(s)-1
    A=[n]
    k=n
    for m in range(n,-1,-1):
        if s[k]>=f[m]:
            A.append(m)
            k=m
    A.reverse()
    return A
    
# zad3

#Algorytmy nie zwracają zawsze tych samych wyników przykład:
s=[1,5]
f=[4,6]
#print(R_ACTIVITY_SELECTOR(s,f,-1,len(f)-1)) #zwraca zadanie numer 0
#print(ACTIVITY_SELECTOR(s,f)) #zwraca zadanie numer 0
print(R_ACTIVITY_SELECTOR2(s,f,-1,len(f)-1)) #zwraca zadanie numer 1
#print(ACTIVITY_SELECTOR2(s,f)) #zwraca zadanie numer 1
