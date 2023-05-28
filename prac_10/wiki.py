import wikipedia

try:
    prompt = input('Enter: ')
    while prompt != '':
        page = wikipedia.page(prompt, auto_suggest=False)
        print(page.title)
        print(wikipedia.summary(prompt, auto_suggest=False))
        print(page.url)
        prompt = input('Enter: ')
    print('Thank you!')
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)
