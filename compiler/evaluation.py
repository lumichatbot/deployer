""" evaluation model for Nile compiler """
import time
import csv

import compiler
from deployer import merlin

from utils import dataset, config


def run():
    """ open dataset and runs tests """
    intents = dataset.read('compilation', '')

    # for (uni, intents) in intents.items():
    results = []

    for intent in intents:
        start = time.time()
        compiled, compilation_time = compiler.compile(intent['nile'])
        deployment_time = merlin.deploy(compiled)
        total = time.time() - start
        results.append((intent['type'], compilation_time, deployment_time, total))

    with open(config.COMPILATION_RESULTS_PATH, 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(['type', 'compilation time', 'deployment time', 'total time'])
        for (mtype, compilation_time, deployment_time, total) in results:
            csv_writer.writerow([mtype, compilation_time, deployment_time, total])


if __name__ == "__main__":
    run()
