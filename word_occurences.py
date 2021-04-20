sentence = input("Enter Text: ")
word_counter = {}
words = sentence.split()
for word in words:
    frequency = word_counter.get(word, 0)
    word_counter[word] = frequency + 1
words = list(word_counter.keys())
words.sort()
max_word_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{word_counter[word]}} : {max_word_length}")