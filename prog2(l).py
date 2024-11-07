# 2.l. Generate first n prime numbers
def genrateprime():
    flag=False
    count=0
    i=2
    while(count<n):
        flag=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                flag=False
                break
            else:
                flag=True
        if flag :
            print(i)
            count+=1
        i+=1
n=int(input("enter the amount of primes you want"))
genrateprime()
