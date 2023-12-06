import math
from typing import List, Optional


def search(items: List[int], value: int) -> Optional[int]:
    index = 0
    while index < len(items):
        if items[index] == value:
            return index
        index = index + 1
    return None


def binary_search(items: List[int], value: int, l: int, r: int) -> Optional[int]:
    while l <= r:
        mid = math.floor((l + r) / 2)
        if mid >= len(items):
            return None

        if value < items[mid]:
            r = mid - 1
        elif value > items[mid]:
            l = mid + 1
        elif value == items[mid]:
            return mid


def binary_search_rec(items: List[int], value: int, l: int, r: int) -> Optional[int]:
    if l > r:
        return None

    mid = math.floor((l + r) / 2)
    if mid >= len(items):
        return None

    if value < items[mid]:
        return binary_search_rec(items, value, l, mid - 1)
    elif value > items[mid]:
        return binary_search_rec(items, value, mid + 1, r)
    elif value == items[mid]:
        return mid


def search_sum(items: List[int], value: int) -> bool:
    for i in items:
        v = value - i
        copy_of_items = sorted(items.copy())
        copy_of_items.remove(i)
        if binary_search(copy_of_items, v, 0, len(copy_of_items)) is not None:
            return True
    return False


def bin_search_again(array: List[int], value: int) -> int:
    if len(array) < 1:
        return -1
    left = 0
    right = len(array)
    return bin_search_func(array, value, left, right)


def bin_search_func(array: List[int], value: int, left: int, right: int) -> int:
    while left <= right:
        if left == len(array):
            return -1

        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1
        elif array[mid] > value:
            right = mid - 1
    return -1
