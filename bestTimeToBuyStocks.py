# def maximizeProfit(price):
#     maxProfit = 0
#     for i in range(len(price)):
#         for j in range(i+1, len(price)):
#             maxProfit = max(maxProfit, price[j]-price[i])

#     return maxProfit


# # price = [7, 1, 5, 3, 6, 4]
# price = [7, 6, 4, 3, 1]
# print(maximizeProfit(price))


# ---------------------------------------------################---------------------------------------
def maximizeProfit(price):
    l = 0
    maxSum = 0
    for r in range(1, len(price)):
        if (price[l] > price[r]):
            l = r
            continue
        maxSum = max(maxSum, price[r]-price[l])

    return maxSum


# price = [7, 1, 5, 3, 6, 4]
price = [7, 6, 4, 3, 1]
# price = [2, 1, 4]
print(maximizeProfit(price))
