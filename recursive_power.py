
def pow(x,n):
    if n == 0:
        return(1)
    if n == 1:
        return(x)
    if n % 2 == 0:
        x1 = pow(x,n//2)
        return(x1*x1)
    else:
        x1 = pow(x,n//2)
        return(x*x1*x1)

pow(2,8)
