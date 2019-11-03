
# The resultant fibonacci number at 'index' x of the fibonacci sequence 
# Note that this computes in O(2**n) time and so it will take longer to compute as x becomes large (around x=30 it takes approximately 5 seconds to compute on a standard computer)

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

import time
start_time = time.time()
fib(35)
print("--- %s seconds ---" % (time.time() - start_time))
