
# My custom module
from wordmanager import *


# Print error
def error(e):
    print(f"ERROR {e}\n>> Try > help")


# Get args from a command
def getargs(text):
    return text.split()[1:]


# Check if the variable "words" exists if not print an error
def valid():
    if "words" in globals():
        return True
    else:
        print("You have to open a file first\n>> Try > openfile")
        return False


# Command loop
while True:
    # Get the command
    command = input("> ")
    # Get the args from the command
    args = getargs(command)

    try:
        # Get the command
        commandname = command.split()[0]

        # > openfile True
        # Open a file if True make the all words lower
        if commandname == "openfile":
            try:
                words = getdict(getwords(args[0]))
            except:
                print("That file does not exists at the current path of the script")

        # > sort min/max
        # Sort the dictionary
        if commandname == "sort" and valid():
            if args[0] == "max":
                reverse = True
            else:
                reverse = False
            try:
                if valid():
                    words = sortdict(words, reverse)
            except Exception as e:
                error(e)

        # > printraw
        # Print the raw dictionary
        if commandname == "printraw" and valid():
            print(words)

        # > pprint
        # Pretty Print the dictionary
        if commandname == "pprint" and valid():
            for word in words:
                print(f"{words[word]}   {word}")

        # > writeto example_wordlist.txt
        # Write the pretty printed results to a text file
        if commandname == "writeto" and valid():
            # Clear the file
            with open(args[0], "w") as f:
                f.write("")
            # Write to the file
            with open(args[0], "a") as f:
                for word in words:
                    f.write(f"{words[word]}   {word}\n")

        # > search example
        # Print the number of times a word was mentioned in the file
        if commandname == "search" and valid():
            number = 0
            try:
                number = words[args[0]]
            except:
                pass
            print(f"The word {args[0]} was mentioned {number} times.")

        # The > help command
        if commandname == "help":
            print(
                "Open a file if True then make the all words lower > openfile example.txt True")
            print("Sort the word count > sort min/max")
            print("Print the raw dictionary > printraw")
            print("Pretty Print the dictionary > pprint")
            print("Write to a file > writeto example_wordlist.txt")
            print("Search through the file > search example")

    # Print the error if there was any
    except Exception as e:
        error(e)
