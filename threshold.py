def numOfSubarrays(arr, k, threshold):
    i = 0
    howManyArrays = 0
    while (i < len(arr)-k + 1):
        sum = 0
        for index in range(i, i+k):
            sum += arr[index]
        average = sum / k
        if (average >= threshold):
            howManyArrays += 1
        i += 1
    return howManyArrays