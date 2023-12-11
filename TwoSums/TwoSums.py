class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            print('Difference Print:',diff)
            if diff in prevMap:
                print('If return print:',prevMap[diff], i)
                return [prevMap[diff], i]
            prevMap[n] = i
            print('After if statement print:',prevMap)
        return 
    
# Solution.twoSum(0,[2,7,11,15], 9)


def twoy(nums: list[int], target: int) -> list[int]:
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if nums[i] + nums[j] == target:
                print([i,j])
                return [i, j]
            
twoy([5,2,11,15], 17)