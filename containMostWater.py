# bruteforce approach

# def containMostWater(arr):

#     maxArea = 0

#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             height = min(arr[i],  arr[j])
#             length = (j-i)

#             area = height*length
#             maxArea = max(area, maxArea)

#     return maxArea


# containMostWater([1, 1])

# ---------------------------------------###############-------------------------------------------
# optimized o(n) solution

def containMaxWater(arr):
    l = 0
    r = len(arr) - 1

    maxArea = 0

    while (l < r):
        height = min(arr[l],  arr[r])
        length = (r-l)
        maxArea = max(maxArea, height*length)

        if (arr[l] <= arr[r]):
            l += 1
        else:
            r -= 1

    return maxArea


print(containMaxWater([1, 1]))
