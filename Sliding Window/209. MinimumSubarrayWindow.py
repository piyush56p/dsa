class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        res= float("inf")
        for r in range(len(nums)):
            curr_sum += nums[r]
            while(curr_sum >= target):
                res = min(r-l+1,res)
                curr_sum -= nums[l]
                l+=1
        return 0 if res == float("inf") else res
