    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictNum = {}
        
        for i in range(len(nums)):
            complement = target-nums[i]
            
            if complement in dictNum:
                return (dictNum[complement], i)
            
            dictNum[nums[i]] = i