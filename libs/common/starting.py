
from utils import send_files_to_server, execute_command

def file_name_from_path(path:str) -> str:
    try:
        script_name = path.split('\\')[-1]
    except:
        script_name = path
    
    return script_name

def run_project(host:str,
                pem_key_path:str,
                script_file:str,
                directory:str = '/home/ubuntu/project_files/',
                utils_file:str = "utils.py",
                compiler_file:str = "compiler.py"):
    
    # Send "utils.py", "compiler.py" and the command script to server
    send_files_to_server(files_list=[script_file, utils_file, compiler_file],
                         host=host,
                         pem_key_path=pem_key_path,
                         directory=directory,)
    
    script_name = file_name_from_path(script_file)
    compiler_name = file_name_from_path(compiler_file)
    
    # Run compiler.run_psql()
    command = "ssh -i " + pem_key_path + " " + host + " python3 " + directory + compiler_name + ' ' + directory + script_name
    execute_command(command)

    # Delete script file
    command = "ssh -i " + pem_key_path + " " + host + " rm " + directory + script_name
    execute_command(command)