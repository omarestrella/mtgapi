import json

supported_sets = ['DGM', 'GTC', 'M14', 'RTR', 'THS']
final_data = {}
all_card_data = {}

for set_name in supported_sets:
    with file('json/%s.json' % set_name) as set_file:
        raw_file = set_file.read()
        data = json.loads(raw_file)
        cards = data.get('cards')
        for card in cards:
            name = card.get('name')
            card['set'] = set_name
            final_data[name] = card
            all_card_data[name] = card
        output_file = file('data/cards/%s.json' % set_name, 'w')
        output_file.writelines(json.dumps(final_data))
        output_file.close()

all_card_file = file('data/all_cards.json', 'w')
all_card_file.writelines(json.dumps(all_card_data))
all_card_file.close()
