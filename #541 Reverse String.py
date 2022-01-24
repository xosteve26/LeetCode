def reverseStr(s, k):
    st = ''
    if len(s) < k:
        return s[::-1]
    elif(len(s) <= 2*k):
        return print(s[:k][::-1]+s[k:])
    else:
        i = 0
        while(i <= len(s)):
            print(s[i:k])
            st += s[i:i+k][::-1]+s[i+k:i+k+k]
            print(st)
            i += 2*k
            print("I VALUE", i)
    return print(st)


reverseStr("abcd", 2)

# "bacdfeg"
