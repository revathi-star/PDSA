def fibo_rec(n):
    if n<=1:
        return n
    return fibo_rec(n-1)+fibo_rec(n-2)

d={}
def memo_fib(n):
    if n<=1:
        return n
    if n in d:
        return d[n]
    d[n]=memo_fib(n-1)+memo_fib(n-2)
    return d[n]

def dp_fib(n):
    if n<=1:
        return n
    fib=[0]*n
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[-1]

def dp_space_fib(n):
    if n<=1:
        return n
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return b

def grid_paths(grid):
    dp=[[0]*(len(grid[0])) for _ in range(len(grid))]
    if grid[0][0]=='.':
        dp[0][0]=1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==0 and j==0:
                continue
            if grid[i][j]=='x':
                continue
            if i==0:
                dp[i][j]=dp[i][j-1]
            elif j==0:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[-1][-1]

def recur_minimum_coins(value,coins):
    if value==0:
        return 0
    mini=float('inf')
    for i in coins:
        val=float('inf')
        if value>=i:
            val=1+recur_minimum_coins(value-i,coins)
        mini=min(mini,val)
    return mini

d={}
def memo_mini_coins(value,coins):
    if value==0:
        return 0
    if value in d:
        return d[value]
    mini=float('inf')
    for i in coins:
        val=float('inf')
        if value>=i:
            val=1+memo_mini_coins(value-i,coins)
        mini=min(val,mini)
    d[value]=mini
    return mini

def dp_minimum_coins(value,coins):
    dp=[float('inf')]*(value+1)
    dp[0]=0
    for i in range(1,value+1):
        for j in coins:
            if i>=j:
                dp[i]=min(dp[i],dp[i-j]+1)
    return dp[-1]

def rec_knapsack(i,cap,wt,prof):
    if i==len(wt)-1:
        return prof[i] if wt[i]<=cap else 0
    
    not_take=rec_knapsack(i+1,cap,wt,prof)

    take=float('-inf')
    if wt[i]<=cap:
        take=prof[i]+recur_minimum_coins(i+1,cap-wt[i],wt,prof)
    
    ans=max(take,not_take)

    return ans

d={}
def memo_knapsack(i,cap,wt,prof):
    if i==len(wt)-1:
        return prof[i] if wt[i]<=cap else 0
    if (i,cap) in d:
        return d[(i,cap)]
    not_take=memo_knapsack(i+1,cap,wt,prof)
    take=float('-inf')
    if wt[i]<=cap:
        take=prof[i]+memo_knapsack(i+1,cap-wt[i],wt,prof)
    d[(i,cap)]=max(not_take,take)
    return d[((i,cap))]

def dp_knapsack(cap,wt,prof):
    n=len(wt)
    dp=[[0]*(cap+1) for _ in range(n)]

    for c in range(cap+1):
        if wt[0]<=c:
            dp[0][c]=prof[0]
    
    for i in range(1,n):
        for c in range(cap+1):
            not_take=dp[i-1][c]
            take=float('-inf')
            if wt[i]<=c:
                take=prof[i]+dp[i-1][c-wt[i]]
            dp[i][c]=max(not_take,take)

    return dp[-1][-1]
