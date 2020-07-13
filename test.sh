#!/bin/bash

ryu-manager mininet/simple_switch.py &
cd compiler
pipenv run python compiler.py > ../deploy_time
cd ../manager
pipenv run sudo python topology.py >> ../deploy_time
cd ..
sudo mn -c
