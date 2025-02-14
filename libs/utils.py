import paramiko

def join_source_file_commands(source_file:str, encoding:str = 'latin-1') -> str:
    """
    Encoding : ['utf-8', 'latin-1', 'cp1252']
    """

    with open(source_file, 'r', encoding=encoding) as file:
        commands = []
        for line in file:
            content = line.strip()
            try:
                if content[0] != '#':
                    commands.append(content)
                    print(content)
            except:
                pass
    
    return ' && '.join(commands)


def run_powershell_script(source_file:str, pem_key_path:str, host:str, user:str):
    """
    Starts a connection with the AWS server and input the commands on source_file
    """

    pem_key = paramiko.RSAKey(pem_key_path)

    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    cliente.connect(hostname=host, username=user, pkey=pem_key)

    stdin, stdout, stderr = cliente.exec_command(join_source_file_commands(source_file))
    print(stdout.read().decode())

    cliente.close()