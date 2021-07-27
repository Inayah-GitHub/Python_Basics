"""
This function counts down from n to 1, returning a sum of the positive numbers within this range. 
Input: A number n
Output: The sum of positive numbers upto and including n 
"""
def sum_positive_numbers(n):
    if n < 1:
        return n
    return n + sum_positive_numbers(n-1)
  
"""
This function compares two numbers and returns them in increasing order
Inputs: Two numbers to be compared
Outputs: The same two numbers, arrange in increasing order
"""
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1
  
""" 
This function returns "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0.
Input: Number to be considered
Output: String detailing whether the number is positive, negative or zero
"""
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"
  
"""
This function determines whether a number is the result of raising a specified base to the power of another integer
Inputs: The number and base to be considered
Output: True or False 
"""
def is_power_of(number, base):
  # Base case: when number is smaller than base
  if number/base == 1:
        return True
    # Recursive case: keep dividing number by base
  elif number/base < 1:
    return False 
  return is_power_of(number/base, base)

"""
The following code checks whether the first and last letters of a message are the same
Input: Message as a string
Output: True or False 
"""
def first_and_last(message):
    if message == "":
        return True
    elif message[0] != message[-1]:
        return False
    else:
        return True
