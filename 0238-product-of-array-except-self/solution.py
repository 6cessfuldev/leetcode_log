class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixs = []
        suffixs = []
        output = []

        for i in range(len(nums)):
            if i == 0:
                prefixs.append(nums[i])
            else:
                prefixs.append(prefixs[i-1] * nums[i])

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffixs.insert(0, nums[i])
            else:
                suffixs.insert(0, suffixs[0] * nums[i])

        for i in range(len(nums)):
            if i == 0:
                output.append(suffixs[i+1])
                continue
            if i == len(nums)-1:
                output.append(prefixs[i-1])
                continue

            output.append(prefixs[i-1] * suffixs[i+1])

        return output
