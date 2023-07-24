N = int(input())
ans=[]
for _ in range(N):
    a, b = map(int, input().split())
    b=b%4
    if b==0:
        b=4
    p=(a**b)%10
    if p==0:
        ans.append(10)
    else:
        ans.append(p)
for i in ans:
    print(i)