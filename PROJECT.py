''' This project takes a look at stylometry - defined as; the statistical analysis of variations in literary style between one writer or genre and another.
The algorithm utilises a distance function to computer the 'distance' between two texts, while it also counts the usage of certain text and/or grammar.'''

import os
import math as mt

def main(textfile, textfile2, feature):

    # if -elif block to ensure data input accuracy
    if feature == 'conjunctions' or feature == 'unigrams' or feature == 'punctuation' or feature == 'composite':
        pass
    else:
        raise ValueError("Please enter the correct options; conjunctions, unigrams, punctuation or composite.")
    # try block for importing of modules


    if os.path.exists(textfile) and os.path.exists(textfile2):
        try:
            with open(textfile, 'r') as f1, open(textfile2, 'r') as f2:
                text1 = f1.read()
                text2 = f2.read()
                t1 = text1.lower()
                t2 = text2.lower()
        except OSError:
            print("There appears to have been a system error. Please try again.")
        except ImportError:
            print("There was an issue with importing of the file. Please try agian.")
        except KeyboardInterrupt:
            print("There has been a KeyboardInterrupt. Please try again.")
        except EOFError:
            print("It looks like one or both files may have been empty. Please try again with the correct file(s).")
    else:
        print("Error! Something unexpected has happened.")

        # There are two different split functions because one is to count punctuation- which will not strip as many characters. The other is with all characters stripped.

    def strip_split_1(text1, text2):
        rm_hyphen1 = text1.replace("--", " ")
        rm_hyphen2 = text2.replace("--", " ")
        # This code removes all unwanted characters but keeps the essentials. Essentials defined as things that end a sentence (?,!,.) as well as other pieces of punctuation
        global strip1
        global strip2
        strip1 = rm_hyphen1.translate({ord(i):None for i in '#$%&()*+/<=>@[\\]^_`{|}~'})
        strip2 = rm_hyphen2.translate({ord(i):None for i in '#$%&()*+/<=>@[\\]^_`{|}~'})
        global split_1
        split_1 = strip1.split()
        global split_2
        split_2 = strip2.split()

    def strip_split_2(t1, t2):
        global split2
        global split1
        rm_h1 = t1.replace("--", " ")
        rm_h2 = t2.replace("--", " ")
        text_1 = rm_h1.translate({ord(i):None for i in '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~'})
        split1 = text_1.split()
        text_2 = rm_h2.translate({ord(i):None for i in '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~'})
        split2 = text_2.split()

    # All functions are defined below.

    # Functions punctuation and composite take in an un-lowered version of the texts so that it is able count the correct amounts of grammar.

    def inner_punc():
        # inner_punc() is to be used inside of punc() since it'll need to be adjusted for later use in composite()
        global profile1
        global profile2
        # call function to find specified punctuation within texts
        strip_split_1(text1, text2)
        list_of_punc = [",",";",":",'"', "'", "-", "?", "!","."]
        # define profiles, obtain keys and set values to 0
        profile1 = dict.fromkeys(list_of_punc, 0)
        profile2 = dict.fromkeys(list_of_punc, 0)
# Need to split the grammar so as to not count all occurences -- e.g. if a period (.) is not at the end of a sentence
        for p in list_of_punc[0:5]:
            for w in strip1:
                if w == p:
                    profile1[w] = profile1.get(w) + 1
            for w in strip2:
                if w == p:
                    profile2[w] = profile2.get(w) + 1
# count - or "'" when they're surrounded by words -- check this by using .isalpha() method
        for i in strip1:
            if i == "'" or i == '-':
                k = strip1.index(i)
                before_ind = k - 1
                after_ind = k + 1
                if strip1[before_ind].isalpha() or strip1[after_ind].isalpha():
                    profile1[i] = profile1.get(i) + 1
        for i in strip2:
            if i == "'" or i == '-':
                k2 = strip2.index(i)
                before_ind2 = k2 - 1
                after_ind2 = k2 + 1
                if strip2[before_ind2].isalpha() or strip2[after_ind2].isalpha():
                    profile2[i] = profile2.get(i) + 1
