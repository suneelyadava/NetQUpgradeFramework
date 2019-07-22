import base64
import sys
import paramiko

nbytes = 4096
hostname = '10.20.14.203'
port = 22
username = 'cumulus'
password = 'CumulusLinux!'
command = 'kubectl get pods'

def  loginSession():
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    session = client.open_channel(kind='session')

    return session

def NetQAppsUpgradeTest():
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)

    stdout_data = []
    stderr_data = []
    session = client.open_channel(kind='session')
    session.exec_command(command)

    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break

    print 'exit status: ', session.recv_exit_status()
    print ''.join(stdout_data)
    print ''.join(stderr_data)

    session.close()
    client.close()

NetQAppsUpgradeTest()

# Setting up the aws cli to download the tar ball for NetQ apps upgrade
def preUpgradeTest():
    HydraUser = ''
    HydraPassword = ''
    HydraHostName = ''
    client = paramiko.Transport((HydraHostName, port))
    client.connect(username=HydraUser, password=HydraPassword)
    sessionOfHydra = client.open_channel(kind='sessionOfHydra')
    sessionOfHydra.exec_command('scp /tmp/syadava/NetQ-2.2.0-SNAPSHOT.tgz')







