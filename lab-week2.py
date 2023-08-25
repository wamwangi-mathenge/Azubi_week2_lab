# Introduction
# Display a welcoming message to the user

print("Welcome to the Azubi Experience.\nKindly share your experience with us so far")
print()
# Store your story variables
# Gather user inputs
name = input("What is your name? ")
course = input("What course are you taking? ")
rating = input("How would you rate the first 2 weeks of your training on a scale of 1 to 5? ")
comment = input("What can Azubi do to improve your experience? ")

print()

# Story Generation
story = f"Hello, my name is {name}. I am pursuing {course} at Azubi Africa. On a scale of 1 to 5, I would give a rating of {rating} for my first 2 weeks of the training. To improve my experience in the program, I would suggest Azubi Africa to {comment}"
print(story)
print()