# Write a Python function that takes a list of words and returns the length of the longest one.

text = input("Please enter words: ")

long_str = 0

for word in text.split():
    if len(word) > long_str:
        long_str = len(word)
        long_word = word

print(f"The longest word is {long_word} with length", len(long_word))
