## Assignment 3.3: Python program to display the fibonacci sequence up to n-th term using recursive function
def fib(n):
    if n ==0 or n==1:
      return 1
    else: 
      return fib(n-1) + fib (n-2);
    
 
def fibNonRecursive(n):
  i,n1,n2,fib = 0,0,0,0;
  while(i <= n):
    if(i==1 or i==0):
      n1,n2,fib = 1,1,1
    else:
      fib = n1 + n2
      n2 = n1;
      n1= fib;
    i+=1
  return fib
   
  
n1 = int(input("Enter the number of Fibonacci numbers: "))
ls, ls2 = [],[]
for n in range(0,n1):
  ls.append(fib(n))
  ls2.append(fibNonRecursive(n))
print(ls)  
print(ls2)