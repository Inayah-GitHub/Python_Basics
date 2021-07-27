"""
Returns, in upper case, the initials of the words contained in the phrase received.  
Input: Phrase to be abbreviated 
Output: Abbreviation 
"""
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()
  
"""
The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, 
up to and including the maximum that's passed into the function. 
Input: Maximum number
Output: All of the positive numbers that are divisible by two, up to and including the maximum 
"""
def even_numbers(maximum):
	return_string = ""
	for x in range(1, maximum+1):
		if x%2 == 0:
			return_string += str(x) + " "
	return return_string.strip()

"""
The counter function accepts start and stop parameters, 
decides accordingly whether to count up or down and then counts from start to stop. 
Inputs: Start and Stop parameters
Outputs: The full count from start to stop, returned as a string
"""
def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x = x-1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x = x+1
	return return_string

""" 
The digits(n) function counts and returns however many digits a number has. 
Input: A number (n)
Ouput: The number of digits that the number n has
"""
def digits(n):
    count = 0
    if n == 0:
        return 1
    while (n)>=1:
        count += 1
        n = n/10
        return count
 
""" 
The list_of_prime_factors function prints all the prime factors of a number 
Input: The number that you want the prime factors of 
Outputs: The number's prime factors 
"""
def list_of_prime_factors(number):
  # Begins by initialising the first factor as 2 (the first prime number)
  factor = 2
  # Script runs until the factor is larger than the number
  while factor <= number:
    # Checks if the factor is a divisor of number
    if number % factor == 0:
      # If it is, the code prints it  
      print(factor)
      # and then divides the original number, resetting the 'number' parameter to the result of this calculation 
      number = number / factor
    else:
      # If it's not, the factor is incremented by 1
      factor += 1
  return "Finished"

"""
* This code reads an integer number from the console and stores the result in the veribale n. 
* It then reads 'n' floating point numers from the console and stores them in a list.
* The list is sorted in the reverse order from highest to lowest. 
* Finally, the script loops over the elements in the list and prints each on its own line to the console. 
Inputs = n (the number of flaoting point numbers to be read) & 'n' floating point numbers
Outputs = n floating point numbers, one per line, sorted from highest to lowest 
"""
n = int(input())
num_list = []
while len(num_list) < n:
    appen = int(input())
    num_list.append(appen)
    num_list.sort(reverse=True)
for i in num_list:
    print('\n' + str(i))
