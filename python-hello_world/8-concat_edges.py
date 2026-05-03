#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# Extract "object-oriented programming", "with", and "Python"
str = str[39:67] + str[107:112] + str[:6]
print(str)
