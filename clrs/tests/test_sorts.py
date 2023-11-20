import copy
from typing import List

from hypothesis import given
from hypothesis.strategies import lists as a_list
from hypothesis.strategies import integers as of_ints

import sorts

class TestSorts:
    @given(a_list(of_ints()))
    def test_insertion_sort_left(self, a: List[int]) -> None:
        b = copy.deepcopy(a)
        sorts.insertion_sort_left(b)

        assert sorted(a) == b

    @given(a_list(of_ints()))
    def test_insertion_sort_right(self, a: List[int]) -> None:
        b = copy.deepcopy(a)
        sorts.insertion_sort_right(b)

        assert sorted(a) == b

    @given(a_list(of_ints()))
    def test_merge_sort_merge(self, a: List[int]) -> None:
        b = copy.deepcopy(a)
        sorts.merge_sort(b, 0, len(b), sorts.merge)

        assert sorted(a) == b

    @given(a_list(of_ints()))
    def test_merge_sort_merge_less_mem(self, a: List[int]) -> None:
        b = copy.deepcopy(a)
        sorts.merge_sort(b, 0, len(b), sorts.merge_less_mem)

        assert sorted(a) == b

    @given(a_list(of_ints()))
    def test_merge_sort_merge_no_inf(self, a: List[int]) -> None:
        b = copy.deepcopy(a)
        sorts.merge_sort(b, 0, len(b), sorts.merge_no_inf)

        assert sorted(a) == b

    @given(a_list(of_ints(), min_size=3, unique=True))
    def test_merge_sort_count_inversions(self, a: List[int]) -> None:
        count = 0
        i = 0
        while i < len(a):
            j = i + 1
            while j < len(a):
                if a[i] > a[j]:
                    count = count + 1
                j = j + 1
            i = i + 1

        b = copy.deepcopy(a)
        assert count == sorts.merge_sort_count_inversions(b, 0, len(b))
