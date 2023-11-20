from typing import List, Optional

from hypothesis import given
from hypothesis.strategies import lists
from hypothesis.strategies import integers

import searches

class TestSearches:
    @given(lists(integers(), min_size=1, unique=True), integers())
    def test_search(self, a: List[int], v: int) -> None:
        result = searches.search(a, v)
        if v in a:
            assert a.index(v) == result
        else:
            assert result is None
    
    @given(lists(integers(), min_size=1, unique=True), integers())
    def test_binary_search(self, a: List[int], v: int) -> None:
        a = sorted(a)
        assert searches.search(a, v) == searches.binary_search(a, v, 0, len(a))

    @given(lists(integers(), min_size=1, unique=True), integers())
    def test_binary_search_rec(self, a: List[int], v: int) -> None:
        a = sorted(a)
        assert searches.search(a, v) == searches.binary_search_rec(a, v, 0, len(a))

    @given(lists(integers(min_value=1), min_size=2, unique=True), integers(min_value=1))
    def test_search_sum(self, a: List[int], v: int) -> None:
        result = searches.search_sum(a, v)

        in_list = False
        for i in a:
            copy_of_a = a.copy()
            copy_of_a.remove(i)
            if (v - i) in copy_of_a:
                in_list = True
                break

        assert result == in_list
