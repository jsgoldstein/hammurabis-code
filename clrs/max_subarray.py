from typing import List

from hypothesis import given
from hypothesis.strategies import lists
from hypothesis.strategies import integers


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


class TestMaxSubarray:
    @given(lists(integers(), min_size=2, unique=True))
    def test_max_subarray(self, a: List[int]) -> None:
        res = max_subarray(a)
        for i in a:
            assert res >= i
        assert res >= sum(a)

    @given(lists(integers(), min_size=2, unique=True))
    def test_max_subarray_recursive(self, a: List[int]) -> None:
        assert max_subarray_recursive(a, 0, len(a) - 1) == max_subarray(a)


