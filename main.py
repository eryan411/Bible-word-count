import re

print("Hello! I'm programmed to look up words in the Bible and tell you how many times they appear!")

with open(r"Bible.txt") as fh:
    contents = fh.read()


def main():
    file = open(r'Bible.txt').read()
    Word = input("What word would you like me to search for? ")
    count = file.count(Word)

    print("The word" + str(Word) + "appears " + str(count) + " times!")


main()
