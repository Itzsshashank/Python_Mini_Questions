def word_frequency_counter(sentence):
    words = sentence.split()

    word_freq = {}

    for word in words:
        # Removing punctuation and converting it to lowercase for consistency
        word = word.strip('.,!?')
        word = word.lower()

        # Checking if word is already in dictionary
        if word in word_freq:
            # If it exists, increment the frequency count
            word_freq[word] += 1
        else:
            # If a new word then add it to dictionary
            word_freq[word] = 1

    return word_freq

# Example
sentence = "He Said 'he likes python Programming' or Python is what he likes"
result = word_frequency_counter(sentence)
print(result)

# Output
# {'he': 2, 'said': 1, "'he": 1, 'likes': 2, 'python': 2, "programming'": 1, 'or': 1, 'is': 1, 'what': 1}
