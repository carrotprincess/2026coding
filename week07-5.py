# week07-5.py 學習計畫 Queue 第1題，有點難
# LeetCode 394. Decode String
from collections import deque

class RecentCounter:

    def __init__(self):
        # 初始化一個空的佇列來存儲請求的時間
        self.queue = deque()

    def ping(self, t: int) -> int:
        # 1. 將當前請求時間 t 加入佇列
        self.queue.append(t)
        
        # 2. 移除所有不在 [t - 3000, t] 範圍內的過期請求
        # 因為 t 是遞增的，所以過期的請求一定會在佇列的最前面
        while self.queue[0] < t - 3000:
            self.queue.popleft()
            
        # 3. 回傳佇列中的元素個數，即為最近的請求數量
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)