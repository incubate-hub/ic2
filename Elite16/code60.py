# Write a python program to Implement Insertion sort and print the sorted list for the below list

def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
 
 
alist = [2, 3, 5, 6, 4, 5]
insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)