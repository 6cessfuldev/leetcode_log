class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1 = 0 
        ptr2 = len(height) - 1
        maxArea = 0

        while ptr1 < ptr2:
            area = (ptr2 - ptr1) * min(height[ptr1], height[ptr2])
            maxArea = max(area, maxArea)
            
            if height[ptr1] < height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
        
        return maxArea

