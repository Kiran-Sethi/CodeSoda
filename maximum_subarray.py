# Bruteforce approach


# def maximum_subarray_bruteforce(nums):
#     max = 0
#     for i in range(len(nums)+1):
#         for j in range(i, len(nums)+1):
#             count = 0
#             print(i, j)
#             for k in range(i, j):
#                 count += nums[k]
#                # print(nums[k], end=" ")

#             #print("----")
#             #print(f'count is {count}')
#             if (count > max):
#                 max = count
#             #print(f'Max is {max}')
#     return max


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(f'max is {maximum_subarray_bruteforce(nums)}')


# ------------------------------------------------------------#####################------------------------------------------
# optimised code

import re


def maximum_subarray_optimsed(nums):
    maxSum = nums[0]
    count = 0

    for n in nums:
        if (count < 0):
            count = 0

        count += n
        print(f"count is {count} and maxsum is {maxSum}")
        maxSum = max(count, maxSum)

    return maxSum


nums = [-3, -2, -1]
print(f'max is {maximum_subarray_optimsed(nums)}')
