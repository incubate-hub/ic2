#93 write a program to find sum of all digits of a number

def sumDigits(num):
  if num == 0:
    return 0
  else:
    return num % 10 + sumDigits(int(num / 10))

x = 0
print("Number: ", x)
print("Sum of digits: ", sumDigits(x))
print()
