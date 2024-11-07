#WAP to check if number is prime number
n=int(input("enter number to be checked:"))
def prime(n):
  flag=0
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      flag=1
      break
    else:
      flag=0
  if flag==0:
    print("prime")
  else:
    print("not prime")
prime(n)
