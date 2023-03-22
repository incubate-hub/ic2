
# Write a python program to Implement Selection sort and print the sorted list for the below list

def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
 
 
alist = [2, 3, 5, 6, 4, 5]
selection_sort(alist)
print('Sorted list: ', end='')
print(alist)
