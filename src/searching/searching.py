def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# ITERATIVE IMPLEMENTATION:
def binary_search(arr, target):
    if 0 < len(arr):
        start_pointer = 0
        end_pointer = len(arr) - 1
        while start_pointer <= end_pointer:
            target_pointer = (start_pointer + end_pointer) // 2
            if target < arr[target_pointer]:
                end_pointer = target_pointer
            elif arr[target_pointer] < target:
                start_pointer = target_pointer
            else:
                return target_pointer
    return -1


# RECURSIVE IMPLEMENTATION:
# def binary_search(arr, start_pointer, end_pointer, target):
#     if end_pointer >= start_pointer:
#         target_pointer = (start_pointer + end_pointer) // 2
#         if arr[target_pointer] == target:
#             return target_pointer
#         elif target < arr[target_pointer]:
#             return binary_search(arr, start_pointer, target_pointer-1, target)
#         else:
#             return binary_search(arr, target_pointer+1, end_pointer, target)
#     else:
#         return -1
