def reverse(s):
    RS=''
    for i in range(-1,-len(s)-1,-1):
        RS+=s[i]
    return RS


def main():
    string=input('Enter a string')
    r=reverse(string)
    print(f'Reverse of string is: {r}')


if __name__=='__main__':
  main()