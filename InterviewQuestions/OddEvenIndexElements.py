#find even index elements
def IndexElements(fl):
   Eresult=[]
   Oresult=[]
   for ind ,val in enumerate(fl):
        if ind%2==0:
         Eresult.append(val)
        else:
         Oresult.append(val)
   return Eresult,Oresult


def main():
    try:
     lst=input('Enter nums seperated by')
     flist=list(map(int,lst.split()))
     even, odd=IndexElements(flist)
     print('even:' ,even,'odd: ',odd)

    except ValueError:
        print('Invalid input')


if __name__=='__main__':
    main()