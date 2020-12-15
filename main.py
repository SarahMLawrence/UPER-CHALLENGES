'''
UPER = UNDERSTAND, PLAN, EXECUTE, REFLECT

Challenge 1
 - Write a function that retrieves the last n elements from a list
 - Since we have edge cases we need a couple of if statements

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


def last(arr, n):
    if n > len(arr):
        return 'invalid'
    elif n == 0:
        return []
    # main solution
    return arr[len(arr) - n:]


print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], 0))
'''
Challenge 2:

 - Given a string of numbers separated by a comma and   space, return the product of the numbers. 
 - Multiply all the numbers


*UNDERSTAND
  - Understand given string 
  - Numbers ", __" separator
  - Need to Multiply all nums in string

  - Edge cases:
    * Can have negatives 
    * Decimals? - no
    * One number? - sure 
    * Empty string? - no 

*PLAN
  - Convert input into numbers 
  - Maybe array 
    * use .split(", ")
  - Multiply array of nums 
    * final_val = 1 
    * For loop over all nums 
      - turn into int 
      - multiply into final_val
'''


def multiply_nums(nums):
    nums_array = nums.split(', ')
    final_val = 1
    for num in nums_array:
        final_val *= int(num)
    return final_val


print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("2, 3"))
print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("10, -2"))
'''
Challenge 3:

 - Create a function that changes specific words into emoticons. Given a sentence as a string, replace the words 'smile', 'grin', 'sad', and 'mad' with their corresponding emoticons


*UNDERSTAND


*PLAN
  - Make new string?
  - Change original string 
    * txt.replace("smile", ":D")
'''


def emotify(txt):
    # The sentence always starts with "Make me"
    # Try to solve without if/else
    txt = txt.replace("smile", ":D").replace("grin", ":)").replace(
        "sad", ":(").replace("mad", ":P")

    return txt


print(emotify("Make me smile, mad, sad"))
