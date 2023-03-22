# Write a program to check whether a number is prime or not
num = 337

if num > 1:
   for i in range(2, num//2 + 1):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(f"{i} times {num//i} is {num}")
           break
   else:
       print(f"{num} is a prime number")

else:
   print(f"{num} is not a prime number")
