#Example 1: only spaces 
text = "   "
print(text.isspace())  # Output: True

#Example 2: spaces and letters 
text = " Hello "
print(text.isspace())  # Output: False

#Example 3: new line and tab characters 
text = "\n\t  "  # Newline and tab characters
print(text.isspace())  # Output: True

#Example 4: empty string
text = ""
print(text.isspace())  # Output: False
