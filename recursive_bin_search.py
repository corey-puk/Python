z = range(1,100)


def find(x,list,low,high):
    if low > high: # no place left to 'search'
        return - 1
    mid = (low + high) // 2
    item = list[mid] # define middle of list
    if item == x:
        return mid # if item is x, must be middle value
    if x < item:
        return find(x,list,low,mid-1) # return and try again with list // 2
    return find(x,list,mid+1,high) # return and try again with list // 2

# Wrap the binary function and utilise recursion algorithm

def search(x,list): # search for x in list
    return find(x,list,0,len(list)-1) # set params for 'find'


search(20,z)
