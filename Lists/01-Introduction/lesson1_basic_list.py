"""
   So far, we've worked with individual variables like name = "Alice" or age = 25.
   But what if we need to store multiple related items, like a list of friends' names?
   We could create separate variables: friend1 = "Alice", friend2 = "Bob", friend3 = "Charlie"...
   But that's not practical! What if we have 200 friends?
   
   That's where lists come in. A list is like a container that can hold multiple items in order.
   Think of it like a shopping list where you write down everything you need to buy.
"""

"""
   Key concepts to highlight:

      []: Square brackets create a list.
      
      Items: The things inside the list, separated by commas.
      
      Order: Lists remember the order of items (first, second, third, etc.).
      
      Index: Each item has a position number starting from 0.
      
      len(): Function to count how many items are in the list.
"""

# We create our first list: a list of friends
# Everything inside the square brackets [] is part of the list
my_friends = ["Alice", "Bob", "Charlie"]

# We can see what's in our list
print("My friends list:")
print(my_friends)

# We can check how many friends we have
total_friends = len(my_friends)
print(f"I have {total_friends} friends")

# We can access individual friends by their position (starting from 0)
print(f"My first friend is: {my_friends[0]}")  # Alice (position 0)
print(f"My second friend is: {my_friends[1]}")  # Bob (position 1)
print(f"My third friend is: {my_friends[2]}")   # Charlie (position 2)

# We can add a new friend to our list
my_friends.append("Diana")
print(f"After adding Diana: {my_friends}")

# We can check if someone is in our friends list
if "Bob" in my_friends:
    print("Bob is my friend!")
else:
    print("Bob is not in my friends list")

"""
   Your turn: Create your own list called favorite_colors with 3 colors.
   Then print the list, print how many colors you have, and print your first 
   and last favorite color. Finally, add one more color to the list.
"""

