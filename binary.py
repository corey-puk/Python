#Example of binary search algorithm

def search(x,nums):
#Initialise the low & high variables
    low = 0
    high = len(nums) - 1
#Use while loop to loop through values of list
    while low <= high:
#We want the algorithm to 'halve' the list each loop
        mid = (low + high)//2
        item = nums[mid]
#We effectively 'push' the middle number between 'high' and
#'low' to establish its index value
        if x == item:
            return mid
        if x < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1
#Algorithm will return index value or -1 if value not in list


nums = range(1,100)


search(62,nums)
