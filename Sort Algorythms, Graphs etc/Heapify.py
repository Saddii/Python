import math

def HEAPIFY(A,i):
    l = 2*i+1
    r = 2*i+2
    largest=i
    if l <= len(A)-1 and A[l]>A[largest]:
        largest = l
    if r<= len(A)-1 and A[r] > A[largest]:
        largest=r
    if i != largest:
        (A[i],A[largest])=(A[largest],A[i])
        HEAPIFY(A,largest)

def BUILDHEAP(A):
    for i in range(len(A)//2-1,-1,-1):
        HEAPIFY(A,i)
    return A

def PARRENT(i):
    return math.floor(i/2)

def MAXIMUM(S):
    if len(S>=1):
        return S[0]

def EXTRACT_MAX(S):
    if len(S>=1):
        S[0]=S[len(S)]
        S.pop(len(S)-1)
        HEAPIFY(S,1)

def INCREASE_KEY(S,i,key):
    if S[i] < key:
        S[i]=key
        while i>0 and S[i]> S[PARRENT(i)]:
            S[i], S[PARRENT(i)]=S[PARRENT(i)], S[i]
            i=PARRENT(i)

def INSERT(S,key):
    S.append(0)
    S[len(S)-1]=-math.inf
    INCREASE_KEY(S,len(S)-1,key)

def buildheap1(A):
    a=len(A)
    B=[]
    for i in range(a):
        INSERT(B,A[i])
    return B

def HEAPIFY3(A,i):
    l = 3*i+1
    m = 3*i+2
    r= 3*i+3
    largest=i
    if l <= len(A)-1 and A[l]>A[largest]:
        largest = l
    if m <= len(A)-1 and A[m] > A[largest]:
        largest=m
    if r<= len(A)-1 and A[r] > A[largest]:
        largest=r
    if i != largest:
        (A[i],A[largest])=(A[largest],A[i])
        HEAPIFY3(A,largest)

def PARRENT3(i):
    return math.floor(i/3)

def MAXIMUM3(S):
    if len(S>=1):
        return S[0]

def EXTRACT_MAX3(S):
    if len(S>=1):
        S[0]=S[len(S)]
        S.pop(len(S)-1)
        HEAPIFY3(S,1)

def INCREASE_KEY3(S,i,key):
    if S[i] < key:
        S[i]=key
        while i>0 and S[i]> S[PARRENT3(i)]:
            S[i], S[PARRENT3(i)]=S[PARRENT3(i)],S[i]
            i=S[PARRENT3(i)]

def INSERT3(S,key):
    S.append(0)
    S[len(S)-1]=-math.inf
    INCREASE_KEY3(S,len(S)-1,key)
