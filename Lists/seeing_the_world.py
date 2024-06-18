# Author: Ryan Summers
# Description: Working on ordering lists.

destinations = ['australia', 'india', 'brazil', 'dominican republic', 'sweden']

print(f"Original {destinations}")

print(f"Sorted {sorted(destinations)}")

print(f"Original {destinations}")

print(f"Sorted in reverse {sorted(destinations, reverse=True)}")

print(f"Original {destinations}")

destinations.reverse()
print(f"Reversed {destinations}")

destinations.reverse()
print(f"Reversed {destinations}")

destinations.sort()
print(f"Alphabetical {destinations}")

destinations.reverse()
print(f"Reverse alphabetical {destinations}")