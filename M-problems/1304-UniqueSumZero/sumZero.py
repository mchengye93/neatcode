    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        if n%2:
            arr.append(0)
        
        for i in range(1,n//2+1):
            arr.append(-i)
            arr.append(i)
        return arr