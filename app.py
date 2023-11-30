course = 'Python for Beginners'
print(course.upper())
# This does not change the string, it returns a new string, it returns a new string
print(course)  # This will just print the old string without the upper case method
print(course.lower())  # Same thing again, prints string in lower, does not change the value
print(course.find('y'))  # This will return the index of the first y, counting starts with 0
print(course.find('Y'))  # This will not work, Python is case-sensitive and hence will return a -1
print(course.replace('for', '4'))  # This will replace for with 4, just for the output,
# if you enter something that is not in the text, it will just return the unchanged text
print(course)  # This is still the original string "Python for beginners"
print(course.find('Python'))
print('Python' in course)  # Returns Boolean for whether the word is in the string
