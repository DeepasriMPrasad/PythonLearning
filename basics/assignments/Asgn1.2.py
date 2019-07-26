#prime number using while loop only

numberList = [2549, 2525, 8171, 25, 6, 13469, 8, 4, 45135, 45139]

index = 0

while index < len(numberList):
  n = numberList[index]
  index= index+1
  if(n==0 or n==1):
    print("{} is special".format(n))
  else:
    i=2
    while(i<=int(n/2)+1):
      if(n % i == 0):
        print("{} is not prime, it's divisible by {}*{}".format(n,int(n/i),i))
        break
      i+=1
    else:
      print("{} is prime".format(n))