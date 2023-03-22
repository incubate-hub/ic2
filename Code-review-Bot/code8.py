
# Write a program to filter the numbers in a list which are divisible by a given number
my_list = [11, 45, 74, 89, 132, 239, 721, 21]

num = 3
result = list(filter(lambda x: (x % num == 0), my_list))

print(f"Numbers divisible by {num} are {result}")