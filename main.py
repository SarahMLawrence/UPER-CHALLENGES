'''
UPER = UNDERSTAND, PLAN, EXECUTE, REFLECT

*UNDERSTAND
  - Ask tons of questions
  - What is in the list?
  - What is n?

  - Inputs:
    * list of nums
    * number of items from end of list

  - Outputs:
    * list or "invalid"

  - Edge cases:
    * "invalid" if n > len of list
    * [] empty list if n = 0

*PLAN
  - Utilize psuedo code 
  - Plain english
  - How do we handle edge cases?
    * return invalid if n > len
    * [] if n = 0
  - How do we do the main problem?
    * get last n elements of list
      - slice
    * get all elements starting at len - n
      - arr[len(arr) - n: ]
'''


# Challenge 1
# Write a function that retrieves the last n elements from a list
# Since we have edge cases we need a couple of if statements

def last(arr, n):
  if n > len(arr):
    return 'invalid'
  elif n == 0:
    return []
  # main solution
  return arr[len(arr) - n: ]

print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], 0))