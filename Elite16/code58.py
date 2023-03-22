# Write a python program to Implement Binary Search with Recursion and print the key element if found

def binary_search_rec(alist, start, end, key):
    """Search key in alist[start... end - 1]."""
    if not start < end:
        return -1
 
    mid = (start + end)//2
    if alist[mid] < key:
        return binary_search_rec(alist, mid + 1, end, key)
    elif alist[mid] > key:
        return binary_search_rec(alist, start, mid, key)
    else:
        return mid
 
 
alist = [2, 3, 5, 6, 4, 5]

key = 6
 
index = binary_search_rec(alist, 0, len(alist), key)
if index < 0:
    print(f'{key} was not found.')
else:
    print(f'{key} was found at index {index}.')
