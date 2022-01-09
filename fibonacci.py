x = int(input("Enter the Number of terms:"))

n1, n2 = 0, 1
count = 0
if x <= 0:
   print("Please enter a positive integer")
elif x == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < x:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
