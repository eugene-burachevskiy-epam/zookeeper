#!/usr/bin/python3

import argparse, datetime
from argparse import RawDescriptionHelpFormatter
from kazoo.client import KazooClient
import kazoo.exceptions

parser = argparse.ArgumentParser(description='Zookeeper write client.\nWrites data to item (UTF-8 bytecode format). If item not exists creates new one with all parent path', formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('item', action="store", help='/path/to/item')
parser.add_argument('data', action="store", help='data to store')
args = parser.parse_args()

fmt = '%Y-%m-%d %H:%M:%S'

zookeeper = {
    'server':'127.0.0.1',
    'port':'2181'    
}

zk = KazooClient(hosts='%(server)s:%(port)s' % zookeeper)
zk.start()

zk.ensure_path(args.item)
a = zk.set(args.item, bytes(args.data, 'utf-8') )
print('ctime="' + datetime.datetime.fromtimestamp(round(a[2] / 1000)).strftime(fmt) + '" mtime="' + datetime.datetime.fromtimestamp(round(a[3] / 1000)).strftime(fmt) + '" version=' + str(a[4]) + ' dataLength=' + str(a[8]) )

zk.stop()
