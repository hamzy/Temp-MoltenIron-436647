#!/usr/bin/env python

"""
Tests the addBMNode MoltenIron command.
"""

# Copyright (c) 2016 IBM Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable-msg=C0103

from __future__ import print_function

import sys
import os
import yaml
import argparse
from molteniron import moltenirond

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Molteniron CLI tool")
    parser.add_argument("-c",
                        "--conf-dir",
                        action="store",
                        type=str,
                        dest="conf_dir",
                        help="The directory where configuration is stored")

    args = parser.parse_args(sys.argv[1:])

    if args.conf_dir:
        if not os.path.isdir(args.conf_dir):
            msg = "Error: %s is not a valid directory" % (args.conf_dir, )
            print(msg, file=sys.stderr)
            sys.exit(1)

        yaml_file = os.path.realpath("%s/conf.yaml" % (args.conf_dir, ))
    else:
        yaml_file = "/usr/local/etc/molteniron/conf.yaml"

    with open(yaml_file, "r") as fobj:
        conf = yaml.load(fobj)

    node1 = {
        "name": "pkvmci816",
        "ipmi_ip": "10.228.219.134",
        "ipmi_user": "user",
        "ipmi_password": "2f024600fc5ef6f7",
        "port_hwaddr": "97: c3:b0: 47:0c:0d",
        "cpu_arch": "ppc64el",
        "cpus": 20,
        "ram_mb": 51000,
        "disk_gb": 500,
        "status": "ready",
        "provisioned": "",
        "timestamp": "",
        "allocation_pool": "10.228.112.10,10.228.112.11"
    }
    node2 = {
        "name": "pkvmci818",
        "ipmi_ip": "10.228.219.133",
        "ipmi_user": "user",
        "ipmi_password": "6cf0957c985b2deb",
        "port_hwaddr": "2d: 9e:3c:83:8a: be",
        "cpu_arch": "ppc64el",
        "cpus": 20,
        "ram_mb": 51000,
        "disk_gb": 500,
        "status": "ready",
        "provisioned": "",
        "timestamp": "",
        "allocation_pool": "10.228.112.8,10.228.112.9"
    }
    node3 = {
        "name": "pkvmci851",
        "ipmi_ip": "10.228.118.129",
        "ipmi_user": "user",
        "ipmi_password": "cc777c10196db585",
        "port_hwaddr": "47: b0:dc:d5: 82:d9",
        "cpu_arch": "ppc64el",
        "cpus": 20,
        "ram_mb": 51000,
        "disk_gb": 500,
        "status": "used",
        "provisioned": "7a72eccd-3153-4d08-9848-c6d3b1f18f9f",
        "timestamp": "1460489832",
        "allocation_pool": "10.228.112.12,10.228.112.13"
    }
    node4 = {
        "name": "pkvmci853",
        "ipmi_ip": "10.228.118.133",
        "ipmi_user": "user",
        "ipmi_password": "a700a2d789075276",
        "port_hwaddr": "44: 94:1a: c7:8a:9f",
        "cpu_arch": "ppc64el",
        "cpus": 20,
        "ram_mb": 51000,
        "disk_gb": 500,
        "status": "used",
        "provisioned": "6b8823ef-3e14-4811-98b9-32e27397540d",
        "timestamp": "1460491566",
        "allocation_pool": "10.228.112.14,10.228.112.15"
    }

    # 8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----
    database = moltenirond.DataBase(conf, moltenirond.TYPE_SQLITE_MEMORY)
    ret = database.addBMNode(node1)
    print(ret)
    assert ret == {'status': 200}
    ret = database.addBMNode(node1)
    print(ret)
    assert ret['status'] == 400
    assert ret['message'] == "Node already exists"
    ret = database.addBMNode(node2)
    print(ret)
    assert ret == {'status': 200}
    ret = database.addBMNode(node2)
    print(ret)
    assert ret['status'] == 400
    assert ret['message'] == "Node already exists"
    ret = database.addBMNode(node3)
    print(ret)
    assert ret == {'status': 200}
    ret = database.addBMNode(node3)
    print(ret)
    assert ret['status'] == 400
    assert ret['message'] == "Node already exists"

    database.close()
    del database
