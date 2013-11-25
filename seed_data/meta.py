import json

final_data = {}

with file('data/all_cards.json') as cards_file:
    colors = set()
    types = set()
    subtypes = set()

    cards = json.loads(cards_file.read())

    for name, data in cards.iteritems():
        [colors.add(c) for c in data.get('colors')]
        [types.add(t) for t in data.get('types')]
        [subtypes.add(st) for st in data.get('subtypes', [])]

    final_data['colors'] = list(colors)
    final_data['types'] = list(types)
    final_data['subtypes'] = list(subtypes)

meta_file = file('data/meta.json', 'w')
meta_file.writelines(json.dumps(final_data))
meta_file.close()

