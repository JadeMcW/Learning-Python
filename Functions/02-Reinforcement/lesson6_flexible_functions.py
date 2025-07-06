"""
   You know how some things in life have default settings that work most of the time, 
   but you can change them if you want? Like how your phone has a default ringtone, 
   but you can choose a different one if you prefer?

   Functions can work the same way! We can give our functions "default values" for 
   some parameters. This means:
   - If someone calls the function and doesn't specify that parameter, it uses the default
   - If they DO specify it, it uses their choice instead

   Let's create a flexible greeting function to see how this works!

"""

# A function with default values - this makes it super flexible!
def greet_someone(name, greeting="Hello", style="friendly"):
    """This function greets someone, but has default values for greeting and style."""
    # If no greeting is provided, it will use "Hello"
    # If no style is provided, it will use "friendly"
    
    print(f"📝 Creating greeting with:")
    print(f"   Name: {name} (this is required)")
    print(f"   Greeting: {greeting} (default: Hello)")
    print(f"   Style: {style} (default: friendly)")
    
    # Different styles create different punctuation
    if style == "friendly":
        punctuation = "! 😊"
    elif style == "formal":
        punctuation = "."
    elif style == "excited":
        punctuation = "!! 🎉"
    else:
        punctuation = "."
    
    # Build the greeting message
    message = f"{greeting}, {name}{punctuation}"
    print(f"💬 Result: {message}")
    print("-" * 40)
    return message

# Let's see how defaults work - this is the magic!
print("=== Flexible Greeting Function ===")

print("1. Using ALL defaults (only providing the required name):")
greet_someone("Emma")  # Only giving the name, using default greeting and style

print("\n2. Changing just the greeting (keeping default style):")
greet_someone("Jack", "Hi there")  # Giving name and greeting, using default style

print("\n3. Changing both greeting and style:")
greet_someone("Sophia", "Good morning", "formal")  # Giving all three parameters

print("\n4. Using keyword arguments (we can put them in any order!):")
greet_someone(style="excited", name="Oliver", greeting="Congratulations")

print("\n5. Mix and match however we want:")
greet_someone("Maya", style="excited")  # Using default greeting but custom style

print("\n" + "="*60)
print("� Flexible functions with defaults are amazing because:")
print("   • They're super easy to use - just provide what you need!")
print("   • The defaults handle the common cases automatically")
print("   • But you can still customize everything when needed")
print("   • One function can handle simple AND complex situations!")
print("\n💡 Think about it: Would you rather have 10 different greeting functions")
print("   or 1 flexible function that can handle any greeting style?")
