N=int(input())
arr=[0]*10
while N/10>0:
    cur_num=N%10
    N=N//10
    arr[cur_num]+=1
cur_max=-1
for i in range(10):
    if i==6 or i==9:
        cur_max=max(cur_max,(arr[6]+arr[9]+1)//2)
    else:
        cur_max=max(cur_max,arr[i])
print(cur_max)