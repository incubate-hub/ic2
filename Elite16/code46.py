#88 write a program to find variance of a dataset

def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot = tot + (x - mean)**2
    return tot/len(X)

# main code
#  a simple data-set 
sample = [1, 2, 3, 4, 5] 
print("variance of the sample is: ", variance(sample))

