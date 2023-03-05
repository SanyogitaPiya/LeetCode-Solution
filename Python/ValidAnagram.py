def isAnagram(s,t):
    if len(s) != len(t):
        return False
    if len(s) == 1 and s != t:
        return False
    char_arr_s = list(s)
    char_arr_s.sort()
    char_arr_t = list(t)
    char_arr_t.sort()
    if char_arr_t == char_arr_s:
        return True
    return False

s = ""
t = "a"
print(isAnagram(s,t))
