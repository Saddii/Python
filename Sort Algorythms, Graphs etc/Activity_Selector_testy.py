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


    
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]


s = [1, 3, 2, 0, 5, 8, 11]
f = [3, 4, 5, 7, 9, 10, 12]

#print(R_ACTIVITY_SELECTOR(s,f,-1,len(f)-1))
#print(ACTIVITY_SELECTOR(s,f))

#zad2

s=[0,1,3,5,5,8]
f=[6,2,4,7,9,9]

def R_ACTIVITY_SELECTOR2(s,f,k,n):
    def Selector2(s,f,k,n):
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

s=[1,5]
f=[4,6]
print(R_ACTIVITY_SELECTOR2(s,f,len(f)-1,-1))
print(ACTIVITY_SELECTOR2(s,f))




'''
import random
t=False
while t==False:
    s=[]
    f=[]
    for i in range(0,100):
        s.append(random.randint(0,99))
    s.sort()
    j=0
    while len(f)<100:
        x=random.randint(0,100)
        if(x>s[j]):
            f.append(x)
            j=j+1

    a=R_ACTIVITY_SELECTOR2(s,f,len(f)-1,-1)
    b=ACTIVITY_SELECTOR2(s,f)
    if(a==b):
        print(True)
    else:
        t=True
        print(s)
        print(f)
        print(a,b)

'''

