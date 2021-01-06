h=input("Enter number of columns b/w 3 & 100:")
w=input("Enter number of rows b/w 3 & 100:")
x=(int(min(w,h))+1)/4
k=range(1,int(x)+1)
print("Number of possible rings:")
for i in k:
    print(i)
ring=input("Chose no of rings to be gild(golden) among options given above:")
if ring==1:
    output=(2*int(w))+(2*(int(h)-2))
    print(int(output))
