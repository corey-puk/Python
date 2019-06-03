
# This code computes the 'manhattan distance' - the distance need to travel in a grid in 2 dimensional space. Inputs are given by lists /
# vectors of size n

def manhat(x,y):
    dist = 0
    for i in range(len(x)):
        dist += abs(y[i]-x[i])
    return(dist)




list1 = [1,3,5,7]
list2 = [1,9,25,42]

manhat(list1,list2)