# I've defined the end of a sentence by looking for the start of a new one. That is, check if index[i] + 2 is in uppercase.
# This is also why there are two different strip_split functions - One needed to retain the Uppercase letters. Also,
# since ? and ! and . are most often associated with the end of a sentence, this is what the program will count.
        for ch in strip1:
            if ch == "." or ch == "?" or ch == "!":
                index_of_1 = strip1.index(ch)
                after_i_1 = index_of_1 + 2
                if strip1[after_i_1].upper():
                    profile1[ch] = profile1.get(ch) + 1
        for ch in strip2:
            if ch == "." or ch == "?" or ch == "!":
                index_of_2 = strip2.index(ch)
                after_i_2 = index_of_2 + 2
                if strip2[after_i_2].upper():
                    profile2[ch] = profile2.get(ch) + 1


    def punctuation():
        inner_punc()
        count1 = sum(profile1.values())
        count2 = sum(profile2.values())
        dist = round(mt.sqrt((count1-count2)**2),2)
        # Need to return vars inside function and then call function using return func() to retrieve values
        return (profile1, profile2, dist)



    def inner_conj():
        ## Need to define an inner function and this is strictly because conj() will be called within composite later but with
        # further added features to the output of the profiles of composite (count of sentences, etc.)
        strip_split_2(t1,t2)
        # list of words to search for "conjunctions"
        words = ["also", "although", "and", "as", "because", "before", "but", "for", "if", "nor", "of","or", "since", "that", "though", "until", "when", "whenever", "whereas","which", "while", "yet"]
        global profile11
        global profile22
        profile11 = dict.fromkeys(words, 0)
        profile22 = dict.fromkeys(words, 0)
        for word in words:
            for w in split2:
                if w == word:
                    profile22[w] = profile22.get(w,0) + 1
            for w in split1:
                if w == word:
                    profile11[w] = profile11.get(w,0) + 1


    def conj():
    # So all we have to do is call inner_conj() within conj and this allows the program the flexibility to use inner_conj within composite()
        inner_conj()
        count11 = sum(profile11.values())
        count22 = sum(profile22.values())
        conj_dist = round(mt.sqrt((count1-count2)**2),2)
        return (profile11, profile22, conj_dist)



    def unigrams():
        strip_split_2(t1,t2)
        # we want to search for each and every word that is within both texts
        global profile1
        global profile2
        global uni_dist
        profile1 = {}
        profile2 = {}
        for w in split1:
            profile1[w] = profile1.get(w,0) + 1
        for w in split2:
            profile2[w] = profile2.get(w,0) + 1
        count1 = sum(profile1.values())
        count2 = sum(profile2.values())
        uni_dist = round(mt.sqrt((count1-count2)**2),2)
        return profile1, profile2, uni_dist


# function to count paragraphs

    def para_count(text):
        paragraph = []
        occ = text.count('\n\n') + 1
        paragraph.append(occ)
        pcount = float(round(sum(paragraph)))
        return pcount


    def composite():
        inner_conj()
        inner_punc()
        period1 = profile1['.']
        question1 = profile1['?']
        exclamation1 = profile1['!']
        sentences1 = period1+exclamation1+question1
        ## profile2
        period2 = profile2['.']
        question2 = profile2['?']
        exclamation2 = profile2['!']
        sentences2 = period2+exclamation2+question2
        # count the number of words
        count_words1 = 0
        count_words2 = 0
        for w in split1:
            count_words1 += 1
        for w in split2:
            count_words2 += 1
        # average words per sentence
        average_words_profile1 = float(round(count_words1/sentences1))
        average_words_profile2 = float(round(count_words2/sentences2))
        para1 = para_count(text1)
        para2 = para_count(text2)
        # average words per paragraph
        average_words_per_paragraph_profile1 = float(round(count_words1/para1))
        average_words_per_paragraph_profile2 = float(round(count_words2/para2))
        # build profiles
        merge1 = {**profile1, **profile11}
        merge2 = {**profile2, **profile22}
        merge1['The average number of words per sentence for profile 1 is'] = average_words_profile1
        merge2['The average number of words per sentence for profile 2 is'] = average_words_profile2
        merge1['The average words per paragraph for profile 1 is'] = average_words_per_paragraph_profile1
        merge2['The average words per paragraph for profile 2 is'] = average_words_per_paragraph_profile2
        # calculate distance
        count_values_1 = sum(merge1.values())
        count_values_2 = sum(merge2.values())
        distance = round(mt.sqrt((count_values_1-count_values_2)**2),2)
        #return results
        return(merge1, merge2, distance)


    # call functions based on conditions met

    if feature == 'composite':
        return composite()
    elif feature == 'unigrams':
        return unigrams()
    elif feature == 'conunctions':
        return conj()
    elif feature == 'punctuation':
        return punctuation()










main('C:/Users/i7-Gamer/Desktop/Hucklebery_Finn.txt','C:/Users/i7-Gamer/Desktop/Banjo_Paterson.txt', 'punctuation')
