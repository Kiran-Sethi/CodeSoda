def longestSubstring(s):
    if(s == ""):
        return 0
    elif(s == " "):
        return 1
    else:
        i = 0
        j =1

        longestSubstring = 0
        maxSubStr = ''

        while(i<len(s) and j-1<len(s)):
            # print(f'i, j is {i},{j}')
            tempLi = sorted(list(s[i:j]))
            # print(f'{list(s[i:j])} v/s {sorted(list(set(tempLi)))} is {tempLi == sorted(list(set(tempLi)))} \n')
            if(tempLi == sorted(list(set(tempLi)))):
                maxSubStr = s[i:j]
                longestSubstring = max(len(maxSubStr),longestSubstring)
                j+=1
            else:
                # print(s[i:j])
                # print(f'max Substring: {maxSubStr} ')
                i+=1

        return max(len(maxSubStr),longestSubstring)


# s = "abcabcbb"
# s = "c"
# s = "davdf"
# s = "bbbbb"
s = "pwwkew"
print(longestSubstring(s))
