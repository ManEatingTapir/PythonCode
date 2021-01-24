import sys

try:
    ini_string = ' '.join(sys.argv[1:])
except IndexError:
    print('Please provide a string for me to count!')
    exit()
    
# Set counter, assume we have at least one word if the string isn't length zero
word_count = 1
# Create list for words
words = []
for c in ini_string:
    # Only checks for spaces right now, possible idea: create delimiters list, check if c is in the list of delimiters.
    if (c == ' '):
        word_count = word_count + 1
        index = ini_string.find(c)
        words.append(ini_string[:index])
        # Delete the word from string via slicing from index + 1 (the next letter) to the end
        ini_string = ini_string[index + 1:]
        
# Clumsy solution to the fact that I can't get the last word due to only checking for spaces
words.append(ini_string)
print(word_count)
print(words)
