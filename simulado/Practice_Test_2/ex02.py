# Analyze the following code and then answer Yes for the statements that are true and No for the statements that are false.

a = float(input("Enter a number. "))

b = float(input("Enter a number to divide by. "))

"""
1) The finally statement will run regardless of which pieces of code above it run.
2) Both the try and except parts will run if a = 0 and b != 0.
3) The else part will run if a = 0 and b != 0.
"""

try:

   print (f"The answer is {a/b}.")

except:

   print("This did not work. Did you try to divide by zero?")

else:

   print("You successfully divided two numbers.")

finally:

   print("Thank you for playing.")