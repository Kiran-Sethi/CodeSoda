# Using pythons inbuilt function

# def valid_palindrome(s):
#     newStr = ""
#     for n in s:
#         if n.isalnum():
#             newStr += n.lower()
#     return newStr == newStr[::-1]


# print(valid_palindrome("a@a"))


# ------------------------------------###########################-------------------------------
# Alternate approach (takes more time but not using inbuilt function. complexity is same)


def isAlphaNumeric(c):  # check if char is alphanumeric
    return (ord("0") <= ord(c) <= ord("9") or ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z"))


def valid_palindrome(s):
    l, r = 0, len(s)-1

    while (l < r):

        # if s[l] is alphanumeric then increase the index
        while l < r and not isAlphaNumeric(s[l]):
            l += 1
        # if s[r] is alphanumeric then decrease the index
        while r > l and not isAlphaNumeric(s[r]):
            r -= 1

        if (s[l].lower() != s[r].lower()):
            return False

        l, r = l+1, r - 1

    return True


print(valid_palindrome("A man, a plan, a canal: Panama"))
