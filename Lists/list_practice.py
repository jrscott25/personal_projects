# Author: Ryan Summers
# Description: Some practice with lists here. Adding and removing from
# a list. As well as retrieving information and using f-strings.

invitees = ["ivan", "j-law", "florence", "jesus"]

print(f"\n")
for name in invitees:
    print(f"{name.title()}, would you like to join me for dinner?")

cantAttend = invitees.pop(0)

print(f"\n")
print(f"{cantAttend.title()} can't make it!")

invitees.insert(0, "floyd")

print(f"\n")
for name in invitees:
    print(f"{name.title()}, would you like to join me for dinner?")

print(f"\nWe found a bigger table!")
invitees.insert(0, "brooke")
invitees.insert(-1, "charles")
print(invitees.insert(3, "rocket"))

print(f"\n")
for name in invitees:
    print(f"{name.title()}, would you like to join me for dinner?")

print(f"\nOh snapsies, we don't have enough room. Removing some guests")

inviteesToRemove = ['Jesus', 'Charles', 'Rocket', 'Brooke']

print(f'\n')
for name in inviteesToRemove:
    print(f"{name.title()}, I'm sorry but I have to uninvite you to dinner.")
    invitees.remove(name.lower())

print(f"\n")
for name in invitees:
    print(f"{name.title()}, would you like to join me for dinner?")

print(f"\nI will end up inviting {len(invitees)} people.")

del invitees[0]
del invitees[0]
del invitees[0]

print(f"Remaining invitees: {invitees}")