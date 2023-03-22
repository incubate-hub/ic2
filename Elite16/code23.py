# initializing string  
test_str = "HellowWorld"

print("The original string is : " + test_str) 
res = ', '.join(test_str[i:i + 2] for i in range(0, len(test_str), 2)) 
 
print("The string after inserting comma after every character pair : " + res) 

