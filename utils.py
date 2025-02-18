import subprocess

def terminal(command:str):
    print("> " + command)

def execute_command(command:str):
    terminal(command)
    subprocess.run(command, shell=True)
    print("\n\n")

def send_files_to_server(files_list:list, host:str, pem_key_path:str, directory:str = '/home/ubuntu/project_files/'):
    files_string = ' '.join(files_list)
    command = 'scp -i ' +  pem_key_path + ' ' + files_string + ' ' + host + ':' + directory
    execute_command(command)

def source_file_commands(source_file:str, encoding:str = 'latin-1') -> list:
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
    
    return commands