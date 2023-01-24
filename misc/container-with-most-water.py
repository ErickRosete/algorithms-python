class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -float('inf')
        left = 0
        right = len(height) - 1
        while( right > left):
            area =  min(height[right], height[left]) * (right - left)
            max_area = max(area, max_area)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_area  