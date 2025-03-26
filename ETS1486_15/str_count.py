str.count()

Description: The str.count() method returns the number of non-overlapping occurrences of a substring in a string.

Syntax:

string.count(sub, start, end)

    sub: The substring to search for.
    start (optional): The starting index.
    end (optional): The ending index.

Example:

text = "apple, banana, apple"
count = text.count("apple")
print(count)  # Output: 2