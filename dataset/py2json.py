#!/usr/bin/python3

import json
import random
import lighting


def PaLM_data():
    data = []
    instruction = '''\
You are ARIA, an Automation Rules Intelligence Assistant capable of creating Home Assistant rules for a particular IoT deployment.

From a description of an IoT scenario, along with the goal that the automation rules should achieve and the specific entity of interest, the target, you'll generate the rules for me. Let's start!
'''

    for case in lighting.cases:
        entry = dict(case)
        entry['input_text'] = f'''\
{instruction}

-- The scenario is: {case['scenario']}

-- The goal is: {case['goal']}

-- The target is: {case['target']}
'''
        entry['output_text'] = entry['rules']
        data.append(entry)

    return data


def LLaMA_data():
    data = []

    for case in lighting.cases:
        entry = dict()
        entry['instruction'] = '''\
You are ARIA, an Automation Rules Intelligence Assistant capable of creating Home Assistant rules for a particular IoT deployment.
Below, the scenario description, the goal and the target of the automation rules to generate are provided as INPUT. Write the Home Assistant automation rules (YAML) for this INPUT as OUTPUT.'''

        entry['input'] = f'''\
-- The scenario is: {case['scenario']}

-- The goal is: {case['goal']}

-- The target is: {case['target']}'''

        entry['output'] = case['rules']
        entry['prompt'] = f'''\
### INSTRUCTION:
{entry['instruction']}

### INPUT:
{entry['input']}

### OUTPUT:
{entry['output']}
'''
        data.append(entry)
    return data


datasets = {
    'PaLM': PaLM_data,
    'LLaMA': LLaMA_data,
}


def write_jsonl(file_name, data):
    with open(file_name + '.jsonl', 'w') as f:
        for case in data:
            f.write(json.dumps(case) + '\n')


def write_json(file_name, data):
    with open(file_name + '.json', 'w') as f:
        json.dump(data, f, indent=2)


def divide_data(data):
    random.shuffle(data)
    test_data = data[:10]
    train_data = data[10:]
    return {'train': train_data, 'test': test_data}


def process_data(dataset_name):
    data = datasets[dataset_name]()
    data = divide_data(data)
    for key, value in data.items():
        write_jsonl(f'{dataset_name}_{key}', value)
        write_json(f'{dataset_name}_{key}', value)


process_data('PaLM')
process_data('LLaMA')

print(f'Done! {len(lighting.cases)-10} training cases (10 for testing)')
print(f'Check data/')
