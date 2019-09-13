def removeElement(self, nums: List[int], val: int) -> int:
    slow=0
    for i in nums:
        if i != val:
            nums[slow]=i
            slow +=1
    return slow