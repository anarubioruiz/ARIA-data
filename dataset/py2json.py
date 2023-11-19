#!/usr/bin/python3

import json
import random
import lighting


def PaLM_data():
    data = []
    text_intro = '''\
You are ARIA, an Automation Rules Intelligence Assistant capable of creating Home Assistant rules for a particular IoT deployment.

From a description of an IoT scenario, along with the goal that the automation rules should achieve and the specific entity of interest, the target, you'll generate the rules for me. Let's start!
'''

    for case in lighting.cases:
        entry = dict()
        entry['input_text'] = f'''\
{text_intro}

### IoT DEPLOYMENT:
{case['scenario']}

### GOAL:
{case['goal']}

### TARGET:
{case['target']}
'''
        entry['output_text'] = case['rules']
        data.append(entry)

    return data


def LLaMA_data():
    data = []
    text_intro = '''\
I am ARIA, an Automation Rules Intelligence Assistant capable of creating Home Assistant rules for a particular IoT deployment.
Below is the description of a scenario, the purpose of the automation rules, and the entity of interest, the target.
'''

    for case in lighting.cases:
        entry = dict(case)
        entry['text'] = f'''\
{text_intro}

### IoT DEPLOYMENT
{entry['scenario']}

### GOAL
{entry['goal']}

### TARGET
{entry['target']}

### RULES
According to the IoT DEPLOYMENT described, the Home Assistant automation rules (YAML) that accomplish the GOAL for the TARGET are:

{entry['rules']}
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
