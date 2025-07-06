"""
   Sometimes we don't want all the items in a list - we only want some of them.
   Like when you have a list of numbers and you only want the positive ones,
   or when you have a list of words and you only want the long ones.
   
   This is called "filtering" - like using a coffee filter that only lets certain things through.
   We look at each item and decide: "Do I want this one? Yes or no?"
   The ones we want go into a new list.
"""

"""
   Key concepts to highlight:

      Empty list: Starting with [] to collect items we want.
      
      append(): Adding items to our new list.
      
      Conditions: Using if statements to decide what we want.
      
      Positive/Negative: Numbers > 0 are positive, < 0 are negative.
      
      Building new lists: Creating separate lists instead of changing the original.
"""

# We have a list of numbers - some positive, some negative
numbers = [5, -2, 8, -1, 3, -4, 7, -3, 2]
print("Original numbers:", numbers)

# Let's separate them into positive and negative numbers
# We start with two empty lists
positive_numbers = []  # This will hold numbers > 0
negative_numbers = []  # This will hold numbers < 0

print("\nLet's separate positive and negative numbers:")

# Look at each number one by one
for i in range(len(numbers)):
    current_number = numbers[i]
    print(f"Looking at number: {current_number}")
    
    # Decide which list it belongs to
    if current_number > 0:
        positive_numbers.append(current_number)
        print(f"  → {current_number} is positive, adding to positive list")
    else:
        negative_numbers.append(current_number)
        print(f"  → {current_number} is negative, adding to negative list")

# Show our results
print(f"\nPositive numbers: {positive_numbers}")
print(f"Negative numbers: {negative_numbers}")
print(f"We found {len(positive_numbers)} positive and {len(negative_numbers)} negative numbers")

""" ---------------------------------------------------------------------------- """

""" 
# Let's try another example: filtering words by length
print("\n--- Filtering words by length ---")
words = ["cat", "elephant", "dog", "butterfly", "ant"]
print("Original words:", words)

# We want only long words (more than 3 letters)
long_words = []
short_words = []

print("\nChecking each word:")
for i in range(len(words)):
    current_word = words[i]
    word_length = len(current_word)
    print(f"'{current_word}' has {word_length} letters")
    
    if word_length > 3:
        long_words.append(current_word)
        print(f"  → Long word! Adding to long_words list")
    else:
        short_words.append(current_word)
        print(f"  → Short word! Adding to short_words list")

print(f"\nLong words (more than 3 letters): {long_words}")
print(f"Short words (3 letters or less): {short_words}")
"""

""" ---------------------------------------------------------------------------- """

""" 
# One more example: finding numbers bigger than 5
print("\n--- Finding big numbers ---")
all_numbers = [2, 8, 1, 9, 4, 7, 3, 6]
big_numbers = []

print("Original numbers:", all_numbers)
print("Looking for numbers bigger than 5:")

for i in range(len(all_numbers)):
    current_num = all_numbers[i]
    if current_num > 5:
        big_numbers.append(current_num)
        print(f"  {current_num} is bigger than 5 ✓")
    else:
        print(f"  {current_num} is not bigger than 5")

print(f"\nNumbers bigger than 5: {big_numbers}")
"""
"""
   Your turn: Create a list called grades with some numbers representing test scores
   (like 85, 67, 92, 78, 88, 73, 95). Then create two new lists: one for passing 
   grades (70 or higher) and one for failing grades (below 70).
   Print each step to show which grades go where.
"""
