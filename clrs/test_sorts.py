import copy
import math
from typing import Callable, List

from hypothesis import given
from hypothesis.strategies import lists as a_list
from hypothesis.strategies import integers as of_ints


# Run with: pytest --hypothesis-show-statistics


def insertion_sort_left(items: List[int]) -> None:
    i = 1
    while i < len(items):
        j = 0
        while j < i:
            if items[j] > items[i]:
                temp = items[j]
                items[j] = items[i]
                items[i] = temp
            j = j + 1
        i = i + 1


def insertion_sort_right(items: List[int]) -> None:
    i = 1
    while i < len(items):
        j = i - 1
        while j >= 0:
            if items[j] > items[j + 1]:
                temp = items[j + 1]
                items[j + 1] = items[j]
                items[j] = temp
            else:
                break
            j = j - 1
        i =  i + 1


def merge_sort(items: List[int], l: int, r: int, merge_func: Callable) -> None:
    if len(items[l:r]) > 1:
        mid = math.floor((l + r) / 2)

        merge_sort(items, l, mid, merge_func)
        merge_sort(items, mid, r, merge_func)

        merge_func(items, l, mid, r)


def merge(items: List[int], l: int, m: int, r: int) -> None:
    left = items[l:m]
    left.append(math.inf)

    right = items[m:r]
    right.append(math.inf)

    i = 0
    j = 0
    resulting = []
    while i < (m - l) or j < (r - m):
        if left[i] < right[j]:
            resulting.append(left[i])
            i = i + 1
        else:
            resulting.append(right[j])
            j = j + 1

    while l < r:
        items[l] = resulting.pop(0)
        l = l + 1


def merge_less_mem(items: List[int], l: int, m: int, r: int) -> None:
    left = items[l:m]
    left.append(math.inf)

    right = items[m:r]
    right.append(math.inf)

    i = 0
    j = 0
    while l < r:
        if left[i] < right[j]:
            items[l] = left[i]
            i = i + 1
        else:
            items[l] = right[j]
            j = j + 1
        l = l + 1


def merge_no_inf(items: List[int], l: int, m: int, r: int) -> None:
    left = items[l:m]
    right = items[m:r]

    i = 0
    j = 0
    while l < r:
        if i == len(left):
            items[l] = right[j]
            j = j + 1
        elif j == len(right):
            items[l] = left[i]
            i = i + 1
        elif left[i] < right[j]:
            items[l] = left[i]
            i = i + 1
        else:
            items[l] = right[j]
            j = j + 1
        l = l + 1


@given(a_list(of_ints()))
def test_insertion_sort_left(a: List[int]) -> None:
    b = copy.deepcopy(a)
    insertion_sort_left(b)

    print(a)
    print(b)

    assert sorted(a) == b


@given(a_list(of_ints()))
def test_insertion_sort_right(a: List[int]) -> None:
    b = copy.deepcopy(a)
    insertion_sort_right(b)

    assert sorted(a) == b


@given(a_list(of_ints()))
def test_merge_sort_merge(a: List[int]) -> None:
    b = copy.deepcopy(a)
    merge_sort(b, 0, len(b), merge)

    assert sorted(a) == b


@given(a_list(of_ints()))
def test_merge_sort_merge_less_mem(a: List[int]) -> None:
    b = copy.deepcopy(a)
    merge_sort(b, 0, len(b), merge_less_mem)

    assert sorted(a) == b


@given(a_list(of_ints()))
def test_merge_sort_merge_no_inf(a: List[int]) -> None:
    b = copy.deepcopy(a)
    merge_sort(b, 0, len(b), merge_no_inf)

    assert sorted(a) == b
