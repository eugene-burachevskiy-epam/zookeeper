#!/usr/bin/python3

import argparse
from argparse import RawDescriptionHelpFormatter
from kazoo.client import KazooClient
import kazoo.exceptions

parser = argparse.ArgumentParser(description='Zookeeper read client.\nReturns zookeeper item data in UTF-8 format to STDOUT. Returns "none" if no item exists', formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('item', action="store", help='/path/to/item')
group = parser.add_mutually_exclusive_group()
group.add_argument('-l', dest="listing", action="store_true", default=False, help='List nested items on /path')
group.add_argument('-d', dest="delete", action="store_true", default=False, help='Delete items on /path recursively')

args = parser.parse_args()

zookeeper = {
    'server':'127.0.0.1',
    'port':'2181'    
}

zk = KazooClient(hosts='%(server)s:%(port)s' % zookeeper)
zk.start()

if args.listing:
    try:
        answer = zk.get_children(args.item)
        print(answer)
    except kazoo.exceptions.NoNodeError:
        print('ERROR: No such path!')

elif args.delete:
    zk.delete(args.item, recursive=True)
    print(args.item + ' deleted!')

else:
    try:
        answer = zk.get(args.item)
        data = answer[0].decode('utf-8')
        print(data)
    except kazoo.exceptions.NoNodeError:
        print('none')

zk.stop()
