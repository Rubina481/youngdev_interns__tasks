# Program: Count word frequency using dictionary

text = input("Enter a text: ")

# Split text into words
words = text.split()

# Create an empty dictionary
word_freq = {}

# Count frequency of each word
for word in words:
    word = word.lower()  # make case-insensitive
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Display result
print("\nWord Frequency:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
