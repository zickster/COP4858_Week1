#nums = "123456789"
import string

def check_isbn():
    nums = raw_input('What is the ISBN number?\n')
    while not is_valid(nums):
        print "Error! Please enter 9 Digits."
        nums = raw_input('What is the ISBN number?\n')
    print "Checksum character is:", compute_checksum(nums)
def is_valid(input):
    """Make sure that the inpu is 9 digits"""
    return len(input) == 9 and input.isdigit()

def compute_checksum(nums):
    """Compute the checksm for the ISBN string"""
    sum = 0
    place = 1
    for d in nums:
            sum = sum + place * string.atoi(d)
            place = place + 1
    #print sum

    remainder = sum % 11
    if remainder <10:
        return remainder
    else:
        return 'X'



    


