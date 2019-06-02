
#The idea of basename is to return only the 'value' of the files name without the .extension
def basename(p):
    return(p.split('/')[-1].split('.')[0])



basename('/user/mike/cits/exam.doc')
    
