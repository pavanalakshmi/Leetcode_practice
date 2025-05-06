# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(nums1)
for i in nums2:
    nums1[m] = i
    m=m+1

nums1.sort()
print(nums1)