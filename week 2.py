#pdsa.py

def naivesearch(l,v):
    for i in range(len(l)):
        if v==l[i]:
            return i
    return False
l=[90,7,4,78,1]
#print(naivesearch(l,3))
#print(naivesearch(l,78))

#Binary search only works when the list is sorted
def binarysearch(l,v):
    low=0
    high=len(l)-1
    while low<=high:
        mid=int((low+high)/2)
        if l[mid]<v:
            low=mid+1
        elif l[mid]>v:
            high=mid-1
        else:
            return mid
    return False
l1=[3,6,17,23,89,115,304]
#print(binarysearch(l1,89))
#print(binarysearch(l1,9))

#Selection Sort
def selectionsort(l):
    n=len(l)
    if n<=1:
        return l
    for i in range(n):
        minpos=i
        for j in range (i+1,n):
            if l[j]<l[minpos]:
                minpos=j
        l[i],l[minpos]=l[minpos],l[i]
    return l
l2=[89,45,34,230,1]
#print(selectionsort(l2))

#Insertion Sort
def insertionsort(l):
    n=len(l)
    if n<=1:
        return l
    for i in range(1,n):
        j=i
        while (j>0 and l[j]<l[j-1]):
            l[j-1],l[j]=l[j],l[j-1]
            j=j-1
    return l
l3=[67,4,2,88,1,6]
l5=[2,0,1,1,2,3,0,2,1,0,2,3,1,2]
print(insertionsort(l5))

#Merge Sort
def merge(a,b):
    m,n=len(a),len(b)
    c,i,j=[],0,0
    while i<m and j<n:
        if a[i]<=b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while i<m:
        c.append(a[i])
        i+=1
    while j<n:
        c.append(b[j])
        j+=1
    return c

def mergesort(l):
    n=len(l)
    if n<=1:
        return l
    left=mergesort(l[:(n//2):])
    right=mergesort(l[(n//2)::])
    sl=merge(left,right)
    return sl
l4=[89,4,17,34,3,1]
sl=(mergesort(l4))
print(sl)