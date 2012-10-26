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
          
        
            
   

def filter_dict(filename, min, max):
    """Creates a new file with only words with
       length >= min and length <= max
    """
    #replace pass below with your code
    pass

def gematria(wordToMatch, filename):
    #replace pass below with your code
    pass

def credit_check(card_num):
    #replace pass below with your code
    pass
    
