""" 

   Our welcome mini-machine always says the same thing. But what if we want it to greet 
   someone by their name? To do that, we need to 'give ingredients' to our recipe. 
   These ingredients are called parameters.

Key concepts to highlight:

   () with names inside: The names inside the parentheses are the parameters. They are like 'slots' where the function expects to receive information.

   Passing arguments: When we call the function, we 'pass' the values that will go into those parameters.

   Order matters: The order of the values you pass must match the order of the parameters.

"""

# This function now expects two 'ingredients': 'name' and 'age'
def introduce_person(name, age):
    print(f"Hi, my name is {name} and I am {age} years old.")
    print(f"It's a pleasure to meet you, {name}!")

# Now, when we call the function, we give it the 'ingredients'.
print("--- Introducing the first person ---")
introduce_person(25, "Alice") # This is wrong

print("\n--- Introducing another person ---")
introduce_person("Bob", 30)

# We can even use variables that we already have
user_name = input("\nWhat is your name? ")
user_age = int(input("How old are you? ")) # We convert it to a number
introduce_person(user_name, user_age)

""" 

   Your turn: Create a function called calculate_rectangle_area() 
   that receives two parameters: length and width. Inside the function, 
   print the area of the rectangle using those parameters. 
   Then, call the function to calculate the area of a 5x8 rectangle 
   and another one that is 12x4.

"""