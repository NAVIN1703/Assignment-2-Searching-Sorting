#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14]
target = 8
index = binary_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print("Element not found")


# In[2]:


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Example usage:
arr = [5, 2, 8, 3, 1, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)


# In[3]:


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)

# Example usage:
arr = [5, 2, 8, 3, 1, 7]
sorted_arr = quick_sort(arr)
print(sorted_arr)


# In[4]:


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

# Example usage:
arr = [5, 2, 8, 3, 1, 7]
sorted_arr = insertion_sort(arr)
print(sorted_arr)


# In[5]:


def sort_list_of_strings(strings):
    sorted_strings = sorted(strings)
    return sorted_strings

# Example usage:
strings = ["apple", "banana", "cherry", "date", "berry"]
sorted_strings = sort_list_of_strings(strings)
print(sorted_strings)


# In[ ]:




