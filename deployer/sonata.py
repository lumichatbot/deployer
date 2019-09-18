""" SONATA-NFV Deployer """

import os
import subprocess
import datetime


def deploy(sonata_intent):
    try:
        script_name = 'res/scripts/{}_intent.sh'.format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S'))
        with open(script_name, 'w') as script:
            script.write(sonata_intent)
            os.chmod(script_name, 0o777)

        subprocess.check_call('./' + script_name, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as err:
        raise ValueError('Deployment of compiled intent failed. Error: {}'.format(err))
