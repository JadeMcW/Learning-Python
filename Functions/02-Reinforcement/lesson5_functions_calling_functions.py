"""
   Here's something really cool: our functions can work together as a team!
   Just like how you might ask a friend to help you with something, one function 
   can "call" (ask for help from) another function.

   Think of it like this:
   - You have a function that knows how to add numbers
   - You have another function that knows how to multiply numbers  
   - You can create a NEW function that uses BOTH of them to solve bigger problems!

   Let's create a simple calculator where functions work together!

"""

# Let's start with two simple "helper" functions
def add_two_numbers(first_number, second_number):
    """This function knows how to add two numbers together."""
    # It's a simple function that just adds and returns the result
    result = first_number + second_number
    print(f"   🔢 Adding: {first_number} + {second_number} = {result}")
    return result

def multiply_two_numbers(first_number, second_number):
    """This function knows how to multiply two numbers together."""
    # Another simple function that just multiplies and returns the result
    result = first_number * second_number
    print(f"   🔢 Multiplying: {first_number} × {second_number} = {result}")
    return result

# Now, the main function that uses OTHER functions to solve a bigger problem
def calculate_rectangle_area_and_perimeter(length, width):
    """This function calculates both area and perimeter of a rectangle using helper functions."""
    print(f"📐 Let's calculate for a rectangle that is {length} × {width}")
    
    # For AREA, we need to multiply length × width
    # Instead of writing length * width, we'll use our multiply function!
    print("Step 1: Calculate the area...")
    area = multiply_two_numbers(length, width)  # Calling our multiply function
    
    # For PERIMETER, we need to calculate 2 × (length + width)
    # First, let's add length + width using our add function
    print("Step 2: Calculate length + width...")
    length_plus_width = add_two_numbers(length, width)  # Calling our add function
    
    # Then multiply that result by 2 using our multiply function
    print("Step 3: Calculate perimeter...")
    perimeter = multiply_two_numbers(length_plus_width, 2)  # Calling multiply again!
    
    print(f"✅ Final Results: Area = {area}, Perimeter = {perimeter}")
    # Return both results
    return area, perimeter

# Let's test our teamwork function!
print("=== Rectangle Calculator (Functions Working Together) ===")
print("Testing with a 5×3 rectangle:")
my_area, my_perimeter = calculate_rectangle_area_and_perimeter(5, 3)

print("\n" + "-"*60)
print("Testing with a 10×7 rectangle:")
my_area2, my_perimeter2 = calculate_rectangle_area_and_perimeter(10, 7)

print("\n" + "="*60)
print("🌟 Amazing! When functions work together:")
print("   • Each function has ONE job and does it well")
print("   • The main function coordinates all the helper functions")
print("   • We can solve complex problems by combining simple functions!")
print("   • Our code becomes like a team of specialists!")
print("\n💡 Instead of one big complicated function, we have many small, clear functions")
print("   working together. This makes our code easier to understand and fix!")
