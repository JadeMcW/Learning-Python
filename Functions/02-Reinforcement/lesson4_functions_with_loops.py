"""
   Now that we know how to create functions, let's see how they become super powerful 
   when we combine them with loops! 
   
   Remember loops? They help us repeat things. When we put loops INSIDE functions,
   our mini-machines can do repetitive work for us automatically.

   Think of it like this:
   - A function without loops = a machine that does one thing once
   - A function with loops = a machine that can do things many times!

   Let's create a party invitation system using functions and loops!

"""

# Our function that works with a list using a FOR loop
# This function will create personalized party invitations for everyone!
def send_party_invitations(guest_names, party_theme):
    """This function creates and sends personalized party invitations to everyone on our list."""
    print(f"🎉 Creating {party_theme} party invitations!")
    print(f"Guest list: {guest_names}")
    print()
    
    # The for loop goes through each name in the list, one by one
    for name in guest_names:  # 'name' will be each person's name
        print(f"📧 Invitation for {name}:")
        print(f"   Dear {name},")
        print(f"   You're invited to my {party_theme} party!")
        print(f"   Hope to see you there!")
        print(f"   RSVP soon! 💌")
        print()  # Add a blank line between invitations
    
    # After creating all invitations, let's count how many we made
    total_guests = len(guest_names)  # len() tells us how many items are in the list
    print(f"✅ Successfully created {total_guests} personalized invitations!")
    print(f"All {party_theme} party invitations have been sent! 📮")

# Let's test our party invitation function!
print("=== Party Invitation System ===")

# First, let's create a list of friends to invite
my_friends = ["Emma", "Jack", "Sophia", "Oliver"]
send_party_invitations(my_friends, "Birthday")

print("\n" + "-"*60)

# We can use the same function for a different party with different people!
family_members = ["Aunt Sarah", "Uncle Mike", "Cousin Lisa"]
send_party_invitations(family_members, "Holiday")

print("\n" + "="*60)
print("🌟 Amazing! This function with a loop:")
print("   • Creates personalized invitations for ANY number of people")
print("   • Works with ANY list of names we give it")
print("   • Saves us from writing the same invitation over and over!")
print("   • Can be reused for different parties and different guest lists!")
print("\n💡 Imagine doing this manually for 50 guests... Functions with loops save the day!")
