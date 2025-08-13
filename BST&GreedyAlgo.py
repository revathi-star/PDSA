class BSTNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST:
    node=BSTNode()
    def __init__(self):
        self.root=BSTNode(None)
    
    def is_empty(self):
        return self.root is None
    
    def preorder(self):
        def func(node):
            if node is None:
                return []
            return [node.value]+func(node.left)+func(node.right)
        return func(self.root)
    
    def inorder(self):
        def func(node):
            if node is None:
                return []
            return func(node.left)+[node.value]+func(node.right)
        return func(self.root)
    
    def postorder(self):
        def func(node):
            if node is None:
                return []
            return func(node.left)+func(node.right)+[node.value]
        return func(self.root)
    
    def search(self,value):
        def func(node,value):
            if node is None:
                return False
            if node.value==value:
                return True
            if node.value<value:
                return func(node.right,value)
            else:
                return func(node.left,value)
        return func(self.root,value)
    
    def minval(self):
        if self.is_empty():
            return None
        node=self.root
        while node.left:
            node=node.left
        return node.value
    
    def maxval(self):
        if self.is_empty():
            return None
        node=self.root
        while node.right:
            node=node.right
        return node.value
    
    def insert(self,value):
        def func(node,value):
            if node is None:
                return BSTNode(value)
            if node.value==value:
                return node
            if value<node.value:
                node.left=func(node.left,value)
            else:
                node.right=func(node.right,value)
            return node
        self.root=func(self.root,value)

    def delete(self,value):
        def func(node,value):
            if node is None:
                return node
            if value>node.value:
                node.right=func(node.right,value)
            elif value<node.value:
                node.left=func(node.left,value)
            else:
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    temp=node.right
                    while temp.left:
                        temp=temp.left
                    node.value=temp.value
                    node.right=func(node.right,value)
            return node
        self.root=func(self.root,value)

def interval_scheduling(intervals):
    intervals.sort(key=lambda x:x[1])
    selected_intervals=[]
    last_end_time=-1
    for start,end in intervals:
        if start>=last_end_time:
            selected_intervals.append((start,end))
            last_end_time=end
    return selected_intervals

def minimize_lateness(tasks):
    tasks.sort(key=lambda x:x[1])
    current_time=0
    max_lateness=0
    cnt=0
    sum_lateness=0
    for processing_time,deadline in tasks:
        start=current_time
        end=start+processing_time
        current_time=end
        lateness=max(0,end-deadline)
        max_lateness=max(max_lateness,lateness)
        sum_lateness+=lateness
        if lateness>0:
            cnt+=1
    return max_lateness,cnt,sum_lateness

import heapq

class Huffman_node:

    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None

    def __lessthan_(self,other):
        return self.freq<other.freq
    
    def __str__(self):
        return f"Node({self.char},{self.freq})"
    
def build_huffman_tree(self,freq):
    heap=[Huffman_node(char,freq) for char,freq in freq.items()]
    heapq.heapify(heap)
    while len(heap)>1:
        left=(heapq.heappop(heap))
        right=(heapq.heappop(heap))
        merged=Huffman_node(None,left.freq+right.freq)
        merged.left=left
        merged.right=right
        heapq.heappush(heap,merged)
    return heap[0]

def generate_huffman_codes(root,prefix='',huffman_codes={}):
    if root:
        if root.char is not None:
            huffman_codes[root.char]=prefix
        generate_huffman_codes(root.left,prefix+'0',huffman_codes)
        generate_huffman_codes(root.right,prefix+'1',huffman_codes)
    return huffman_codes

def huffman_encoding(text):
    if not text:
        return '',{}
    freq={}
    for char in text:
        if char in  freq:
            freq[char]+=1
        else:
            freq[char]=1
    root=build_huffman_tree(freq)
    huffman_code=generate_huffman_codes(root,'',{})
    encoded_text=''.join(huffman_code[char] for char in text)
    return encoded_text,huffman_code

def huffman_decoding(encoded_text,huffman_codes):
    if not encoded_text or not huffman_codes:
        return ''
    reverse_code={code:char for char,code in huffman_codes.items()}
    decoded_text=''
    temp_code=''
    for bit in encoded_text:
        temp_code+=bit
        if temp_code in reverse_code:
            decoded_text+=reverse_code[temp_code]
            temp_code=''
    return decoded_text,reverse_code

class AVLNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=1

class AVLTree:
    node=AVLNode()
    def __init__(self):
        self.root=AVLNode(None)

    def is_empty(self):
        return self.root is None
    
    def preorder(self):
        def func(node):
            if node is None:
                return []
            return [node.value]+func(node.left)+func(node.right)
        return func(self.root)
    
    def inorder(self):
        def func(node):
            if node is None:
                return []
            return func(node.left)+[node.value]+func(node.right)
        return func(self.root)
    
    def postorder(self):
        def func(node):
            if node is None:
                return []
            return func(node.left)+func(node.right)+[node.value]
        return func(self.root)
    
    def search(self,value):
        def func(node,value):
            if node is None:
                return False
            if node.value==value:
                return True
            if value<node.value:
                return func(node.left,value)
            else:
                return func(node.right,value)
        return func(self.root,value)

    def minvalue(self):
        if self.is_empty():
            return None
        node=self.root
        while node.left:
            node=node.left
        return node.value

    def maxvalue(self):
        if self.is_empty():
            return None
        node=self.root
        while node.right:
            node=node.right
        return node.value

    def height(self,node):
        return node.height if node else 0   

    def slope(self,node):
        return self.height(node.left)-self.height(node.right) if node else 0

    def right_rotate(self,y):
        x=y.left
        T2=x.right
        x.right=y
        y.left=T2
        y.height=1+max(self.height(y.left),self.height(y.right))
        x.height=1+max(self.height(x.left),self.height(x.left))
        return x

    def left_rotate(self,x):
        y=x.right
        T2=y.left
        y.left=x
        x.right=T2
        y.height=1+max(self.height(y.left),self.height(y.right))
        x.height=1+max(self.height(x.left),self.height(x.right))
        return y   
    
    def rebalance(self,node):
        slope=self.slope(node)
        if slope>1:
            if self.slope(node.left)<0:
                node.left=self.left_rotate(node.left)
            return self.right_rotate(node)
        if slope<-1:
            if self.slope(node.right)>0:
                node.right=self.right_rotate(node.right)
            return self.left_rotate(node)
        return node
    
    def insert(self,value):
        def func(node,value):
            if not node:
                return AVLNode(value)
            if value<node.value:
                node.left=func(node.left,value)
            elif value>node.value:
                node.right=func(node.right,value)
            else:
                return node
            node.height=1+max(self.height(node.left),self.height(node.right))
            return self.rebalance(node)
        self.root = func(self.root,value)

    def delete(self,value):
        def func(node,value):
            if not node:
                return node
            if value<node.value:
                node.left=func(node.left,value)
            elif value>node.value:
                node.right=func(node.right,value)
            else:
                if not node.left and not node.right:
                    return None
                elif not node.right:
                    return node.left
                elif not node.left:
                    return node.right
                else:
                    temp=node.right
                    while temp.left:
                        temp=temp.left
                    node.value=temp.value
                    node.right=func(node.right,value)
                node.height=1+max(self.height(node.left),self.height(node.right))
                return self.rebalance(node)
            self.root=func(self.root,value)
            