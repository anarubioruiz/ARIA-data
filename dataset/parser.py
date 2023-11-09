#!/usr/bin/python3

import json

from lighting_cases import cases


file_name = 'data/ARIA_dataset'
text_intro = '''\
I am ARIA, an Automation Rules Intelligence Assistant capable of creating Home Assistant rules for a particular IoT deployment.

From a description of an IoT scenario, along with the goal that the automation rules should achieve and the specific entity of interest, the target, I'll generate the rules for you. Let's start!
'''


def prepare_data():
    for case in cases:
        scenario = case['scenario']
        goal = case['goal']
        target = case['target']
        rules = case['rules']

        case['text'] = f'''\
{text_intro}

### IoT DEPLOYMENT
{scenario}

### GOAL
{goal}

### TARGET
{target}

### RULES
According to the IoT DEPLOYMENT described, the Home Assistant automation rules that accomplish the GOAL for the TARGET are:

```yaml
{rules}
```
'''


def write_jsonl():
    with open(file_name + '.jsonl', 'w') as f:
        for case in cases:
            f.write(json.dumps(case) + '\n')


def write_json():
    with open(file_name + '.json', 'w') as f:
        json.dump(cases, f, indent=2)


prepare_data()
write_jsonl()
write_json()

print(f'Done! {len(cases)} cases')
print(f'Check data/{file_name}.<jsonl/json>')
