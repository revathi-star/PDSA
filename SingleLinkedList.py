class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def insert_begin(self,data=None):
        temp=Node(data)
        if self.head:
            temp.next=self.head
            self.head=temp
        else:
            self.head=temp
            self.tail=temp
        self.count+=1
    def insert_end(self,data=None):
        temp=Node(data)
        if self.head:
            self.tail.next=temp
            self.tail=temp
        else:
            self.head=temp
            self.tail=temp
        self.count+=1
    def insert_pos(self,data=None,pos=None):
        if pos<1 or pos>self.count + 1:
            print('Invalid position specified')
        elif pos==1:
            self.insert_begin(self,data)
        elif pos==self.count+1:
            self.insert_end(self,data)
        else:
            temp=Node(data)
            temp1=self.head
            i=2
            while i<pos-1:
                temp1=temp1.next
            temp.next=temp1.next
            temp1.next=temp
            self.count+=1
    def delete_begin(self):
        if self.head is None:
            print('Underflow')
        elif self.head.next is None:
            print('Deleted',self.head.data)
            self.head=None
            self.tail=None
            self.count-=1
        else:
            print('Deleted',self.head.data)
            self.head=self.head.next
            self.count-=1
    def delete_end(self):
        if self.head==None:
            print('Underflow')
        elif self.head.next==None:
            print('Deleted',self.head.data)
            self.head=None
            self.tail=None
            count-=1
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            print('Deleted',self.tail.data)
            temp.next=None
            self.tail=temp
            self.count-=1 
    def delete_pos(self,pos):
        if pos<1 or pos>self.count:
            print('Invalid position')
        elif pos==1:
            self.delete_begin()
        elif pos==self.count:
            self.delete_end()
        else:
            i=2
            temp=self.head
            while i<pos:
                temp=temp.next
                i+=1
            print('Deleted',temp.next.data)
            temp.next=temp.next.next
            count-=1
    def display(self):
        if self.head==None:
            print('List is empty')
        else:
            temp=self.head
            print('The elements are:')
            while temp:
                print(temp.data,end=' ')
                temp=temp.next
            print()
    def search(self,ele):
        temp=self.head
        f=False
        i=1
        while temp:
            if temp.data==ele:
                f=True
                break
            i+=1
            temp=temp.next
        if f:
            print('The element is present at index',i)
        else:
            print('The element is not present in the list')
    def reverse(self):
        if self.head is None:
            print('List is empty')
        prev=None
        curr=self.head
        while curr:
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
        self.head,self.tail=self.tail,self.head
        print('List reversed successfully')

if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.insert_end(10)
    sll.insert_end(20)
    sll.insert_begin(5)
    sll.insert_pos(15, 3)
    sll.display()
    sll.reverse()
    sll.display()
    sll.delete_begin()
    sll.display()
    sll.delete_end()
    sll.display()
    sll.delete_pos(2)
    sll.display()
    sll.search(15)
    sll.display()