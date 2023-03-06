def isPalindrome(s):
    s1 = s.lower()
    s2 = ""
    for char in s1:
        if char.isalnum():
            s2=s2+char
    i = 0
    j = len(s2) -1
    count = int(len(s2)/2)
    for a in range(0,count):
        if(s2[i] != s2[j]):
            return False
        else:
            if(i == j):
                return True
            else:
                i = i+1
                j = j-1
    return True

s=" !"
print(isPalindrome(s))