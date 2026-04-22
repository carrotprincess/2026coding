# week08-5.py 學習計畫 Binary Search 第3題
# LeetCode 162. Find Peak Element 找到「比左右鄰居大」的那項

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 思考法：for 迴圈不行嗎？ (因為全部發現，這題只要1000個數)
        
        N = len(nums) # 陣列大小 N
        
        if N == 1:
            return 0 # N=0 最大 (只有1個數，就是最大，不用再 nums[i-1] nums[i+1] 了啦)
            
        for i in range(N):
            if i == 0: # 在最左邊，只有右邊 (要比右邊大)
                if nums[i] > nums[i+1]:
                    return i
            
            elif i == N-1: # 在最右邊，沒有右邊，只有左邊 (要比左邊大)
                if nums[i] > nums[i-1]:
                    return i
            
            # 下面可能會當機，因 i-1 或 i+1 會超出範圍，所以加上面的 if
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i