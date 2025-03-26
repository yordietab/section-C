str.strip()

Description: The str.strip() method returns a copy of the string with leading and trailing whitespace removed.

Syntax:

string.strip([chars])

    chars (optional): A string specifying the set of characters to be removed. If omitted, whitespace is removed.

Example:

text = "  Hello, World!  "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"