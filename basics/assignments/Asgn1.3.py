#Python Program to display all prime numbers within an interval
for n in range(1,51):
  if(n==1 or n==0):
    print("{} is special".format(n))
  else:
    print("---------------------------------------\n")
    for i in range(2, int(n/2)+1):
      if(n % i == 0):
        print("{} is not a prime number, it's divisible by {}*{}".format(n,i,int(n/2)))
        break
    else: print("{} is a prime number".format(n))