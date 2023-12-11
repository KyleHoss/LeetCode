class Solution:
    def twoSum(self, nums, target):

        output = [[0]*2]*len(nums)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                output[i][0] = [i,j]
                output[i][i] = nums[i] + nums[j]
            print(output,'=',nums[i],"+",nums[j])
        print(target)

Solution.twoSum(0,[2,7,11,15], 9)