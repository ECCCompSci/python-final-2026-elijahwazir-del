# ============================================================
# Python Final Project 2026
# Name: Elijah
# Date: 5/7/2026
# Project Title: THE AMIZING WACKY QUIZ!!1!!1!!
# Description: (Write 1-2 sentences explaining what your program does)
# ============================================================


# ---- SECTION 1: Setup / Variables ----
# Create your starting variables here.
# Example: player_name = ""
name = input("your name:")
yes = 0

# ---- SECTION 2: Welcome Message ----
# Greet the user and explain what your program does.

print("Welcome!")
print(name)



# ---- SECTION 3: Get Input from User ----
# Use input() to ask the user for information.
# Remember: input() always returns a string.
# Use int() or float() if you need a number.

# Example:
# player_name = input("What is your name? ")
# score = int(input("Enter a number: "))
question = input("Did you wake up today?: ")
if question == "yes":
    print("Good for you")
elif question == "no":
    print("How are you here then")
else:
    print("Thats not a valid answer")

question2 = input("Did you remeber?: ")
if question == "yes":
    print("Is that true?")
elif question == "no":
    print("did you really")
else:
    print("that isnt the answer")

question = input("did you have breakfast today?: ")
if question == "yes":
    print("i bet it was good")
elif question == "no":
    print("were you not hungry?")
else:
    print("stop putting random answers.")
# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.

# Example:
# if score >= 90:
#     print("Great job!")
# elif score >= 70:
#     print("Good work!")
# else:
#     print("Keep practicing!")
if yes >= 3:
    print("you answered all of them yes")
elif yes <= 1:
    print("you answered mostly no")
elif yes == 0:
    print("you answered none of them yes")




# ---- SECTION 5: Final Output ----
# Print a final message, result, or summary to the user.

print("----------------------------")
print("Thanks for using my program!")
