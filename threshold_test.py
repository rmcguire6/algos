from threshold import numOfSubarrays
def test_case_zero():
    assert numOfSubarrays(arr= [1], k=1, threshold = 0) == 1
def test_case_one():
    assert numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k=3, threshold = 4) == 3
def test_case_two():
    assert numOfSubarrays([11,13,17,23,29,31,7,5,2,3], k=3, threshold = 5) == 6