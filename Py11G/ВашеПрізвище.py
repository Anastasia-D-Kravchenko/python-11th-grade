import random
def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    mid = length // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
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
with open("input.txt", "w") as f:
    f.write(" ".join(map(str, [random.randint(1, 1000) for _ in range(2000)])))
with open("input.txt", "r") as f:
    A = list(map(int, f.readline().split()))
with open("output.txt", "w") as f:
    f.write(" ".join(map(str, merge_sort(A))) + "\n")