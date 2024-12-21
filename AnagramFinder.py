"""
Anagram Finder starter code:
Written by my CS teacher
"""

#you may need to change this if you put the text file in a different folder or name it something else
DICT_FILE_PATH = "../../Libraries/dictionary.txt"

'''
Combine the two lists into one list and return that new list
Example: if list1 = ["a", "b", "c"] and list2 = ["d", "e", "f"], this procedure returns ["a", "b", "c", "d", "e", "f"]
'''
def combineLists(list1, list2):
    combinedList = []
    for i in range(len(list1)):
        combinedList.append(list1[i])
    for j in range(len(list2)):
        combinedList.append(list2[j])
    return combinedList

'''
Removes the duplicates from the list of words. You do not need to return anything. Instead, modify 'words' so that it no longer has duplicates.
Example: if words = ["cat", "cat", "dog", "elephant" , "dog"] then it would modify the list to be ["cat", "dog", "elephant"]
'''
def removeDuplicates(words):
    toRemove = []
    for i in range(len(words)-1):
        for j in range(len(words)-1):
            skip = False
            for m in range(len(toRemove)):
                if toRemove[m] == j:
                    skip = True
                    break
            if i >= j or skip:
                continue
            elif words[i] == words[j]:
                toRemove.append(j)
    toRemove.reverse()
    for i in range(len(toRemove)-1):
        words.pop(toRemove[i])
        print(words, toRemove)


'''
Insert letter at given index and returns the new word. 
Example: insertLetter("cap", "m", 2) returns "camp"
insertLetter("fame", "r", 1) returns "frame"
'''
def insertLetter(word, letter, i):
    insertLetterWord = word[:i] + letter + word[i:]
    return insertLetterWord

'''
Removes the letter at the index given by i.
Returns the word without the letter and returns the letter
Example: removeLetter("python", 3) returns a tuple of 2 values: ("pyton", "h")
'''
def removeLetter(word, i):
    removedLetter = word[i]
    removeLetterWord = word[:i] + word[i + 1:]
    return removeLetterWord, removedLetter # the word AND the letter

'''
Swap letters at index 1 and index 2 in word. Return the word with the letters swapped.
Example: swapLetters("bat", 0, 2) returns "tab"
Example: swapLetters("what", 0, 3) returns "thaw"
'''
def swapLetters(word, index1, index2):
    swapLetterWord = word[:index1] + word[index2] + word[index1 + 1:index2] + word[index1]
    return swapLetterWord


'''
Return a new list of words that appear in both list1 and list2. 
Example: list1 = ["cat", "dog", "frog"] and list2 = ["frog", "dog", "giraffe"], then it returns ["dog", "frog"]
'''
def similarWords(list1, list2):
    simWords = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                simWords.append(list1[i])
    return simWords




################################### Don't Modify Code Below This Line #################################


'''
Returns a list of words from a text file
You do not need to edit this procedure.
'''
def readWordsFromFile(fileName):    
    file = open(fileName, "r")
    words = []
    word = file.readline()
    while word != '':
        words.append(word.lower())
        word = file.readline().strip()
    return words


'''
This procedure will return a list of all the letter arrangements for a given word. It relies on the completion of the other procedures.
You do not need to edit this procedure.
'''
def getArrangements(word):
    possibleWords = []
    if len(word) == 1:
        return [word]
    elif len(word) == 2:
        return [word, swapLetters(word, 0, 1)]
    else:
        for i in range(len(word)):
            tinyWord, letter = removeLetter(word, i) #removes letter at i
            tinyList = getArrangements(tinyWord)
            for j in range(len(tinyList)):
                tinyList[j] = insertLetter(tinyList[j], letter, 0)
            possibleWords = combineLists(possibleWords, tinyList)
            removeDuplicates(possibleWords)
        return possibleWords

'''
An anagram solver for the typed in word.
You do not need to edit this procedure.
'''
def main():
    dictionary = readWordsFromFile(DICT_FILE_PATH) 
    word = ""
    while word != 'q':
        word = input("Please enter a word (all lowercase): ('q' to quit)")
        possibleAnagrams = getArrangements(word)
        print(similarWords(dictionary, possibleAnagrams)) # compare each arranged word to the dictionary to find if it is an anagram
       
if __name__ == "__main__":
    main()
