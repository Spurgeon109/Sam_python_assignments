n = int(input("enter the number :"))

for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    for k in range(n, i, -1):
        print(k, end=" ")
    print("\n")