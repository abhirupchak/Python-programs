# WAP tp create a pyramid of the character "*" and a revese pyramid 

def pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(1,i):
            print("*", end=" ")
        for l in range(2,i):
            print("*",end=" ")
        print()       
    print()
    for m in range(n,-1,-1):
        for g in range(n-m):
            print(" ", end=" ")
        for o in range(1,m):
            print("*", end=" ")
        for p in range(2,m):
            print("*",end=" ")
        print()   

pyramid(5)