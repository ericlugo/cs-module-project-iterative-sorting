# checks if positions are valid then, if true, performs swap
def swap_positions(arr, pos1, pos2):
    if (pos1 in range(0, len(arr))) and (pos2 in range(0, len(arr))) and (pos1 != pos2):
        arr[pos1], arr[pos2] = arr[pos2], arr[pos1]


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        swap_positions(arr, i, smallest_index)
    return arr


def bubble_sort(arr):
    end_of_list = len(arr)-1
    while 0 < end_of_list:
        current_index = 0
        while current_index < end_of_list:
            if arr[current_index+1] < arr[current_index]:
                swap_positions(arr, current_index, current_index+1)
            current_index += 1
        end_of_list -= 1
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):

    max_value = None
    if maximum is not None:
        max_value = maximum + 1
    elif 0 < len(arr):
        max_value = max(arr) + 1

    if (max_value is not None) and (0 < max_value):
        counting_list = [0]*max_value
        for value in arr:
            if 0 <= value:
                counting_list[value] += 1
            else:
                return "Error, negative numbers not allowed in Count Sort"

        main_index = 0
        for i in range(len(counting_list)):
            while 0 < counting_list[i]:
                arr[main_index] = i
                counting_list[i] -= 1
                main_index += 1

    return arr
