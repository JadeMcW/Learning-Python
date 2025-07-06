"""
   Now we know how to create lists and add items to them.
   But what if we need to find something specific in our list?
   Like finding the longest word, or the biggest number?
   
   We need to look at each item in the list, one by one, and compare them.
   It's like looking through a box of books to find the thickest one.
   You pick up each book, check how thick it is, and remember the thickest so far.
"""

"""
   Key concepts to highlight:

      Accessing items: We use [0], [1], [2] to get items by position.
      
      len(): Gets the length/size of strings or lists.
      
      Comparison: Using > to compare which is bigger/longer.
      
      Variables to remember: Keeping track of the "best so far".
      
      range(len(list)): A way to go through all positions in a list.
"""

# We a list of the names of books
books = ["Python", "JavaScript", "HTML", "CSS"]

print("Our book list:", books)

# Let's find the longest book title step by step
print("\n--- Finding the longest book title ---")

# Start by assuming the first book is the longest
longest_book = books[0]  # Start with "Python"
print(f"Starting with: '{longest_book}' (length: {len(longest_book)})")

# Now check each book one by one
print("Checking each book:")
for i in range(len(books)):
    current_book = books[i]
    current_length = len(current_book)
    print(f"  Book {i + 1}: '{current_book}' has {current_length} letters")
    
    # Is this book longer than our current longest?
    if current_length > len(longest_book):
        print(f"    → This is longer! New longest: '{current_book}'")
        longest_book = current_book
    else:
        print(f"    → Not longer than '{longest_book}'")


""" -------------------------------------------------------------------------------------------- """

""" 
# We a list of animals names
animals = ["cat", "elephant", "dog", "butterfly"]

print("Our animal list:", animals)

# Let's find the longest animal name step by step
print("\n--- Finding the longest animal name ---")

# Start by assuming the first animal name is the longest
longest_animal = animals[0]
print(f"Starting with: '{longest_animal}'") # Start with cat

# Check each animal
for i in range(len(animals)):
    current_animal = animals[i]
    if len(current_animal) > len(longest_animal):
        longest_animal = current_animal

print(f"The longest animal name is: '{longest_animal}'")

# We can also find the shortest
print("\n--- Finding the shortest animal name ---")
shortest_animal = animals[0]  # Start with first animal

for i in range(len(animals)):
    current_animal = animals[i]
    if len(current_animal) < len(shortest_animal):
        shortest_animal = current_animal

print(f"The shortest animal name is: '{shortest_animal}'")
"""
"""
   Your turn: Create a list of 4 numbers called my_numbers.
   Then find the biggest number in the list by checking each number one by one.
   Print each step to show how you're comparing the numbers.
"""
