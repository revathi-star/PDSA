"""
import time
import sys 
sys.setrecursionlimit(100000000)
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_rec(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fib_rec(n-1)+fib_rec(n-2)

start1=time.perf_counter()
fib_iter(20)
end1=time.perf_counter()
result1=(float(end1)-float(start1))

start2=time.perf_counter()
fib_rec(20)
end2=time.perf_counter()
result2=(float(end2)-float(start2))

if result1>result2:
    print('iterative wins')
else:
    print('recursion wins')

print(fib_iter(20))
print(fib_rec(20))
"""

"""class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def tree_sum(root):
    if root is None:
        return 0
    return root.value+tree_sum(root.left)+tree_sum(root.right)
if (__name__)=="__main__":
    root=Node(10)
    root.left=Node(5)
    root.right=Node(15)
    root.left.left=Node(3)
    root.left.right=Node(7)
    total=tree_sum(root)
    print(total)
"""
# l=list(map(int,input().split()))
# max_value=l[0]
# for i in range(1,len(l)):
#     if l[i]>max_value:
#         max_value=l[i]
# print(max_value)

l=list(map(int,input().split()))
flag=True
for i in range(len(l)-1):
    if l[i]<=l[i+1]:
        flag=True
    else:
        flag=False
        break
print(flag)