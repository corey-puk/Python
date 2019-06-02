import math as mt



def main(textfile, arg2='listing', normalize='True'):
    global text2


    if arg2 == 'listing' and normalize == 'False':
        try:
            with open(textfile, 'r') as f1:
                text1 = f1.read()
                text1 = text1.lower()
        except IOError:
            print("There was an error with the file. Please try again.")
    elif arg2=='listing' and normalize != 'False':
        try:
            with open(textfile, 'r') as f1:
                text1 = f1.read()
                text1 = text1.lower()
        except IOError:
            print("There was an error with the file. Please try again.")
    elif arg2 != 'listing' and normalize == 'False':
        try:
            with open(textfile, 'r') as f1, open(textfile2, 'r') as f2:
                text1 = f1.read()
                text1 = f1.lower()
                text2 = f2.read()
                text2 = text2.lower()
        except IOError:
            print("There was an error with the file. Please try again.")
    elif arg2 != 'listing' and normalize != 'False':
        try:
            with open(textfile, 'r') as f1, open(textfile2, 'r') as f2:
                text1 = f1.read()
                text1 = f1.lower()
                text2 = f2.read()
                text2 = f2.lower()
        except IOError:
            print("There was an error with the file. Please try again.")
    else:
        print("Something has gone wrong!")

#calculate distance between both texts - What I've done is sum up over all the values of the two dictionaries and divide that by their respective sentence counts
#I then take the square root of the squared 'distance' as per the forumla.


        if arg2 != 'listing' and normalize != 'False':
            def dist():
                pf1 = float(profile1_sum/scount)
                pf2 = float(profile2_sum/scount2)
                global dist
                dist = mt.sqrt((pf1-pf2)**2)
                print("The distance between the two texts is", dist)
            dist()


# Two functions processf1 and processf2 both take the text files and replace, count words, sentence, parahraphs and determine the words per sentence and paragraph

    def processf1(text1):
        def sent_count():
            for ch in '"#$%()*+,-/<=>@[\\]^_{|}~':
                global sent_text1
                sent_text1 = text1.replace(ch, ' ')
                sent_split = sent_text1.split()
                sentences_count = []
                x = sent_text1.count('?') + 1
                z = sent_text1.count('!') + 1
                y = sent_text1.count('.') + 1
                sentences_count.append(x)
                sentences_count.append(y)
                sentences_count.append(z)
                global scount
                scount = int(sum(sentences_count))
                words_s = len(sent_split)
                global av_sent
                av_sent = float(words_s/scount)
        sent_count()

        # define paragraph counter - this function counts paragraphs and words per paragraph -
        # As there are 2 texts, 2x most things can be assumed - I'm trying to minimise comment usage across duplicate code

        def para_count():
            paragraph = []
            occ = sent_text1.count('\n\n') + 1
            paragraph.append(occ)
            pcount = int(sum(paragraph))
            #sort through the assorted characters that may appear in texts
            for ch in '!"#$%()*+,-./<=>?@[\\]^_{|}~':
                para_amend = sent_text1.replace(ch, ' ')
                paratext = para_amend.split()
                words_per_para = len(paratext)
                global words_p
                words_p = float(words_per_para/pcount)


            #initialise dictionary 1

            profile1 = {}

            global profile1_sum
            profile1_sum = sum(profile1.values())

            global word

            profile1['Words per sentence'] = av_sent
            profile1['Words per paragraph'] = words_p

            # I 'pop' the keys so that they do not enter through loop when normalising. I then add them back in using l.append()

            # I also create another dictionary that will only utilised when conditions are met

            profile1_1 = profile1
            profile1_1.pop('Words per paragraph')
            profile1_1.pop('Words per sentence')

            # This starts the accumulator for the dictionary_word_counter

            for word in paratext:
                profile1[word] = profile1.get(word,0) + 1

            # sorts and lists dictionary vals and keys

            global uniqueWord1
            uniqueWord1 = list(profile1.keys())
            uniqueWord1.sort()


            if arg2=='listing' and normalize=='False':
                for w in uniqueWord1:
                    list_one = (w, (profile1[w]))
                    print(list_one)


            if arg2=='listing' and normalize != 'False':
                def conv():
                    wpp = print("The number of words per paragraph is", words_p)
                    wps = print("The number of words per sentence is", av_sent)
                    uniq = list(profile1_1.keys())
                    global list_two
                    for w in uniq:
                        list_one = [w, float(profile1_1[w]/scount)]
                        print(list_one)
                conv()

        para_count()

    processf1(text1)



    def processf2(text2):
        def sent_count():
            for ch in '"#$%()*+,-/<=>@[\\]^_{|}~':
                global sent_text2
                sent_text2 = text2.replace(ch, ' ')
                sent_split = sent_text2.split()
                sentences_count = []
                x = sent_text2.count('?') + 1
                z = sent_text2.count('!') + 1
                y = sent_text2.count('.') + 1
                sentences_count.append(x)
                sentences_count.append(y)
                sentences_count.append(z)
                scount2 = int(sum(sentences_count))
                words_s = len(sent_split)
                global av_sent
                av_sent = float(words_s/scount2)
        sent_count()


        def para_count():
            paragraph = []
            occ = sent_text2.count('\n\n') + 1
            paragraph.append(occ)
            pcount = int(sum(paragraph))
            for ch in '!"#$%(),.*+\,-\./<=>?@[\\]^_{|}~':
                para_amend = sent_text2.replace(ch, ' ')
                paratext = para_amend.split()
                words_per_para = len(paratext)
                global words_p
                words_p = float(words_per_para/pcount)

                #initialise dictionary var_2

            profile2 = {}

            profile2_1 = profile2

            global profile2_sum
            profile2_sum = sum(profile2.values())

            # input each word and accumulation of count as key:value into dictionary, with key being word/syntax and value being count

            global w
            for w in paratext:
                profile2[w] = profile2.get(w,0) + 1

                    # sort into unique elements

            global uniqueWord2
            uniqueWord2 = list(profile2.keys())
            uniqueWord2.sort()



            if arg2 == 'listing' and normalize != 'False':
                def conv2():
                    proflile2_1 = profile2
                    wpp = print("The number of words per paragraph in text 2 is", words_p)
                    wps = print("The number of words per sentence in text 2 is", av_sent)
                    uniq2 = list(profile2_1.keys())
                    for w in uniq2:
                        list_two = [w, float(profile2_1[w]/scount)]
                        print(list_two)
            conv2()



        para_count()

    processf2(text2)










main('sample.txt','listing')
