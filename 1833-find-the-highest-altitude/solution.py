class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre_sum = [gain[0]]

        for i in range(1, len(gain)):
            pre_sum.append(pre_sum[i-1] + gain[i])

        return max(0, max(pre_sum))
