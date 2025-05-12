# s = "III"
# s = "LVIII"
s = "MCMXCIV"

roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

sum = 0
i = 0

while i<len(s):
    if i+1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
        sum = sum + roman_map[s[i+1]] - roman_map[s[i]]
        i=i+2
    else:
        sum = sum + roman_map[s[i]]
        i=i+1

print(sum)
