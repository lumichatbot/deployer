import os
import sys

ROOT_PATH = os.path.dirname(sys.modules['__main__'].__file__)
DATASET_PATH = os.path.join(ROOT_PATH, 'res/dataset.txt')
MAPPINGS_PATH = os.path.join(ROOT_PATH, 'res/mappings.txt')

MAPPINGS_SDN_RULE_TEMPLATE = {
    'match': {},
    'action': {
        'output': 'forward',
        'port': 'any'
    }
}

MAPPINGS_IPS = {
    'firewall': '143.54.12.2',
    'dpi': '143.54.12.3',
    'ids': '143.54.12.4',
    'load-balancer': '143.54.12.5',
    'parental-control': '143.54.12.6',
    'database': '143.54.12.7',
    'marketing': '143.54.12.8',
    'gateway': '143.54.12.9',
    'backend': '143.54.12.10',
    'ps4': '143.54.12.11',
    'asjacobs-pc': '143.54.12.12'
}

MAPPINGS_PORT = {
    'firewall': '0',
    'dpi': '1',
    'ids': '2',
    'load-balancer': '3',
    'parental-control': '4',
    'database': '5',
    'marketing': '6',
    'gateway': '7',
    'backend': '8',
    'ps4': '9',
    'asjacobs-pc': '10'
}

MAPPINGS_TRAFFIC_PROTOCOL = {
    'http': {
        'protocol': 'http',
        'port': '80'
    },
    'https': {
        'protocol': 'https',
        'port': '443'
    },
    'udp': {
        'protocol': 'udp',
        'port': '*'
    },
    'youtube': {
        'protocol': 'rtmp',
        'port': ['80', '1935']
    },
    'netflix': {
        'protocol': 'tcp',
        'port': ['22', '33001']
    }
}

MAPPINGS_HOURS = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                  '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
MAPPINGS_TARGETS = ['att', 'bell', 'ufrgs', 'pucrs', 'company', 'adp', 'example']
MAPPINGS_MIDDLEBOXES = ['firewall', 'dpi', 'ids', 'load-balancer', 'parental-control']
MAPPINGS_USERNAMES = ['asjacobs', 'granville', 'rjpfitscher', 'ronaldo']
MAPPINGS_LOCATIONS = ['database', 'marketing', 'gateway', 'backend', 'ps4', 'asjacobs-pc']
MAPPINGS_TRAFFIC = ['udp', 'http', 'netflix', 'youtube']
MAPPINGS_QOS_METRICS = [['latency', 'ms'], ['loss', '%'], ['jitter', 'ms'], ['throughput', 'mbps']]
MAPPINGS_QOS_CONSTRAINTS = ['less', 'less or equal', 'more', 'more or equal', 'equal', 'different', 'none']

NILE_OPERATIONS = ['add', 'from', 'to', 'with', 'allow', 'block', 'start', 'end']
NILE_FUNCTIONS = ['endpoint', 'client', 'middlebox', 'latency', 'bandwidth', 'jitter', 'loss', 'hour', 'date', 'traffic', 'flow']
NILE_KEYWORDS = ['define', 'intent'] + NILE_OPERATIONS
