def search(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        for i in range(len(nums)):
            if target > nums[-1]:
                return len(nums)
            elif target > nums[i] and target < nums[i+1]:
                return i+1
            
#Time Complexity: O(n)
# To improve the Time Complexity to O(lgN):

def searchInsert(self, nums: List[int], target: int) -> int:
    l = 0 
    #right side: the index of the last element
    r = len(nums)-1
    while l<= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l=mid+1
        else:
            r=mid-1
    return l


