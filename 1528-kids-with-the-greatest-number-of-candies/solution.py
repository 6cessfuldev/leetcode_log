class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)

        return list(map(lambda x: max_val <= x + extraCandies, candies))

        
             
