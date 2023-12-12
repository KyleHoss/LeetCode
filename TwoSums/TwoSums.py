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