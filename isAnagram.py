

def isAnagram(s, t):

    if (len(s) != len(t)):
        return False

    dict = {}

    for c in s:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

    for n in t:
        if n not in dict:
            return False
        if (dict[n] != t.count(n)):
            return False

    return True


s = "rat"
t = "car"

print(isAnagram(s, t))
