#Implementation Using a For Loop
prev2=0
prev1=1
print(prev2,end=' ')
print(prev1,end=' ')
for fibo1 in range(18):
    newFibo1=prev2+prev1
    print(newFibo1,end=' ')
    prev2=prev1
    prev1=newFibo1
print('\n')

#Implementation Using Recursion
print(0,end=' ')
print(1,end=' ')
count=2
def fibonacci(prev3,prev4):
    global count
    if count<=19:
        newFibo2=prev3+prev4
        print(newFibo2,end=' ')
        prev3=prev4
        prev4=newFibo2
        count+=1
        fibonacci(prev3,prev4)
    else:
        return

fibonacci(0,1)
print('\n')

#Finding The nth Fibonacci Number Using Recursion
def F(n):
    if n<=1:
        return n
    else:
        return F(n-1)+F(n-2)

for i in range(20):
    print(F(i),end=' ')