import string
count = 0

def vowel_count():
    word = raw_input('Type in a Word.\n')
    count = 0
    vowel = 'aeiouyAEIOUY'
    """Returns the number of a, e, i, o, u, & y's
       Remember, case should not matter.
    """
    for letter in word:
        if letter in vowel:
            count += 1
    print ('There are %d' %count + ' vowels in the word %s' %word +'.')        

        
def syllable_count():
    word = raw_input('Type in a Word.\n')
    count = 0
    vowel_count = 0
    lenght = len(word) -1
    vowel = 'aeiouyAEIOUY'
    vowel_end = word[lenght]
    vowel_check = 'false'
    

    for letter in word:
        if letter in vowel:
            count += 1
            vowel_count += 1
        elif vowel_count == 2:
            count -= 1
        else:
            vowel_count = 0
    if vowel_end == 'e':
        count -= 1
    if count < 1:
        count = 1
    print count    
          
        
            
   

#def filter_dict(filename, min, max):
def filter_dict():
    import shutil
    
    letter_min = int(raw_input('Type in the MIN of letters.\n'))
    letter_max = int(raw_input('Type in the MAX of letters.\n'))

    letter_min +=1
    letter_max +=1
    
    textfile = open('ospd.txt', 'r')
    #content = textfile.read()
    dict_result = open ('filtered-dictionary file.txt', 'w')
    
    for line in iter(textfile):
        if len(line) <= int(letter_max):
            if len(line) >= int(letter_min):
                dict_result.write(line)

    textfile.close()
    dict_result.close()
    


def gematria_dic():
    import shutil
    
    sum = 0
    sum2 = 0
    dic_sum = 0
    word_sum = 0

##    word = raw_input('Type in a Word.\n')
##    
##    for d in word:
##        sum = int(ord(d)) - ord('a') + 1
##        word_sum = sum + word_sum
##	
##    print word_sum

    textfile = open('namespace.txt', 'r')
    for e in iter(textfile):
        for e in e:
            sum2 = int(ord(e)) - ord('a') + 1
            dic_sum = sum2 + dic_sum
            if e == "\n":
                dic_sum =0
##            print e
##            print dic_sum



def gematria():
    import shutil
    sum = 0
    sum2 = 0
    dic_sum = 0
    word_sum = 0

    word = raw_input('Type in a Word.\n')
    
    for d in word:
        sum = int(ord(d)) - ord('a') + 1
        word_sum = sum + word_sum
	
    print word_sum

    textfile = open('ospd.txt', 'r')
    for e in iter(textfile):
        found_sum= e
        for e in e:
            sum2 = int(ord(e)) - ord('a') + 1
            if e == "\n":
                if dic_sum == word_sum:
                    print found_sum
                dic_sum =0
            else:
                dic_sum = sum2 + dic_sum
            
      
    

def credit_check(card_num):
    #replace pass below with your code
    pass
    
