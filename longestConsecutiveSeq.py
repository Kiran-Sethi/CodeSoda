def longestConsecutiveSeq():
    count = 1
    sortedNums = list(sorted(set(nums)))
    i = 0
    maxCount = 0
    while (i < len(sortedNums)-1):
        count = 1
        while ((i < len(sortedNums)-1) and (sortedNums[i+1] - sortedNums[i] == 1)):
            count += 1
            i += 1
        i += 1
        maxCount = max(maxCount, count)

    if (len(sortedNums) == 1):
        return 1
    return maxCount


nums = [0, 0]
