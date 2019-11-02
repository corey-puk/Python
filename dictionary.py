# This is just a little play with dictionary values with a function that takes in an argument of a dictionary. 
# No attempt has been made to raise any exceptions given an incorrect input to the function

dict = {"Fred":55, "James":67, "Jemima":71}

def marksdistribution(D):
    marks = {"N":0, "P":0, "Cr":0, "D":0,"HD":0}
    for k in D.values():
        if k < 50:
            marks['N'] += 1
        elif k >= 50 and k < 60:
            marks['P'] += 1
        elif k >= 60 and k < 70:
            marks['Cr'] += 1
        elif k >= 70 and k < 80:
            marks['D'] += 1
        elif k >= 80:
            marks['HD'] += 1
    print(marks)
    
marksdistribution(dict)
    
    
