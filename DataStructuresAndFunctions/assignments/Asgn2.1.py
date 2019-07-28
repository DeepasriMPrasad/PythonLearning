# Assignment 2.1: Python Program to Check where a String is Palindrome or not ?
strInputLst = ["ababa", "aa", "abc", "aba", "ababababa"]

for string in strInputLst:
  revCharLst = []
  revCharLst = [i for i in string]
  charLst = revCharLst.copy()
  revCharLst.reverse()
  if(charLst == revCharLst):
    print("{} is a palindrome".format(string))
  else:
    print("{} in not a palindrome".format(string))