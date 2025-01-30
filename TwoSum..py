

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
        



# HashTabel Approch 

def twoSum(nums:list[int], target:int)->list[int]:
    pmap = {}

    for index, value in enumerate(nums):
        diff = target - value
        if diff in pmap:
            return pmap[diff], index

        pmap[value] = index


print(twoSum([1,2,3], 5))
