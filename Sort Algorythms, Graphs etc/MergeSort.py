from math import floor
import random

def merge_sort1(A):
    if len(A)>0:
        s=floor((len(A))/2)
        L=merge_sort1(A[0:s])
        R=merge_sort1(A[s:len(A)])
        i=0
        j=0
        k=0
        while i< len(L) and j < len(R):
                if L[i]<R[j]:
                    A[k]=L[i]
                    i+=1
                else:
                    A[k]=R[j]
                    j+=1
                k+=1
        while i<len(L):
                A[k]=L[i]
                i+=1
                k+=1
        while j<len(R):
                A[k]=R[j]
                j+=1
                k+=1
        return A
    return A

def merge_sort2(A):
    if len(A)>1:
        s=floor((len(A)+1)/3)
        L=merge_sort2(A[0:s])
        M=merge_sort2(A[s:2*s])
        R=merge_sort2(A[2*s:len(A)])
        i=0
        j=0
        k=0
        l=0
        while i< len(L) and l<len(M) and j < len(R):
                if L[i]<=R[j]:
                    if L[i]<=M[l]:
                        A[k]=L[i]
                        i+=1
                        k+=1
                    elif M[l]<=R[j]:
                        A[k]=M[l]
                        k+=1
                        l+=1
                    if len(L)==i or len(M)==l:
                            break
                if R[j]<=L[i]:
                    if R[j]<M[l]:
                        A[k]=R[j]
                        j+=1
                        k+=1
                    elif M[l]<=R[j]:
                        A[k]=M[l]
                        l+=1
                        k+=1
        while i<len(L) and l<len(M):
            if L[i]<=M[l]:
                A[k]=L[i]
                i+=1
                k+=1
            else:
                A[k]=M[l]
                l+=1
                k+=1
        while l<len(M) and j<len(R):
            if M[l]<=R[j]:
                A[k]=M[l]
                l+=1
                k+=1
            else:
                A[k]=R[j]
                j+=1
                k+=1
        while i<len(L) and j<len(R):
            if R[j]<=L[i]:
                A[k]=R[j]
                j+=1
                k+=1
            else:
                A[k]=L[i]
                i+=1
                k+=1
        while i<len(L):
                A[k]=L[i]
                i+=1
                k+=1
        while l<len(M):
            A[k]=M[l]
            l+=1
            k+=1
        while j<len(R):
                A[k]=R[j]
                j+=1
                k+=1
        return A
    return A
    
def merge_sort3(A):
    if len(A)>5:
        s=floor((len(A))/2)
        L=merge_sort3(A[0:s])
        R=merge_sort3(A[s:len(A)])
        i=0
        j=0
        k=0
        while i< len(L) and j < len(R):
                if L[i]<R[j]:
                    A[k]=L[i]
                    i+=1
                else:
                    A[k]=R[j]
                    j+=1
                k+=1
        while i<len(L):
                A[k]=L[i]
                i+=1
                k+=1
        while j<len(R):
                A[k]=R[j]
                j+=1
                k+=1
        return A
    else:
        for i in range(1,len(A)):
            x=A[i]
            j=i-1
            while j>-1 and A[j]>x:
                A[j+1]=A[j]
                j=j-1
            A[j+1]=x
        
    return A
