# Bruteforce approach

# def twoSum(num, target):
#     for i in range(len(num)):
#         for j in range(i, len(num)):
#             if (i == j or i > j):
#                 continue
#             elif ((num[i] + num[j]) == target):
#                 return [i, j]


# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums, target))


# --------------------------------------------#####################------------------------------------------
# optimised code
# Trick is use hashmap to find target - num[n] value in hashmap

def twoSum(num, target):

    valueIndexDict = {}

    for n in range(len(num)):
        numToFind = target - num[n]
        if (numToFind in valueIndexDict):
            return [valueIndexDict[numToFind], n]
        else:
            valueIndexDict[num[n]] = n


nums = [-3, 4, 3, 90]
target = 0
print(twoSum(nums, target))
