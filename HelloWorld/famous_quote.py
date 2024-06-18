# Author: Ryan Summers
# Description: Just practice using f strings. The following program should print the quote and author.

quote = "Men are haunted by the vastness of eternity. And so we ask ourselves: will our actions echo across the " \
        "centuries? Will strangers hear our names long after we are gone, and wonder who we were, how bravely we " \
        "fought, how fiercely we loved?"

famous_person = "\twolfgang peterson           "

message = f"{famous_person.title()} once said, {quote}"

print(message)

famous_person = famous_person.lstrip()
famous_person = famous_person.rstrip()
famous_person = famous_person.strip()

message = f"{famous_person.title()} once said, {quote}"

print(f"\n{message}")
