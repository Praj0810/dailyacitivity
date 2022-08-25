def isMatch(s, p):
    SP = [[False for _ in range(len(p) + 1)] for _ in range(len(s)+1)]
    SP[0][0] = True
    
    for i in range(len(s) +1):
        for j in range(1, len(p) +1):
            pattern = p[j-1]
            
            if pattern == ".":
                SP[i][j] = (i != 0 and SP[i-1][j-1])
            elif pattern == "*":
                star = p[j-2]
                SP[i][j] = SP[i][j-2] or (i > 0 and SP[i-1][j] and (star == s[i-1] or star == "."))
                
            else:
                SP[i][j] = (i != 0 and SP[i-1][j-1] and s[i-1] == pattern)
    return SP[-1][-1]

    
s = input("Enter S")
p = input("enter P")
# test case one
#s = "aa"
#p = "a"

# #test case two
# s = "aa"
# p = "a*"

#  #test case three
# s = "ab"
# p = ".*"

# # test case four
# s = "mississippi"
# p = "mis*is*p*.

# # # #test case five
# s ="aab"
# p = "c*a*b"

print(isMatch(s,p))
