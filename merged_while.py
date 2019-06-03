def merge(list1,list2):
    merged = []
    while list1 != [] and list2 != []:
        if list1[0] <= list2[0]:
            merged.append(list1[0])
            list1 = list1[1:]
        else:
            merged.append(list2[0])
            list2 = list2[1:]
    if list1 != []:
        merged = merged + list1
    else:
        merged = merged + list2
    return(merged)

x = [2,4,6,8]
y = [1,3,5,11,12]

merge(x,y)
