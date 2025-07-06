"""

   So far, our functions have only printed things. 
   But often, we want the function to calculate something and 'give' us that result
   to use it elsewhere in our program. It's like a recipe that gives you back a cake, 
   it doesn't just tell you 'I made a cake'. 
   The return keyword makes the function 'hand over' a value to us."

   Key concepts to highlight:

      return: Sends a value out of the function.

      Saving the result: When a function has a return, we can save the value it returns in a variable.

      Using the result: Once the value is in a variable, we can use it in print(), in an if statement, in other operations, etc.

      None by default: If a function has no return statement, Python automatically returns None (which means 'nothing').

"""

# This function adds two numbers and returns the result.
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total # Here the function 'delivers' the value of 'total'

# Now, the function's result can be saved in a variable
print("--- Using the result of the sum ---")
result_of_my_sum = add_two_numbers(10, 5)
print(f"The result of the sum is: {result_of_my_sum}")

# We can use that result directly in a conditional
if add_two_numbers(20, 10) > 25: # The function runs here and returns 30
    print("The sum was greater than 25!")
else:
    print("The sum was 25 or less.")

# Functions can also return multiple values (Python packs them into a tuple)
def get_min_max_list(list_of_numbers):
    minimum = min(list_of_numbers)
    maximum = max(list_of_numbers)
    return minimum, maximum # Returns two values, packed in a tuple

example_numbers = [4, 1, 8, 2, 7]
# We can 'unpack' the values directly into variables
my_min, my_max = get_min_max_list(example_numbers)
print(f"From the list {example_numbers}, the minimum is {my_min} and the maximum is {my_max}.")

"""

   Your turn: Create a function called is_even_or_odd() that receives a number. 
   The function should return the string 'Even' if the number is even, and 'Odd' 
   if it's odd. Then, call the function with the number 7 and with the number 10, 
   and save the result in a variable to print it


"""
