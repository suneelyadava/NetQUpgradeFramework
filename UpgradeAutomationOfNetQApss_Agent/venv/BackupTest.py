import paramiko
import re
import time

nbytes = 4096
hostname = '10.20.14.192'
port = 22
username = 'cumulus'
password = 'CumulusLinux!'
command3 = "echo 'CumulusLinux!' | sudo -S -k backuprestore.sh -b -l /tmp/backuprestore/"
command1 = "export HISTIGNORE='*sudo -S*'"


def backuptest():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, username='cumulus', password='CumulusLinux!', port=22)
    (stdin, stdout, stderr) = s.exec_command(command1)
    print stdout.read()
    time.sleep(5)
    (stdin, stdout, stderr) = s.exec_command(command3)
    print stdout.read()
    s.close()


backuptest()
