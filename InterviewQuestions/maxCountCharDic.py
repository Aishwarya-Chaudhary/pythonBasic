#Find max occuring char in string using dictionary
def maxOccuringChar(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return max(dic.keys())
str1=input('Enter a String')
print(maxOccuringChar(str1))