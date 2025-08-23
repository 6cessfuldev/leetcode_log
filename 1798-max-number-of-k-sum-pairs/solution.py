class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = list(filter(lambda x: x < k, nums))
        nums.sort()

        if len(nums) < 1:
            return 0

        ptr1 = 0
        ptr2 = len(nums) - 1
        cnt = 0

        print(nums)

        while ptr1 < ptr2:

            if nums[ptr1] == k - nums[ptr2]:
                cnt += 1
                ptr1 += 1
                ptr2 -= 1
            elif nums[ptr1] < k - nums[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1

        return cnt



