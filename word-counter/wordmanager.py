
# Get the list of words in a file
#Example: ["Hello", "World"]
def getwords(file, lower=False):
    words = []
    with open(file, "r") as f:
        for line in f:
            for word in line.split():
                if lower:
                    words.append(word.lower())
                else:
                    words.append(word)

    return words


# Get the words and the number of those words in a file
#Example: {"Hello": 1, "World": 1}
def getdict(words):
    wordsdict = {}
    for word in words:
        if word in wordsdict:
            wordsdict[word] += 1
        else:
            wordsdict[word] = 1
    return wordsdict


# Stackoverflow magic to sort the dictionary by the value of the keys
# Example
# from {hey":2, "the":7, "my":5}
# to   {"the":7, "my":5, "hey":2}
def sortdict(wordsdict, reverse=False):
    sorteddict = {k: v for k, v in sorted(
        wordsdict.items(), key=lambda item: item[1], reverse=reverse)}
    return sorteddict
