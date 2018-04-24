## Simple Zookeeper shell client.

Run script with --help for usage details.

Edit script for your Zookeeper server connection details.


Usage example:
```shell
root@vbox:~# zooset some_path/newitem 'hello world'
ctime="2018-04-24 12:09:40" mtime="2018-04-24 12:24:47" version=2 dataLength=11
root@vbox:~# zooget -l /
['some_path', 'rootitem', 'integer', 'zookeeper', 'somedata']
root@vbox:~# zooget -l /some_path
['newitem']
root@vbox:~# zooget /some_path/newitem
hello world
root@vbox:~#
```
