#!/usr/bin/python2.7
'''
This script can exec the commdlist you give in the hosts list
'''

import threading
import paramiko
import subprocess

cmd_list = ['id',
        'w',
        'netstat -apn|grep tcp',
        'cat /etc/passwd'
        ]

def ssh_command(ip, user, passwd, command):rc
    for x in command:
        client = paramiko.SSHClient()
        #client.load_host_keys('/root/.ssh/know_hosts')
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=user, password=passwd)
        ssh_session = client.get_transport().open_session()
        if ssh_session.active:
            ssh_session.exec_command(x)
            print ssh_session.recv(1024)
            print
    return

ssh_command('127.0.0.1','root','password',cmd_list)
ssh_command('192.168.1.1','root','password',cmd_list)
