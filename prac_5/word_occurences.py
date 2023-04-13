word_occurences = dict()
text = input('Text: ')
words = text.split()
for word in words:
    frequency = word_occurences.get(word, 0)
    try:
        word_occurences[word] += 1
    except KeyError:
        word_occurences[word] = 1

words = list(word_occurences.keys())
words.sort()

longest_word = max(len(word) for word in words)
for word in words:
    print(f'{word:{longest_word}} : {word_occurences[word]}')
