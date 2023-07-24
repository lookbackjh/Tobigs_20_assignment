N=int(input())
#2차원 배열 선언
arr=[[0]*(101) for _ in range(101)]
for _ in range(N):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1

ans=0
for i in range(1,101):
    for j in range(1,101):
        ans+=arr[i][j]
print(ans)