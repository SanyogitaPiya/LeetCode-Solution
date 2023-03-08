def strStr(haystack, needle):
        if haystack == needle:
            return 0
        win_size = len(needle)
        start = 0
        end = win_size
        while (end != len(haystack)+1):
            sub_str = haystack[start:end]
            if sub_str == needle :
                return start
            else:
                start = start + 1
                end = end +1
        return -1

haystack = "hello"
needle = "ll"
print(strStr(haystack,needle))