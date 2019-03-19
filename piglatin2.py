from string import punctuation

def encodeWords(word, wordLen, succAdd, rangeStart, consWord, prevWord): #Actual encoding of the word takes place here
    revPunctCounter = 0
    for c in reversed(word):
        if c in punctuation:
            revPunctCounter = revPunctCounter + 1
    if word[wordLen-1] in punctuation: #Checking if the word ends with a punctuation
        encodedWord = word[rangeStart:(wordLen-revPunctCounter)] + consWord + succAdd + word[(wordLen-revPunctCounter):]
    else:
        encodedWord = (word[rangeStart:(wordLen)] + consWord + succAdd)
    if prevWord.endswith(".") or not prevWord:
        print prevWord
        encodedWord = encodedWord[0].upper() + encodedWord[1:len(encodedWord)]
    encodedWords.append(encodedWord)

def setValues(V): #Set values of the variables in encoding function
    if V == 0: #If the first letter is a vowel
        succAdd = 'yay' #The successor to add is yay
        rangeStart = 0 #The entire word is copied as it is so the copying starts from 0
        consWord = '' #The first character of the word is not copied to the end unlike in consonants so empty
    else:
        succAdd = 'ay' #The successor to add is ay
        consWord = word[0:counter] #The consonant sequence is placed at the end along with the successor
        rangeStart = counter #The word is kept as it is except the consonant sequence, hence, the copying starts from when the consonant ends
    return succAdd, rangeStart, consWord

words = []
encodedWords = []
fileName = raw_input("Enter the name of the file to translate (with the file extension):")
with open(fileName,'r') as f:
    for line in f:
        for word in line.split():
            words.append(word)
vowels = ["a","e","i","o","u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
prevWord = ''

for word in words:
    wordLen = len(word)
    counter = 0 #This is to find the number of consonants in sequence in beginning of a word
    word = word.lower()
    if word[0] in vowels:
        V = 0
        succAdd, rangeStart, consWord = setValues(V)
        encodeWords(word, wordLen, succAdd, rangeStart, consWord, prevWord)
    elif word[0] in consonants:
        succAdd = 'ay'
        V = 1
        for c in word:
            if c not in vowels:
                counter = counter+1
            else:
                break
        succAdd, rangeStart, consWord = setValues(V)
        encodeWords(word, wordLen, succAdd, rangeStart, consWord, prevWord)
    else:
        if (word[0] in punctuation and wordLen == 1) or word[0].isdigit() == True: #If there is a standalone punctuation or a number
            encodedWords.append(word)
        else: #If there is a word starting with a punctuation
            if word[1] in vowels:
                c = list(word)
                c[0], c[1] = c[1], c[0]
                word = "".join(c)
                succAdd, rangeStart, consWord = setValues(V)
                encodeWords(word, wordLen, succAdd, rangeStart, consWord, prevWord)
            else:
                V = 1
                for c in word:
                    if c in vowels or (c == 'y' and word[0]!='y'):
                        break;
                    else:
                        counter = counter+1
                temp1 = word[1:counter]
                temp2 = word[0]
                temp3 = word[counter:wordLen]
                word = temp1 + temp2 + temp3
                counter = counter - 1
                succAdd, rangeStart, consWord = setValues(V)
                encodeWords(word, wordLen, succAdd, rangeStart, consWord, prevWord)
    prevWord = word

print(" ".join(encodedWords))



