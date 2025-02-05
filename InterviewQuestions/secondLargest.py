def secondLargest(nums):
    unique_nums = sorted(set(nums))
    if len(unique_nums) < 2:
        return None
    return  unique_nums[-2]
def main():

      lst=input('Enter a list: ')
      num = list(map(int,lst.split()))
      result=secondLargest(num)
      if result is not None:
            print(f"The second largest number is: {result}")
      else:
            print("Error: The list must contain at least two distinct numbers.")

if __name__=='__main__':
  main()