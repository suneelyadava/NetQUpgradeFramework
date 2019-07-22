import base64
import sys
import paramiko
import os




HydraUser='syadava'
HydraPassword="Intuit@54321"
HydraHostName='Hydra-11'
port=22




def preUpgradeTest():
    client = paramiko.Transport((HydraHostName, port))
    client.connect(username=HydraUser, password=HydraPassword)
    session = client.open_channel(kind='session')
    print (session)
    session.exec_command('scp /tmp/syadava/NetQ-2.2.0-SNAPSHOT.tgz'+' '+'cumulus@10.20.14.203:/tmp/')

preUpgradeTest()