def bubblesort1(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1,i,-1):
            if A[j]<A[j-1]:
                A[j], A[j-1]=A[j-1], A[j]
    return A

def bubblesort2(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1,i,-1):
            if A[j]>A[j-1]:
                A[j], A[j-1]=A[j-1], A[j]
    return A

def bubblesort3(A):
    for i in range(len(A)-1,0 ,-1):
        for j in range(i):
            if A[j]>A[j+1]:
                A[j+1], A[j]=A[j], A[j+1]
    return A