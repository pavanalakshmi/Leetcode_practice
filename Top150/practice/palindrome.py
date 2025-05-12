s = "madam"
s1 = ""

for i in range(len(s)-1, -1, -1):
    # print(s[i])
    s1 += s[i]

# for i in reversed(s):
#     s1 += i

if s.lower() == s1.lower():
    print(s, " is a Palindrome")
else:
    print(s, " is not a Palindrome")
