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

def heap_sort1(A):
    posortowana=[]
    for i in range(len(A)//2-1,-1,-1):
        HEAPIFY(A,i)
    while len(A)>0:
        A[len(A)-1], A[0] = A[0],A[len(A)-1]
        posortowana.insert(0,A[len(A)-1])
        A.pop(len(A)-1)
        HEAPIFY(A,0)
    return posortowana



def HEAPIFY2(A,i):
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
        HEAPIFY2(A,largest)

def heap_sort2(A):
    posortowana=[]
    for i in range(len(A)//3,-1,-1):
        HEAPIFY2(A,i)
    while len(A)>0:
        A[len(A)-1], A[0] = A[0],A[len(A)-1]
        posortowana.insert(0,A[len(A)-1])
        A.pop(len(A)-1)
        HEAPIFY2(A,0)
    return posortowana




def HEAPIFY3(A,i):
    while True:
        l = 2*i+1
        r = 2*i+2
        largest=i
        if l <= len(A)-1 and A[l]>A[largest]:
            largest = l
        if r<= len(A)-1 and A[r] > A[largest]:
            largest=r
        if i != largest:
            (A[i],A[largest])=(A[largest],A[i])
            i=largest
        else:
            break

def heap_sort3(A):
    posortowana=[]
    for i in range(len(A)//2-1,-1,-1):
        HEAPIFY3(A,i)
    while len(A)>0:
        A[len(A)-1], A[0] = A[0],A[len(A)-1]
        posortowana.insert(0,A[len(A)-1])
        A.pop(len(A)-1)
        HEAPIFY3(A,0)
    return posortowana






