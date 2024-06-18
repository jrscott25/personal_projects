# Author: Ryan Summers
# Description: Practicing formatting strings. Should print a few variations of the 'name' variable.

name = "Ryan"

message = f"Hello {name}, would you like to learn some Python today? \nLowercase: {name.lower()} " \
          f"\nUppercase: {name.upper()} \nTitlecase: {name.title()}"

print(message)