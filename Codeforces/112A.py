a = input()
b = input()
n = int(len(a))

if a.upper() == b.upper():
    print('0')
    
for i in range(int(n)):
    if a[i].upper() < b[i].upper():
        print('-1')
        break
    if a[i].upper() > b[i].upper():
        print('1')
        break
