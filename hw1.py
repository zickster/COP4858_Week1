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
    
    letter_min = raw_input('Type in the MIN of letters.\n')
    letter_max = raw_input('Type in the MAX of letters.\n')

    letter_min = int(letter_min) +1
    letter_max = int(letter_max) +1
    
    textfile = open('namespace.txt', 'r')
    #content = textfile.read()
    

    dict_result = open ('namespace-result.txt', 'w')
    
    for line in iter(textfile):
        if len(line) <= int(letter_max):
            if len(line) >= int(letter_min):
                dict_result.write(line)

    textfile.close()
    dict_result.close()
    
    
    
    """Creates a new file with only words with
       length >= min and length <= max
    """




def gematria(wordToMatch, filename):
    #replace pass below with your code
    pass

def credit_check(card_num):
    #replace pass below with your code
    pass
    
