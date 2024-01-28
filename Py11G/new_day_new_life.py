#------------------------------------------------------------------------
print("Алгоритм підрахунком")
# Function to perform counting sort on the given array
def countingSort(array):
    size = len(array)
    print("Size: ", size)
    # Find the maximum element in the array to determine the size of the count array
    max_element = max(array)
    # Initialize an array to store the sorted output
    output = [0] * size
    print("Output: ", output)
    # Initialize a count array to store the count of each element
    count = [0] * (max_element + 1)
    print("Count: ", count)
    # Count the occurrences of each element in the input array
    for i in range(0, size):
        count[array[i]] += 1
        print(f"Count for counting at all {array[i]}: ", count)
    # Update the count array to store the cumulative count
    for i in range(1, max_element + 1):
        count[i] += count[i - 1]
        print("Recount by +: ", count)
    # Build the sorted output array using the count array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
        print("Shift: ", count)
    # Copy the sorted elements back to the original array
    for i in range(0, size):
        array[i] = output[i]
        print("Let's turn back: ", array)
    return array
# Test data
data = [3, 0, 0, 1, 0, 1, 3, 3, 3]
# Print the sorted array in ascending order
print(f"Sorted Array in Ascending Order: {countingSort(data)}")
#------------------------------------------------------------------------  
print("Завдання 4")
print("Алгоритм вставкою")
import timeit
import random
code_to_test_1 = """
def insertion_sort(nums):
    for i in range(1, len(nums)):
        items_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > items_to_insert:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = items_to_insert
random_list = [6, 2, 5, 8, 20, 27, 30, 41]
insertion_sort(random_list)
"""
elapsed_time_1 =  timeit.timeit(code_to_test_1, number=1)
print(f"Зиконано за: {elapsed_time_1}")
#------------------------------------------------------------------------  
print("Алгоритм злиттям")
code_to_test_2 = """
def merge_sort(list):
    length = len(list)
    if length == 1:
        return list
    mid = length // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)
def merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output
unsorted = [6, 2, 5, 8, 20, 27, 30, 41]
sorted = merge_sort(unsorted)
"""
elapsed_time_2 =  timeit.timeit(code_to_test_2, number=1)
print(f"Зиконано за: {elapsed_time_2}")
#------------------------------------------------------------------------  
print("Алгоритм підрахунком")
code_to_test_3 = """
def countingSort(array):
    size = len(array)
    max_element = max(array)
    output = [0] * size
    count = [0] * (max_element + 1)
    for i in range(0, size):
        count[array[i]] += 1
    for i in range(1, max_element + 1):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]
    return array
data = [6, 2, 5, 8, 20, 27, 30, 41]
"""
# #------------------------------------------------------------------------  
# print("Алгоритм підрахунком з вікіпедії")
# code_to_test_3 = """
# a = [6, 2, 5, 8, 20, 27, 30, 41]
# cnt = [0] * (max(a) + 1)
# for item in a:
#     cnt[item] += 1
# result = [num for num, count in enumerate(cnt) for i in range(count)] 
# print(result)
# """
elapsed_time_3 =  timeit.timeit(code_to_test_3, number=1)
print(f"Зиконано за: {elapsed_time_3}")
mas = [elapsed_time_1, elapsed_time_2, elapsed_time_3]
best = min(mas)
print(f"Найкращий час: {best} = Найкращий код {mas.index(best)+1}")
import math
mas = [8**2, 8*math.log(8), 8+8]#O(n^2), O(nlog n), O(n+k)
best = min(mas)
print(f"Найкращий книжковий час: {best} = Найкращий код {mas.index(best)+1}")
print("PS:\nЯкщо хочете спробувати довщий: [random.randint(0, 100000) for _ in range(20000)]\nВставте замість [6, 2, 5, 8, 20, 27, 30, 41]")