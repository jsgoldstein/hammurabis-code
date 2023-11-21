import random
import time
from typing import List


def max_subarray(array: List[int]) -> int:
    max_subarray = array[0]
    i = 0
    while i < len(array):
        j = i + 1
        while j <= len(array):
            if sum(array[i:j]) > max_subarray:
                max_subarray = sum(array[i:j])
            j = j + 1
        i = i + 1
    return max_subarray


def max_subarray_recursive(array: List[int], left: int, right: int) -> int:
    if left == right:
        return array[left]

    middle = (left + right) // 2
    left_sum = max_subarray_recursive(array, left, middle)
    right_sum = max_subarray_recursive(array, middle + 1, right)
    mid_sum = max_subarray_middle(array, left, middle, right)

    return max(left_sum, right_sum, mid_sum)


def max_subarray_middle(array: List[int], left: int, middle: int, right: int) -> int:
    left_sum = float('-inf')
    curr_sum = 0

    left_index = middle
    while left_index >= left:
        curr_sum = curr_sum + array[left_index]
        if curr_sum > left_sum:
            left_sum = curr_sum
        left_index = left_index - 1

    right_sum = float('-inf')
    curr_sum = 0

    right_index = middle + 1
    while right_index <= right:
        curr_sum = curr_sum + array[right_index]
        if curr_sum > right_sum:
            right_sum = curr_sum
        right_index = right_index + 1

    return max(left_sum, right_sum, left_sum + right_sum)


def max_subarray_index(array: List[int], left: int, right: int) -> int:
    max_subarray = array[left]
    i = left
    while i <= right:
        j = i + 1
        while j <= right:
            if sum(array[i:j]) > max_subarray:
                max_subarray = sum(array[i:j])
            j = j + 1
        i = i + 1
    return max_subarray


def max_subbaray_mixed(array: List[int], left: int, right: int) -> int:
    if right - left <= 5:
        # I have to deal w/ an off by 1 here in the recursive case...
        return max_subarray_index(array, left, right + 1)

    if left == right:
        return array[left]

    middle = (left + right) // 2
    left_sum = max_subbaray_mixed(array, left, middle)
    right_sum = max_subbaray_mixed(array, middle + 1, right)
    mid_sum = max_subarray_middle(array, left, middle, right)

    return max(left_sum, right_sum, mid_sum)


def max_subarray_linear(array: List[int]) -> int:
    index = 0
    running_sum = 0
    result = float('-inf')

    while index < len(array):
        running_sum = running_sum + array[index]
        if running_sum > result:
            result = running_sum
        if running_sum < 0:
            running_sum = 0
        index = index + 1
    
    return result


def find_crossover():
    """
    This came out to be about 4 or 5

    # for k, v in find_crossover().items():
    #     if v['brute'] < v['recursion']:
    #         print(f"Brute is faster for {k}")
    """
    executions = 500
    n = 10
    array = []
    timed_executions = {}
    for i in range(n):
        array.append(random.randint(-100, 100))

        total_time_brute = 0
        total_time_recursion = 0
        for _ in range(executions):
            start_brute = time.time()
            max_subarray(array)
            end_brute = time.time()
            total_time_brute = total_time_brute + (end_brute - start_brute)

            start_recursion = time.time()
            max_subarray_recursive(array, 0, len(array) - 1)
            end_recursion = time.time()
            total_time_recursion = total_time_recursion + (end_recursion - start_recursion)

        timed_executions[i + 1] = {
            'brute': (total_time_brute / executions) * 1000,
            'recursion': (total_time_recursion / executions) * 1000,
        }

    return timed_executions


def find_crossover_v2():
    """
    This came out to be about 2 or 3

    for k, v in find_crossover_v2().items():
        if v['brute'] < v['recursion']:
            print(f"Brute is faster for {k}")
    """
    executions = 500
    n = 10
    array = []
    timed_executions = {}
    for i in range(n):
        array.append(random.randint(-100, 100))

        total_time_brute = 0
        total_time_recursion = 0
        for _ in range(executions):
            start_brute = time.time()
            max_subarray(array)
            end_brute = time.time()
            total_time_brute = total_time_brute + (end_brute - start_brute)

            start_recursion = time.time()
            max_subbaray_mixed(array, 0, len(array) - 1)
            end_recursion = time.time()
            total_time_recursion = total_time_recursion + (end_recursion - start_recursion)

        timed_executions[i + 1] = {
            'brute': (total_time_brute / executions) * 1000,
            'recursion': (total_time_recursion / executions) * 1000,
        }

    return timed_executions
