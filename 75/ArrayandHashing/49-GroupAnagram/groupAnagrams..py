    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        
        for word in strs:
            count = [0]*26
            
            for letter in word:
                count[ord(letter)-ord('a')] += 1
            ans[tuple(count)].append(word)
        return ans.values()