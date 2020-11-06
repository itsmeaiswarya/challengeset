arr = [int(i) for i in input().split(' ', 2)]
n = arr[0]
S = arr[1]
sum = 0
if int(n) < int(S):
    k = int(S)/int(n)
    S -= (int(n)*int(k))
    sum += int(k)
    if int(n) > int(S) and int(S) != 0:
        sum += 1
elif int(n) > int(S):
    sum += S
print(sum)
