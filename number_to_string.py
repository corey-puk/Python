def num2str():
    while True:
        try:
            n = int(input("This program converts integer values into their respective worded format. Please enter an integer between 0 and 100: "))
            n = int(n)
            if n > 100 or n < 0:
                raise ValueError("Please enter an integer between 0 and 100.")
            break
        except (ValueError, TypeError, EOFError):
            print("This program works only with integers 0 to 100.")
    string_n = str(n)
    dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',
            12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    dict2 = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    dict_words = {'20':"twenty", '30':"thirty",'40':"fourty",'50':"fifty",'60':"sixty",'70':"seventy",'80':"eighty",'90':"ninety",'100':"one hundred"}
    # ensure this small snippet of code is not run if > 20
    if n < 20:
        for key in dict:
            if n == key:
                print(dict[key])
    if n >= 20:
        # check starting digit -- need to ensure it is checked as a string
        if string_n == '20':
            print(dict_words['20'])
        elif string_n[0] == '2' and string_n[1] != '0':
            for key in dict2:
                if string_n[1] == key:
                    print('twenty ' + dict2[key])
        # thirty
        if string_n == '30':
            print(dict_words['30'])
        elif string_n[0] == '3' and string_n[1] != '0':
            for key in dict2:
                if string_n[1] == key:
                    print('thirty ' + dict2[key])
        # fourty
        if string_n == '40':
            print(dict_words['40'])
        elif string_n[0] == '4' and string_n[1] != '0':
            for key in dict2:
                if string_n[1] == key:
                    print('fourty ' + dict2[key])
        # fifty
        if string_n == '50':
            print(dict_words['50'])
        elif string_n[0] == '5' and string_n[1] != '0':
            for key in dict2:
                if string_n[1] == key:
                    print('fifty ' + dict2[key])
        # sixty
        if string_n == '60':
            print(dict_words['60'])
        elif string_n[0] == '6' and string_n[1] != '0':
            for key in dict2:
                if string_n[1] == key:
                    print('sixty ' + dict2[key])
        # seventy
        if string_n == '70':
            print(dict_words['70'])
        elif string_n[0] == '7' and string_n[1] != '0':
            for key in dict2:
                if string_n[1] == key:
                    print('seventy ' + dict2[key])
        # eighty
        if string_n == '80':
            print(dict_words['80'])
        elif string_n[0] == '8' and string_n[1] != '0':
            for key in dict2:
                if string_n[1] == key:
                    print('eighty ' + dict2[key])
        # ninety
        if string_n == '90':
            print(dict_words['90'])
        elif string_n[0] == '9' and string_n[1] != '0':
            for key in dict2:
                if string_n[1] == key:
                    print('ninety ' + dict2[key])
        #100
        if string_n == '100':
            print(dict_words['100'])       
