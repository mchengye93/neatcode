 #recursion
  def fib(n):
    if n in [1, 0]:
        return n
    return fib(n - 1) + fib(n - 2)

# Using memoization
  class Fibber(object):

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            # Edge case: negative index
            raise ValueError('Index was negative. No such thing as a '
                             'negative index in a series.')
        elif n in [0, 1]:
            # Base case: 0 or 1
            return n

        # See if we've already calculated this
        if n in self.memo:
            return self.memo[n]

        result = self.fib(n - 1) + self.fib(n - 2)

        # Memoize
        self.memo[n] = result

        return result

 # Using bottom up approach
   def fib(n):
    # Edge cases:
    if n < 0:
        raise ValueError('Index was negative. No such thing as a '
                         'negative index in a series.')
    elif n in [0, 1]:
        return n

    # We'll be building the fibonacci series from the bottom up
    # so we'll need to track the previous 2 numbers at each step
    prev_prev = 0  # 0th fibonacci
    prev = 1       # 1st fibonacci

    for _ in xrange(n - 1):
        # Iteration 1: current = 2nd fibonacci
        # Iteration 2: current = 3rd fibonacci
        # Iteration 3: current = 4th fibonacci
        # To get nth fibonacci ... do n-1 iterations.
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current
