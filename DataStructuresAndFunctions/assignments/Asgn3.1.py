#Python program to print Highest Common Factor (HCF) of two numbers
n1,n2 = 12,8 #4
n1,n2 = 9,21 #3
n1,n2 = 7,5 #1

n1=int(input('first num: '))
n2=int(input('second num: '))

if(n1>n2):
  l,h=n1,n2
else:
  l,h=n2,n1
  
gcd = 1
for i in range(1,h):
  if(h%i==0 and l%i==0):
    gcd=i
print("gcd is {}".format(gcd))