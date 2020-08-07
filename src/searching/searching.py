def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    if 0 < len(arr):
        start_pointer = 0
        end_pointer = len(arr) - 1
        target_pointer = end_pointer // 2
        while (start_pointer != target_pointer) and (end_pointer != target_pointer):
            if arr[target_pointer] == target:
                return target_pointer
            elif target < arr[target_pointer]:
                end_pointer = target_pointer
            else:
                start_pointer = target_pointer
            target_pointer = start_pointer + ((end_pointer-start_pointer) // 2)
    return -1
