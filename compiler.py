import sys
import subprocess
from utils import source_file_commands

def print_result(process):
    # Exibe a saída do psql
    if process.returncode == 0:
        print("Comando executado com sucesso!")
        print(process.stdout)
    else:
        print(f"Erro ao executar o comando: {process.stderr}")

def run_psql(script_name:str):
    script_commands = source_file_commands(script_name)

    # There is a problem with the command 'sudo su - postgres' and 'psql'
    try:
        first_comms = script_commands[:script_commands.index('sudo su - postgres')]
        last_coms = script_commands[script_commands.index('sudo su - postgres') + 1:]

        try:
            before_psql_com = last_coms[:last_coms.index('psql')]
            after_psql_com = last_coms[last_coms.index('psql') +1:]

        except:
            before_psql_com = []
            after_psql_com = []
        
        cmd_simple = ' && '.join(first_comms)
        cmd_advanced = ["sudo", "-u", "postgres"] + before_psql_com + ["psql", "-c"] + after_psql_com

    except:
        cmd_simple = ' && '.join(script_commands)
        cmd_advanced = []
    


    """
    # Comando para rodar psql como o usuário postgres e executar os comandos desejados
    cmd = [
        "sudo", "-u", "postgres", "psql", "-c",
        "create database psycopg;"
    ]
    """

    # Executa o comando e captura a saída
    process = subprocess.run(cmd_simple, shell=True)
    print_result(process)

    process = subprocess.run(cmd_advanced, capture_output=True, text=True)
    print_result(process)


if __name__ == "__main__":
    run_psql(sys.argv[1])