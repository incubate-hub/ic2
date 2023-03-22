# Write a function that returns the sum of digits of a given number
def digisum(num):
    sum_=0
    while num > 0:
        dig = num % 10
        sum_+=dig
        num//=10
    return sum_