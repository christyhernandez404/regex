# Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.
import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken",
         "Jordan Alexander Williams", "Madonna", "programming is cool"]
# first name             last name      middle name
pattern = r"^[A-Z][a-z]* [A-Z][a-z]*( [A-Z][a-z]*)*$"


def solution(alist):
    for name in names:
        if re.match(pattern, name):
            print(name)
        else:
            print("Invalid name")


solution(names)
