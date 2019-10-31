def addmats(a,b):
    # check if matrices are similar length
    check1 = len(mat1[0])
    check2 = len(mat2[0])
    if check1 == check2:
        for i in a:
            k = i
        for g in b:
            h = g
        new_mat = [sum(x) for x in zip(h,k)]
        # where h and k are the inner elements of respective matrices
        print(new_mat)
    else:
        print("Please ensure matrices are of the same size.")
            
