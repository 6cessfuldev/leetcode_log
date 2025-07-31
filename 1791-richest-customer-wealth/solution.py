class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0

        for i in accounts:
            maxSum = max(maxSum, sum(i))

        return maxSum
        
