    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tCount = {}
        sCount = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            tCount[t[i]] = tCount.get(t[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i],0) + 1
        
        for letter in sCount:
            if tCount.get(letter,0) != sCount[letter]:
                return False
        return True