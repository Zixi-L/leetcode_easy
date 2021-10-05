class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        def formatstr(lower, upper):
            if lower == upper:
                return str(lower)
            return str(lower) + '->' + str(upper)
        
        output = []
        nums.insert(0,lower-1) # 连着的数之间没有 interval，所以这样加一个 lower-1 不影响
        nums.insert(len(nums),upper+1)
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] != 1:
                output.append(formatstr(nums[i-1]+1, nums[i]-1))
            

        return output
