from typing import List

from hypothesis import given
from hypothesis.strategies import lists
from hypothesis.strategies import integers

import max_subarray

class TestMaxSubarray:
    @given(lists(integers(), min_size=2, unique=True))
    def test_max_subarray(self, a: List[int]) -> None:
        res = max_subarray.max_subarray(a)
        for i in a:
            assert res >= i
        assert res >= sum(a)

    @given(lists(integers(), min_size=2, unique=True))
    def test_max_subarray_recursive(self, a: List[int]) -> None:
        assert max_subarray.max_subarray_recursive(a, 0, len(a) - 1) == max_subarray.max_subarray(a)

    @given(lists(integers(), min_size=2, unique=True))
    def test_max_subarray_index(self, a: List[int]) -> None:
        assert max_subarray.max_subarray_index(a, 0, len(a)) == max_subarray.max_subarray(a)

    @given(lists(integers(), min_size=2, unique=True))
    def test_max_subbaray_mixed(self, a: List[int]) -> None:
        assert max_subarray.max_subbaray_mixed(a, 0, len(a) - 1) == max_subarray.max_subarray(a)

    @given(lists(integers(), min_size=2, unique=True))
    def test_max_subarray_linear(self, a: List[int]) -> None:
        assert max_subarray.max_subarray_linear(a) == max_subarray.max_subarray(a)
