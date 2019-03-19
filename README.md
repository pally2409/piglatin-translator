# Pig Latin Translator
A Pig Latin translator coded in Python

## Introduction 
Pig Latin alters English words by adding a suffix according to the beginning character/characters of the word.

## Rules
### 1. Vowels
For words starting with a vowel, add 'yay' to the end of the word. For eg. the word *and* becomes *andyay*.

### 2. Consonant
For words starting with a consonant or a consonant cluster, the consosnant or consonant cluster is moved to the end of the word and 'ay' is added. For eg. the word *simple* becomes *implesay* and the word *crows* becomes *owscray*.

### 3. Exceptions
Y is considered as a vowel if it's part of a consonant cluster. For eg. the word *rhythm* becomes *ythmrhay* but the word *yellow* is *ellowyay*

## Features 
1. Retains the punctuation of the word.
2. Capitalises the beginning of sentence.
3. Can handle upper case and lower case words.
4. Retains capitalisation of fully capital words (eg. *CAPITAL* becomes *APITALCAY*) or words starting with a capital vowel (eg. *And* becomes *Andyay*).

## Sample
