""" Merlin deployer """

import os
import re
import time

from utils import config
import deployer.parser as merlin_parse


def deploy(merlin_intent):
    """ Magic """
    print "Merlin", merlin_intent
    start = time.time()

    working_dir = os.getcwd()

    with open(config.MERLIN_WORKKING_PATH + config.MERLIN_FILE_OUTPUT, 'w') as f:
        f.write(merlin_intent)

    os.chdir(config.MERLIN_WORKKING_PATH)
    full_topology_path = working_dir.split('/nile')[0] + config.TOPOLOGY_DOT_PATH[2:]
    full_output_path = working_dir.split('/nile')[0] + config.MERLIN_EXEC_OUTPUT[2:]
    command = './{} -topo {} {} -verbose >> {}'.format(config.MERLIN_EXEC, full_topology_path, config.MERLIN_FILE_OUTPUT, full_output_path)
    os.system(command)

    os.chdir(working_dir)

    with open(config.MERLIN_EXEC_OUTPUT) as f:
        output = f.read()
        if not re.search('(E|e)rror', output):
            merlin_parse.parse_merlin_output(config.MERLIN_EXEC_OUTPUT)
        else:
            raise 'Execution error!'

    os.remove(config.MERLIN_EXEC_OUTPUT)

    elapsed_time = time.time() - start
    return elapsed_time
