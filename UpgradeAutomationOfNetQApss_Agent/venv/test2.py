
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    session = client.open_channel(kind='session')
    stdout_data = []
    stderr_data = []
    #session.exec_command(command)
    session.exec_command('echo CumulusLinux! | sudo -S ls')

    session.exec_command('backuprestore.sh -b -l /tmpt/suneel/')

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









s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    s.exec_command('echo CumulusLinux! | sudo -S ls')
    (stdin, stdout, stderr) = s.exec_command('sudo backuprestore.sh -b -l /opt/suneel/')

    for line in stdout.readlines():
        print line
    s.close()


    client.connect(username=username, password=password)
    session = client.open_channel(kind='session')
    stdout_data = []
    stderr_data = []
    session.exec_command('echo CumulusLinux! | sudo -S ls')
    #session.exec_command('sudo backuprestore.sh -b -l /opt/suneel/')
    #ession.exec_command('kubectl get pods')

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