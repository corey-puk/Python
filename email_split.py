def splitEmailAddress(address):
    list = []
    for i in address.split('@'):
        for k in i.split('.'):
            list.append(k)
    return(list)



splitEmailAddress('corey.johnson@hotmail.com')
