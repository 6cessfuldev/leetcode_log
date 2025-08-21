class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1 = 0
        ptr2 = 0

        while ptr2 < len(nums):
            ptr2 += 1
            if nums[ptr1] == 0:
                nums.append(nums[ptr1])
                del nums[ptr1]
            else:
                ptr1 += 1
        
