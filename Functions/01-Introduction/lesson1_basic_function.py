
"""
   So far, we've written code that runs from top to bottom. But sometimes, we do the same thing over and over. 
   Imagine you want to print a 'Welcome' message in different parts of your program. You could write print('Welcome to the program!') every time. 
   But what if you decide to change the message later? You would have to change it in every single spot.
   That's where functions come in. A function is like a mini-machine or a recipe that you create once, 
   and then you can 'call' that machine to do its job whenever you need it. This way, if you change the 'recipe,' it changes everywhere you use it.

"""

""" 

   Key concepts to highlight:

      def: The keyword to "define" a function.

      Function Name: What we call it (like the "Welcome Mini-Machine").

      (): Parentheses, which will be empty for now.

      :: A colon, which indicates that the function's body starts next.

      Indentation: Super important! The code that belongs to the function must be indented (with spaces or tabs). 
      Python uses indentation to know what is inside the function.

"""


# We define our first mini-machine: 'greet_welcome'
# Everything indented under 'def' is part of the function.
def greet_welcome():
   print("---------------------------------")
   print("Welcome to my amazing program!")
   print("I hope you die")
   print("---------------------------------")

# Now, we 'call' our mini-machine to do its job.
print("The program is about to start...")
greet_welcome() # Here we 'call' the function

print("\n--- A while later, in another part of the program ---")
# We can call it again, without rewriting anything!
greet_welcome()

print("\nThe program has ended. See you soon!")

""" 

   Your turn: Create your own function called show_instructions() that, when called, 
   prints 3 lines of text explaining a simple game (for example: '1. Guess a number. 2. 
   I'll give you hints. 3. Win!'). Then, call that function twice in your code.

"""