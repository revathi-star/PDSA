
#Quick Sort
def partition(l,lower,upper):
    pivot=l[lower]
    i=lower
    for j in range(lower+1,upper+1):
        if l[j]<=pivot:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[lower],l[i]=l[i],l[lower]#place the pivot in its right position 
    return i
def quicksort(l,lower,upper):
    if (lower<upper):
        pivot_pos=partition(l,lower,upper)
        quicksort(l,lower,pivot_pos-1)
        quicksort(l,pivot_pos+1,upper)
    return l

l=[78,2,5,2,1,7]
print(quicksort(l,0,5))

#LinkedList
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def isempty(self):
        return self.head==None
    
    def append(self,data):
        if self.isempty():
            self.head=Node(data)
        else:
            temp=self.head #helps in traversing upto the end position
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(data)
    
    def delete(self,v):
        #if list is empty
        if self.isempty():
            return 'List is empty'
        #if element v is found in the first location itself
        if self.head.data==v:
            self.head=self.head.next
            return
        #if element v is found somewhere in the linked list
        temp=self.head
        temp1=self.head
        while temp.next!=None and temp.data!=v:#until we reach the end of the list or until the node whose value we want to delete is not reached
            temp1=temp
            temp=temp.next
        if temp.data==v:
            temp1.next=temp.next
            return
        #if element v does not exist
        if temp.next==None:
            return 'Element v does not exist'
        
    def display(self):
        temp=self.head
        while temp.next!=None:
            print(temp.data,end=',')
            temp=temp.next
        print(temp.data)
l1=[5,9,1,4,3]
l2=LinkedList()
for v in l1:
    l2.append(v)
l2.display()
l2.delete(4)
print('\n')
l2.display()
l2.append(10)
print('\n')
l2.display()

#Stacks
class Stack:
    def __init__(self):
        self.stack=[]

    def isempty(self):
        return self.stack==[]

    def push(self,v):
        self.stack.append(v)

    def pop(self):
        v=None
        if not self.isempty():
            v=self.stack.pop()
        return v
    
    def __str__(self):
        return str(self.stack)

st=Stack()
st.push(10)
st.push(20)
st.push(30)
print(st)
print(st.pop()) #30
print(st.pop()) #20
print(st)

# Queues
class Queue:
    def __init__(self):
        self.queue=[]

    def isempty(self):
        return self.queue==[]
    
    def enqueue(self,v):
        self.queue.append(v)

    def dequeue(self):
        v=None
        if not self.isempty():
            v=self.queue[0]
            self.queue=self.queue[1:]
        return v

    def __str__(self):
        return str(self.queue)
    
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q)
print(q.dequeue())#10
print(q.dequeue())#20
print(q)