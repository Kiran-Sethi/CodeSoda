def min_remove_valid_parenthesis(str):

    res = []
    stack = []
    count = -1
    index = 0

    for c in range(len(str)):
        if (str[c] == ")" and count == -1):
            index += 1
            continue

        if (str[c] == "("):
            stack.append(c-index)
            res.append(str[c])
            count += 1
        elif (str[c] == ")" and count >= 0):
            # print(f'stack before remove {stack}')
            stack = stack[:-1]
            # print(f'stack after remove {stack}')
            count -= 1
            res.append(str[c])
        else:
            res.append(str[c])

    # print("".join(res))
    # print(stack)
    if (len(stack) > 0):
        for i in stack:
            res[i] = "#"
        res = "".join(res)
        res = res.replace("#", '')
    return res


print(min_remove_valid_parenthesis("))(("))
