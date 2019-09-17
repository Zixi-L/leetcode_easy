def search(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        for i in range(len(nums)):
            if target > nums[-1]:
                return len(nums)
            elif target > nums[i] and target < nums[i+1]:
                return i+1


print(search([1,3,5,6], 0))
