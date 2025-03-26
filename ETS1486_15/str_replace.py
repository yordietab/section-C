str.replace()

Description: The str.replace() method returns a copy of the string with all occurrences of a specified substring replaced with another substring.

Syntax:

string.replace(old, new, count)

    old: The substring to be replaced.
    new: The substring to replace with.
    count (optional): Maximum number of replacements.

Example:

text = "Hello, World!"
replaced_text = text.replace("World", "Python")
print(replaced_text)  # Output: "Hello, Python!"