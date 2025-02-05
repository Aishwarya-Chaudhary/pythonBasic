#If two words are anagrams, they must contain the same characters with the same frequency.
# So, the word "listen" can be rearranged into "silent,"
# but "listen" and "silently" are not anagrams because they have different letters.They are case insensitive and blank space doent matter
def anagramCheck(s1,s2):
    L_s1=s1.replace(" ","").lower()
    L_s2 =s2.replace(" ", "").lower()
    return sorted(L_s1)==sorted(L_s2)
str1=input('Enter string 1')
str2=input('Enter string 2')
if anagramCheck(str1,str2):
    print(f'[{str1} and {str2} are anagrams of each other')
else:
    print(f'[{str1} and {str2} are Not anagrams of each other')
