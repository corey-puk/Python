def marksdist(d):
    grades_count = {}
    for grade in ['N','P','Cr','D','HD']:
        grades_count[grade] = 0
    for mark in d.values():
        if mark < 50:
            grades_count['N'] += 1
        elif mark >= 50 and mark < 60:
            grades_count['P'] += 1
        elif mark >= 60 and mark < 70:
            grades_count['Cr'] += 1
        elif mark >= 70 and mark < 80:
            grades_count['D'] += 1
        else:
            mark >= 80
            grades_count['HD'] += 1
    return(grades_count)


dict = {"Fred":55, "James":67, "Harry":90}

marksdist(dict)
