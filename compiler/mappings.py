import copy
import re
from random import randint, sample

import config


def write():
    intents = {}
    with open(config.DATASET_PATH, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            if line:
                entities, intent = line.split('>')
                sdn_rule = copy.deepcopy(config.MAPPINGS_SDN_RULE_TEMPLATE)

                intent = intent.replace('@id', sample(config.MAPPINGS_USERNAMES, 1)[0])

                origin = sample(config.MAPPINGS_LOCATIONS, 1)[0]
                if '@location' in intent:
                    sdn_rule['match']['src_ip'] = config.MAPPINGS_IPS[origin]
                    intent = intent.replace('@location', origin, 1)

                destination = sample(config.MAPPINGS_LOCATIONS, 1)[0]
                if '@location' in intent:
                    sdn_rule['match']['dst_ip'] = config.MAPPINGS_IPS[destination]
                    intent = intent.replace('@location', destination, 1)

                if '@target' in intent:
                    for i in range(intent.count('@target')):
                        intent = intent.replace('@target', sample(config.MAPPINGS_TARGETS, 1)[0], 1)

                if '@middlebox' in intent:
                    for i in range(intent.count('@middlebox')):
                        mb = sample(config.MAPPINGS_MIDDLEBOXES, 1)[0]
                        sdn_rule['action']['port'] = config.MAPPINGS_PORT[mb]
                        intent = intent.replace('@middlebox', mb, 1)

                if '@qos_metric' in intent:
                    for i in range(intent.count('@qos_metric')):
                        qos_metric = sample(config.MAPPINGS_QOS_METRICS, 1)[0]
                        qos_constraint = sample(config.MAPPINGS_QOS_CONSTRAINTS, 1)[0]
                        while '@qos_value' in intent and qos_constraint == 'none':
                            qos_constraint = sample(config.MAPPINGS_QOS_CONSTRAINTS, 1)[0]

                        if '@qos_value' not in intent:
                            qos_constraint = 'none'

                        intent = intent.replace('@qos_metric', qos_metric[0], 1)
                        intent = intent.replace('@qos_constraint', qos_constraint, 1)
                        intent = intent.replace('@qos_value', str(randint(1, 100)), 1)

                intent = intent.replace('@hour', sample(config.MAPPINGS_HOURS, 1)[0])
                intent = intent.replace('@hour', sample(config.MAPPINGS_HOURS, 1)[0])

                if 'allow traffic(\'@traffic\')' in intent:
                    allow = sample(config.MAPPINGS_TRAFFIC, 1)[0]
                    sdn_rule['match']['protocol'] = config.MAPPINGS_TRAFFIC_PROTOCOL[allow]
                    intent = intent.replace('@traffic', allow, 1)

                if 'block traffic(\'@traffic\')' in intent:
                    block = sample(config.MAPPINGS_TRAFFIC, 1)[0]
                    sdn_rule['match']['protocol'] = config.MAPPINGS_TRAFFIC_PROTOCOL[block]
                    sdn_rule['action']['output'] = 'drop'
                    sdn_rule['action']['port'] = '*'
                    intent = intent.replace('@traffic', block, 1)

                intents[intent] = sdn_rule

    with open(config.MAPPINGS_PATH, 'wb') as file:
        for intent, rule in intents.items():
            rule_str = ''
            for i, (k, v) in enumerate(rule.items()):
                rule_str += '{0}: {1}'.format(k, v)
                rule_str += ', ' if i + 1 != len(rule.items()) else ''

            file.write((intent.split("Intent:")[1]).strip() + ' > { ' + rule_str + ' }\n')


def read():
    mappings = {}
    with open(config.MAPPINGS_PATH, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            if line:
                intent, rule = line.split('>')
                intent = re.sub(' +', ' ', intent).strip()
                mappings[intent] = rule.strip()

    return mappings


if __name__ == '__main__':
    write()
