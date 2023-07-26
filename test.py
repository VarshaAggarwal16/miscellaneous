min = int(input("Enter the min : "))
max = int(input("Enter the max : "))
with open('results.txt', 'w') as f:
    for n in range(min,max+1):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    break

        else:
            print(n)
            print(file = f)
            print("", file = f)
            print((n), file = f)