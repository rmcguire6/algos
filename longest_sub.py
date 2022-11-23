def longestSubstring(s):
    if s == None:
        return 0
    uniqueCharacters = []
    i = 0
    j = 0
    max_substring_length = 0
    while i < len(s):
        character = s[i]
        while character in uniqueCharacters:
            uniqueCharacters.pop(0)
            j += 1
        uniqueCharacters.append(character)
        if len(uniqueCharacters) > max_substring_length:
            max_substring_length = len(uniqueCharacters)
        i += 1
    return max_substring_length
