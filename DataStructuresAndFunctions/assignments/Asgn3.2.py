def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide (a,b):
    if(a == 0 or b== 0):
      return "Not a number"
    else:
      return a/b
    
def calculator(choice, num1, num2):
  operationList = [("Sum","+",add), ("Difference",'-', subtract), ("Product","*",multiply), ("Quotient","/",divide)]
  for index, operation in enumerate(operationList,1):
    if choice == index:
      print( str(operation[0] + " of {} "+operation[1]+" {} is: {}").format(num1, num2, operation[2](num1,num2)))

def printSelection(choice):
  selectionList = ["Addition","Subtraction","Multiplication","Division"]
  for ind, selection in enumerate(selectionList,1):
    if int(choice) == ind:
      print("You have chosen {}".format(selection))
      break
    
        
while True:
  print("---------------------------------------------------------------------")
  choice = input("Simple Calculator: Enter 1-Addition; 2-Subtraction; 3-Multiply; 4-Divide; 0-To Quit ")
  if choice  not in ['1','2','3','4']:
    print("Exiting simple calculator...")
    break
  else:
    printSelection(choice)
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    calculator(int(choice),n1,n2)