def removeDuplicates(self,nums):
    if len(nums)==1 or 0:
        return 1 or 0
    else:
        # The slow point which points to the last no-duplicate number
        count=0
        # The fast point which points to each number in the list
        for i in range(1,len(nums)):
            # when i=1, nums[count] = nums[0], which is not modified
            
            if nums[count]!=nums[i]:
            # The duplicate run has ended, so ww copy its value to nums[count+1]
                count+=1
                nums[count]=nums[i]
        # return the length of non-duplicates array. 
        return count+1
