#**str.lower()**

The str.lower() method is used to convert all the uppercase characters in a string to lowercase. It doesn't modify the original string but instead returns a new string with all characters in lowercase.

#**str.upper()**

str.upper() method converts all the lowercase characters in a string to uppercase. Like str.lower(), it doesn't modify the original string but returns a new one with all characters in uppercase.

#**str.title()**

The str.title() method converts the first character of each word in a string to uppercase and all other characters to lowercase. It's useful for formatting text into title case. Like other string methods, it doesn't modify the original string but returns a new one.

#**str.capitalize()**

is a string method that returns a new string with the first character capitalized and the rest of the characters converted to lowercase.

#**str.swapcase()**

is a string method that returns a new string with all uppercase letters converted to lowercase and all lowercase letters converted to uppercase.

#**str.find()**

is a string method used to locate the position (index) of a substring within a string. If the substring is found, it returns the index of its first occurrence; otherwise, it returns -1.

#**str.index()**

is a string method that finds the first occurrence of a specified substring within a string. It works similarly to str.find(), but the key difference is that if the substring is not found, str.index() raises a ValueError, whereas str.find() returns -1.

#**str.startswith()**

is a string method that checks if a string starts with a specified prefix. It returns True if the string starts with the given substring and False otherwise.

#**str.endswith()**

is a string method that checks if a string ends with a specified suffix. It returns True if the string ends with the given substring and False otherwise.

#**str.count()**

 Returns the count of non-overlapping occurrences of a substring.

#**str.replace()**

 Returns a copy of the string with occurrences of a substring replaced.

#**str.strip()**

 Returns a copy of the string with leading and trailing whitespace removed.

#**str.islower()**

is a type of string method which that acts as a boolean and returns true if all the text are lowercase and false if it is uppercase

#**str.isupper()**

is a type of string method which returns true if all the text are in upper case and false if it is lowercase

#**str.encode()** 

is a method used to convert a string (which is in Unicode by default) into a bytes object using a specified encoding. This is useful when working with files, network communication, or encryption, where text needs to be represented as bytes.

#**str.lstrip()**

 method in Python is used to remove leading whitespace (spaces, tabs, newlines, etc.) from a string. It returns a new string with the leading characters removed.
**syntax: str.lstrip([chars])**

**chars (optional)**: A string specifying the set of characters to remove from the left side of the string. If not provided, it removes leading whitespace characters by default (spaces, tabs, newlines).

#**str.rstrip()**

 method in Python is used to remove trailing whitespace (spaces, tabs, newlines, etc.) from the right end of a string. It returns a new string with the trailing characters removed.

**syntax: str.rstrip([chars])**

chars (optional): A string specifying the set of characters to remove from the right side of the string. If not provided, it removes trailing whitespace characters by default (spaces, tabs, newlines).

#**str.split()**

 method in Python is used to split a string into a list of substrings based on a specified delimiter. By default, it splits by whitespace characters (spaces, tabs, newlines), but you can specify a custom delimiter if needed.

**syntax : str.split(separator=None, maxsplit=-1)**

**separator (optional)**: The delimiter or separator string. The string will be split wherever this separator occurs. If None (or not provided), it will split by any whitespace (spaces, tabs, newlines).

**maxsplit (optional)**: The maximum number of splits to do. The default value of -1 means "no limit," i.e., it will split as many times as possible.

#**str.join()**

 method in Python is used to join elements of an iterable (like a list or tuple) into a single string, using the given string as a separator between elements.

**syntax**: separator.join(iterable)

**separator** – The string placed between each element of the iterable.

**iterable** – A list, tuple, set, or any iterable containing strings.

#**str.isalpha()** 

method in Python checks whether a string contains only alphabetic characters (A-Z or a-z). It returns:

True → if all characters are letters and the string is not empty.

False → if the string contains numbers, spaces, or special characters, or if it is empty.**syntax:string.isalpha()**. No parameters are needed.

Works only with letters (no spaces, digits, or symbols).

#**str.isdigit()** 

method in Python checks if a string contains only numeric digits (0-9). It returns:

True → if all characters in the string are digits and the string is not empty.

False → if the string contains letters, spaces, symbols, or is empty.**syntax: string.isdigit()**

No parameters needed.

Works only for digits (0-9).

#**str.isalnum()**

 method in Python checks if a string contains only alphanumeric characters (letters A-Z, a-z and digits 0-9) and is not empty.

It returns:

True → if all characters are letters and/or numbers.

False → if the string contains spaces, special characters, or is empty.

#**str.isspace()**

 method in Python checks if a string contains only whitespace characters (such as spaces, tabs, and newlines) and is not empty.

It returns:

True → if the string contains only whitespace.

False → if the string has any non-whitespace characters or is empty.

#**str.format()**

 method in Python is used to format strings by inserting values into placeholders {} within a string. This makes it easier to create dynamic and readable output.

**syntax: string.format(value1, value2, ...)**

{} → Acts as a placeholder in the string.

format(value1, value2, ...) → Inserts values into the placeholders.