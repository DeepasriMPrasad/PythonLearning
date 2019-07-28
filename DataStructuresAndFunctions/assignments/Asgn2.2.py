#Assignment 2.2: Python Program to Sort Words in Alphabetic Order?
strInput = input("Enter a sentence ");
st = [i.lower() for i in strInput.split()]
st.sort()
s = '';
for i in st:
  s+= i+" "
print("Words Sorted : ({})".format(s))