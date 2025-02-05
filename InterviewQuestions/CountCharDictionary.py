#Word frequency count:count the frequency of each word in string using a dictionary
def word_Count(s):
    words=s.lower().split()
    word_count={}
    for i in words:
      if i in word_count:
          word_count[i]+=1
      else:
          word_count[i]=1
    return word_count

str1=input('Enter a String')
print(word_Count(str1))


