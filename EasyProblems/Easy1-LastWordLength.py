def lengthOfLastWord(s):
    wordList = s.split()
    lastWord = wordList[-1]
    return len(lastWord)

s = "Hello World"
result = lengthOfLastWord(s)
print(result)

