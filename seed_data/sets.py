import json

supported_sets = ['DGM', 'GTC', 'M14', 'RTR', 'THS']
final_data = {
    'sets': []
}

for s in supported_sets:
    with file('cards/%s.json' % s) as set_file:
        raw_file = set_file.read()
        data = json.loads(raw_file)
        name, code, date, block = data.get('name'), data.get('code'), data.get('releaseDate'), data.get('block')
        final_data['sets'].append({
            'name': name,
            'code': code,
            'release_date': date,
            'block': block
        })
        output_file = file('data/sets.json', 'w')
        output_file.writelines(json.dumps(final_data))
        output_file.close()
