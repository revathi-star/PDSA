def linear_search(list,ele):
    for i in range(len(list)):
        if list[i]==ele:
            return i
    return -1

def binary_search(list,ele): #List should be sorted
    low,high=0,len(list)-1
    while low<=high:
        mid=(low+high)//2
        if ele==list[mid]:
            return mid
        elif ele>list[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

def binary_search_recur(list,ele):
    def helper(low,high):
        if low>high:
            return -1
        mid=(low+high)//2
        if list[mid]==ele:
            return mid
        elif list[mid]>ele:
            return helper(low,mid-1)
        else:
            return helper(mid+1,high)
    return helper(0,len(list)-1)
    
def ternary_search(list,ele):
    low,high=0,len(list)-1
    while low<=high:
        mid1=low+((high-low)//3)
        mid2=high-((high-low)//3)
        if list[mid1]==ele:
            return mid1
        if list[mid2]==ele:
            return mid2
        if list[mid1]>ele:
            high=mid1-1
        elif list[mid2]<ele:
            low=mid2+1
        else:
            low=mid1+1
            high=mid2-1
    return -1

def rotated_binary_search(list,ele):
    low,high=0,len(list)-1
    if list[high]>list[low]:
        return list[high]
    while low<high:
        mid=(low+high)//2
        if list[mid]>list[high]:
            low=mid+1
        else:
            high=mid
    return list[low-1]

def selection_sort(list):
    n=len(list)
    for i in range(n-1):
        mini=list[i]
        pos=i
        for j in range(i+1,n):
            if list[j]<mini:
                mini=list[j]
                pos=j
        list[i],list[pos]=list[pos],list[i]

def insertion_sort(l):
    n=len(list)
    for i in range(1,n):
        temp=l[i]
        j=i-1
        while j>=0 and temp<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=temp

def merge(arr,low,mid,high):
    left=arr[low:mid+1]
    right=arr[mid+1:high]
    i,j,k=0,0,low
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1


def merge_sort(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)

from random import randint

def partition(arr,low,high):
    pivot_index=randint(low,high)
    arr[low],arr[pivot_index]=arr[pivot_index],arr[low]
    pivot=arr[low]
    start=low
    end=high
    while start<end:
        while start<high and pivot>=arr[start]:
            start+=1
        while end>low and pivot<arr[end]:
            end-=1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
    arr[low],arr[end]=arr[end],arr[low]
    return end
    
def quick_sort(arr,low,high):
    if low>=high:
        return 
    end=partition(arr,low,high)
    quick_sort(arr,low,end-1)
    quick_sort(arr,end+1,high)

def quick_select(arr,k):
    if k<0 or k>=len(arr):
        return -1
    low,high=0,len(arr)-1
    pivot=partition(arr,low,high)
    if pivot==k:
        return arr[pivot]
    elif pivot<k:
        low=pivot+1
    else:
        high=pivot-1

def mom(lis):
    if len(lis)<=5:
        lis.sort()
        return sorted(lis)[len(lis)//2]
    nlist=[]
    for i in range(0,len(list),5):
        tlist=lis[i:i+5]
        tlist.sort()
        nlist.append((tlist)[len(tlist)//2])
    return mom(nlist)

def mom_partition(arr,low,high):
    ele=mom(arr[low:high+1])
    pivot_index=-1
    for i in range(low,high+1):
        if arr[i]==ele:
            pivot_index=i
            break
    arr[low],arr[pivot_index]=arr[pivot_index],arr[low]
    pivot=arr[low]
    start=low
    end=high
    while start<end:
        while start<high and pivot>=arr[start]:
            start+=1
        while end>low and pivot<arr[end]:
            end-=1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
    arr[low],arr[end]=arr[end],arr[low]
    return end

def fast_select(arr,k):
    if k<0 or k>=len(arr):
        return -1
    low,high=0,len(arr)-1
    while low<=high:
        pivot=mom_partition(arr,low,high)
        if pivot==k:
            return arr[pivot]
        elif pivot<k:
            low=pivot+1
        else:
            high=pivot-1