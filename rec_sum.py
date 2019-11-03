# function will take compute the sum of integers 1 through x using recursion

def rec(x):
    if x == 1:
        return 1
    else:
        return x + rec(x-1)
            
        
rec(5)
