from longest_sub import longestSubstring


def test_case_zero():
    assert longestSubstring("abcabcbb") == 3


def test_case_one():
    assert longestSubstring("bbbbb") == 1


def test_case_two():
    assert longestSubstring("pwwkew") == 3
