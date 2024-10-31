# test.py

import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def execute_command(command):
    os.system(command)

if __name__ == "__main__":
    # Vulnerable to path traversal
    file_content = read_file("../../etc/passwd")
    print(file_content)

    # Vulnerable to command injection
    execute_command("ls; rm -rf /")