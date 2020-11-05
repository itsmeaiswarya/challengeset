n = input()
a = []
X = 0
for i in range(int(n)):
    a.append(input())

    if '+' in a[i]:
        X = X + 1

    if '-' in a[i]:
        X = X - 1
print(X)
