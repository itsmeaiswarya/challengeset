n = int(input())
List = []
for i in range(int(n)):
    List.append(input())

for i in range(int(n)):
    t = List[i]
    if int(len(t)) <= 10:
        print(t)

    elif int(len(t)) > 10:
        i2 = int(len(t))-2

        for j in range(int(len(t))):
            i1 = t[0]
            i3 = t[len(t)-1]
        print(i1+str(i2)+i3)



