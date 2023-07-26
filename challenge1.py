x=int(input("Enter the lowest number: "))
y=int(input("Enter the highest number"))
with open("challenge.txt","w") as f:
    for n in range (x,y):
        if all(n%i!=0 for i in range (2,n)):
            a=[]
            a.append(n)
            print (a)
            print ((a), file = f)