from palindrome import isPalindrome


def test_case_1():
    assert isPalindrome("A man, a plan, a canal: Panama") == True


def test_case_2():
    assert isPalindrome("race a car") == False


def test_case_s_empty():
    assert isPalindrome("") == True


def test_case_capital_letters():
    assert isPalindrome("BUG gub") == True
