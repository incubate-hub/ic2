#91 write a program to check eligibility for voting

# input age
age = int(input("Enter Age : "))

if age>=18:
        status="Eligible"
else:
    status="Not Eligible"

print("You are ",status," for Vote.")

