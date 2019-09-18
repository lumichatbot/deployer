#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net import Mininet, CLI
from mininet.node import OVSSwitch, RemoteController
from mininet.link import TCLink
from mininet.log import output, warn
from mininet.term import makeTerm
from random import randint
import json
import sys
import time
import os
import re
import pwd

sys.path.append('..')
from utils import config

TIMEOUT=5

HOST_REGEX='\sh[0-9]+\[type=host'
SWITCH_REGEX='\ss[0-9]+\[type=switch'
LINK_REGEX='\s(h|s)[0-9]+ -> (h|s)[0-9]+'

class DotTopo(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)
        self.dot_nodes = {}
        self.dot_links = []

    def add_host(self, line):
        host = self.parse_line(line)
        self.dot_nodes[host['name']] = self.addHost(host['name'], mac=host['mac'], ip=host['ip'])

    def add_switch(self, line):
        switch = self.parse_line(line)
        self.dot_nodes[switch['name']] = self.addSwitch(switch['name'], dpid=switch['id'])

    def add_link(self, line):
        tokens = self.parse_line(line)
        nodes = tuple(filter(None, re.split('[\-> ]',tokens['name'])))
        for link in self.dot_links:
            n1, n2 = link
            if n1 == nodes[1] and n2 == nodes[0]:
                return
        self.dot_links.append(nodes)

    def parse_line(self, line):
        result = {}
        tokens = list(filter(None, re.split('[\[\],;]',line.strip())))
        result['name'] = tokens[0]
        for token in tokens[1:]:
            key, value = token.split('=')
            result[key] = value.strip('\"')
        return result

    def import_dot(self, fname):
        f = open(fname)
        matches = {
            'host':HOST_REGEX,
            'switch':SWITCH_REGEX,
            'link':LINK_REGEX
        }
        for l in f:
            for m in matches:
                pattern = re.compile(matches[m])
                if pattern.match(l):
                    if m == 'host':
                        self.add_host(l)
                    elif m == 'switch':
                        self.add_switch(l)
                    elif m == 'link':
                        self.add_link(l)

        for link in self.dot_links:
            n1, n2 = link
            self.addLink(n1, n2)

def start_mininet():
    controller = RemoteController('c0', ip='127.0.0.1', port=6633)

    topo=DotTopo()
    topo.import_dot('../res/topology.dot')

    net = Mininet(topo=topo, controller=controller, link=TCLink)
   
    controller.start()
    net.start()

    # while True:
    random_host1 = net.get('h%d'%randint(1,160))
    random_host2 = net.get('h%d'%randint(1,160))

    makeTerm(random_host1, title='Iperf Server', cmd='iperf -s')
    makeTerm(random_host2, title='Iperf Client', cmd='iperf -c '+random_host1.IP())

    file = open(config.TC_COMMANDS_PATH)

    start_time = time.time()
    rules_tc = json.loads(file.read())
    for rule_ip in rules_tc:
        print(rule_ip)
        for i in range(1,160):
            host = net.get('h{}'.format(i))
            if host.IP() == rule_ip:
                print(rule_ip)
                break
        for rule in rules_tc:
            makeTerm(host, title='Commands', cmd=rule)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


if __name__ == '__main__':
    deploy_time = start_mininet()
    print("Deploy time: ", deploy_time)
