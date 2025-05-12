nums = [2,2,1,1,1,2,2]

# nums.sort()

count = 0
output = None

for i in nums:
    if count == 0:
        output = i
    if i == output:
        count = count+1
    else:
        count = count-1

print (output)
