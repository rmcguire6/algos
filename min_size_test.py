from minsize import minSize
def test_case_zero():
    assert minSize(target = 7, nums =[2,3,1,2,4,3]) == 2
def test_case_one():
    assert minSize(target = 4, nums = [1,4,4]) == 1
def test_case_two():
    assert minSize(target = 11, nums = [1,1,1,1,1,1,1,1]) == 0