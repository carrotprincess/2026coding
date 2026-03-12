# week02-2.py 學習筆記 Two Pointers 第1題
# LeetCode 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)  # 陣列的大小
        k = 0  # 設宣告 k 一開始在最左邊待命

        for i in range(N):  # 把 nums[i] 的數字一一檢查
            if nums[i] != 0:  # 碰到不是 0 的數，要搬到左邊
                nums[k] = nums[i]  # 左邊 nums[k] 右邊 nums[i]
                k += 1  # k 指下一個位置

        for i in range(k, N):  # 剩下的格子
            nums[i] = 0  # 全部補 0