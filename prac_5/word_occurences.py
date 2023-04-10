word_occurences = dict()
text = input('Text: ')
words = text.split()
longest_word = len(max(words, key=len))
for word in words:
    if word in word_occurences:
        word_occurences[word] += 1
    else:
        word_occurences[word] = 1

for word, count in word_occurences.items():
    print(f'{word:{longest_word}} : {count}')
