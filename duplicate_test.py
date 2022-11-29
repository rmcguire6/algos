from duplicate import containsNearbyDuplicate
def test_case_zero():
    assert containsNearbyDuplicate(arr= [1,2,3,1], k=3) == True
def test_case_one():
    assert containsNearbyDuplicate(arr = [1,0,1,1], k=1) == True
def test_case_two():
    assert containsNearbyDuplicate([1,2,3,1,2,3], k=2) == False