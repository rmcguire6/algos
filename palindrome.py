import re


def isPalindrome(s):

    str = s.lower()
    match = re.findall(r'[a-z]', str)
    firstPointer = 0
    lastPointer = len(match) - 1
    while firstPointer < lastPointer:
        if (match[firstPointer] != match[lastPointer]):
            return False
        firstPointer += 1
        lastPointer -= 1
    return True
