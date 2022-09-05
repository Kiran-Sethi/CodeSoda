

# def contigiousSum(num):

#     maxSum = num[0]

#     for i in range(len(num)):
#         for j in range(len(num)+1):
#             count = 0
#             for k in range(i, j):
#                 count += num[k]
#             maxSum = max(maxSum, count)

#     return maxSum


# nums = [5, 4, -1, 7, 8]
# print(contigiousSum(nums))

# o(n3)


# ---------------------------------------------------------

def contigiousSum(num):

    maxSum = num[0]
    count = 0

    for i in num:
        if (count < 0):
            count = 0

        count += i
        maxSum = max(count, maxSum)

    return maxSum


nums = [-3, -1, -2]
print(contigiousSum(nums))
