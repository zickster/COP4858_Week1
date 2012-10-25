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
    lenght = len(word) -1
    vowel = 'aeiouAEIOU'
    vowel_end = word[lenght]
    vowel_check = 'false'
    
    """Syllables are determined as follows:
       Each sequence of vowels a e i o u y,
          except for the last e in a word,
       is a vowel.
       However, if that algorithm yields a count of 0, change it to 1.
    """
    for letter in word:
        print 1
        if letter in vowel:
            count += 1
            print 1
#           if lenght in vowel:
            if vowel_check is vowel.find(vowel_end)==1
                print 'true'
##            print 'Count %d' %count
##            print 'vowel_check %s' %vowel_check
##            if vowel_check is 'True':
##                count = -1
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
    
