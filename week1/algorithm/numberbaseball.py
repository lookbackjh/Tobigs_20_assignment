#include<vector>
#include <iostream>
#include<string>
# convert into python code 

def checkstrike(numa, numb):
    strike = 0
    for i in range(3):
        if numa[i] == numb[i]:
            strike += 1
    return strike

def checkball(numa, numb):
    ball = 0
    for i in range(3):
        for j in range(3):
            if i != j and (numa[i] == numb[j] ):
                ball += 1
    return ball

N=int(input())
num_map=[0]*1001
numbers=[]
strike=[]
ball=[]
for _ in range(N):
    number, s, b = map(int, input().split())
    numbers.append(number)
    strike.append(s)
    ball.append(b)
for i in range(100,1000):
    if '0' in str(i):
        continue
    # if there is multiple same number
    if len(set(str(i))) != 3:
        continue
    for j in range(N):
        if checkstrike(str(i), str(numbers[j])) != strike[j] or checkball(str(i), str(numbers[j])) != ball[j]:
            num_map[i] = 0
            break
        else:
            num_map[i] = 1
print(sum(num_map))