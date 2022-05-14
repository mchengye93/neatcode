  def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set()
	  
	 for n in nums:
		If n in numSet:
		      return True
		numSet.add(n)
	return false
	
