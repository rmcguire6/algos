def minSize(target, nums):
    pointer = 0
    lengthOfSubstring = 1
    while lengthOfSubstring < len(nums):     
        while pointer < len(nums):
            substring = nums[pointer:pointer + lengthOfSubstring + 1]
            print('sub', substring)
            currentSum = 0
            for index, value in enumerate(substring):
                currentSum += value
            print('point', pointer, currentSum)
            if currentSum == target:
                print('current sum ', currentSum)
                return len(substring)
            pointer += 1
        lengthOfSubstring += 1
    return 0