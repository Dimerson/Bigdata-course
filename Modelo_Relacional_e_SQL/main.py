import sys
import os
from dotenv import load_dotenv

# adding root path to sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# importing util functions
from libs.common.starting import run_project

# Load enviroment variables
load_dotenv()
HOST = os.getenv("HOST")
PEM_KEY = os.getenv("PEM_KEY")

SCRIPT_FILE = r"Modelo_Relacional_e_SQL\script.txt"

def main():
    run_project(HOST,PEM_KEY,SCRIPT_FILE)

try:
    main()

except Exception as e:
    print(e)