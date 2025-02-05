#A palindrome is a word, phrase, number, or sequence that reads the same backward as forward, ignoring spaces, punctuation, and capitalization.
def isPalindrom(num):
    original=str(num)
    return original==original[::-1]

num=input('Enter a number to find its a palindrome or not? :')
if isPalindrom(num):
    print('Its a palindrome')
else:
    print('Its not a palindrome')