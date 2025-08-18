import json
from pathlib import path





def read_json(file):
    with open(file, 'r') as f:
        data = json.load(f)
        return data
    


def write_json(data, file):
    with open(file, 'w') as f:
       json.dumps(data, f, indent=4)


data = read_json(Path('./data/pardaz.json'))
data['messages'] = data['messages'][:10000]
write_json(data, Path('./data/pardaz-short.json'))