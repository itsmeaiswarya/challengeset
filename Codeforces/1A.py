n, m, a = map(int, input().split())
if n % a == 0:
    f1 = n//a
else:
    f1 = n//a + 1

if m % a == 0:
    f2 = m//a
else:
    f2 = m//a + 1

print(f1*f2)
