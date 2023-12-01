import pytest
from Bubble import bubble

def test_sort():
    assert bubble([9,8,7]) == [7, 8, 9]
    assert bubble([8,7,6]) == [6, 7, 8]
    assert bubble([3,2,1]) == [1, 2, 3]
    