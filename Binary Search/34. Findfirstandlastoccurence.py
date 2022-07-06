class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        def binarysearch(nums,target,low,high):
            nonlocal first, last
            if low>high:
                return
            mid = int((low+high)/2)
            if(target == nums[mid]):
                if first == -1:
                    first = last = mid
                if first > mid:
                    first = mid
                if last<mid:
                    last = mid
                binarysearch(nums,target,low,mid-1)
                binarysearch(nums,target,mid+1,high)
            elif (target>nums[mid]):
                binarysearch(nums,target,mid+1,high)
            else:
                binarysearch(nums,target,low,mid-1)
            return [first,last]
        return binarysearch(nums,target,0,len(nums)-1)
        
