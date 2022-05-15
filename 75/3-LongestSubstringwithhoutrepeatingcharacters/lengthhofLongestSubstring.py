    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        maxLength = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
                
            charSet.add(s[r])
            maxLength = max(maxLength, r-l+1)
        return maxLength