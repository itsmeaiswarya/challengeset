n = int(input())
arr = [int(i) for i in input().split(' ', n)]
num = 0
for i in range(int(n)):
    if int(arr[i]) == 1:
        num += 1

if num >= 1:
    print("HARD")

if num == 0:
    print("EASY")

