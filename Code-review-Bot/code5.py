# Write a program to find the factorial of a number
num = 13
factorial = 1

if num < 0:
   print("No factorials for negative numbers!")

elif num == 0:
   print("The factorial of 0 is 1")

else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print(f"The factorial of {num} is {factorial}")

