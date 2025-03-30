name = "Alice"
age = 25
text = "My name is {} and I am {} years old.".format(name, age)
print(text)


#output: My name is Alice and I am 25 years old.

#Also using positional indexes
text = "I love {1} more than {0}.".format("tea", "coffee")
print(text)
#output: I love coffee more than tea.
