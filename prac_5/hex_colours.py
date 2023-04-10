COLOURS = {
    'Absolute Zero': '#0048ba',
    'Acid Green': '#b0bf1a',
    'Alice Blue': '#f0f8ff',
    'Alizarin Crimson': '#e32636',
    'Amaranth': '#e52b50',
    'Amber': '#ffbf00',
    'Amethyst': '#9966cc',
    'Antique White': '#faebd7',
    'Apricot': '#fbceb1',
    'Aqua': '#00ffff'
}

colour_name = input('Enter colour: ').title()
while colour_name != '':
    if colour_name in COLOURS:
        print(COLOURS[colour_name])
    else:
        print('Invalid colour!')
    colour_name = input('Enter colour: ').title()