import paramiko
import re
import time

nbytes = 4096
hostname = '10.20.14.192'
port = 22
username = 'cumulus'
password = 'CumulusLinux!'
command1 = "export HISTIGNORE='*sudo -S*'"
command2 = "echo CumulusLinux! | sudo -u root --stdin ls ; echo Y | sudo backuprestore.sh -r -l /tmp/backuprestore/"


def restoretest():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, username='cumulus', password='CumulusLinux!', port=22)
    (stdin, stdout, stderr) = s.exec_command(command1)
    print stdout.read()
    (stdin, stdout, stderr) = s.exec_command(command2)
    print stdout.read()
    s.close()


restoretest()
