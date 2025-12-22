class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = nums.count(0)
        count1 = nums.count(1)
        count2 = nums.count(2)

        for i in range(count0):
            nums[i] = 0
        for i in range(count0, count1 + count0):
            nums[i] = 1
        for i in range(count0 + count1, count0 + count1 + count2):
            nums[i]  = 2
           



      
