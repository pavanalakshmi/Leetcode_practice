
# nums = [3,2,2,3]
# val = 3
nums = [0,1,2,2,3,0,4,2]
val = 2
output = len(nums)

expectedNums = []

for i in range(0, len(nums)):
    if nums[i]!=val:
        expectedNums.insert(i, nums[i])

print(expectedNums)

# for i in range(0, len(nums)):
#     if nums[i]==val:
#         nums[i] = 0
#         output-=1

# nums.sort(reverse=True)
# print(nums)
# print(output)
