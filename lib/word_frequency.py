import string

def word_frequency(sentence):
    # Initialize an empty dictionary to store word frequencies
    word_freq = {}
    
    # Remove punctuation and convert the sentence to lowercase
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()
    
    # Iterate through the words in the sentence
    for word in words:
        # If the word is already in the dictionary, increment its frequency by 1
        if word in word_freq:
            word_freq[word] += 1
        # If the word is not in the dictionary, add it with a frequency of 1
        else:
            word_freq[word] = 1
    
    return word_freq

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
