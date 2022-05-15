    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = [[] for i in range(len(nums)+1)]
        
        dictCount = {}
        ans = []
        
        for n in nums:
            dictCount[n] = dictCount.get(n,0) + 1
        
        for num, count in dictCount.items():
            counts[count].append(num)
        
        for i in range(len(counts)-1, 0, -1):
            for number in counts[i]:
                ans.append(number)
                if len(ans) == k:
                    return ans