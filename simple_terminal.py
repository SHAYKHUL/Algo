import os
import shutil
import stat
import time
import subprocess
import socket

def help():
    print("Available commands:")
    print("- read: to read a file")
    print("- ls: List files and directories")
    print("- cd: Change current directory")
    print("- mkdir: Create a new directory")
    print("- touch: Create a new file")
    print("- rm: Delete a file or directory")
    print("- cat: Display the contents of a file")
    print("- echo: Append text to a file")
    print("- cp: Copy a file or directory")
    print("- mv: Move a file or directory")
    print("- find: Search for files or directories")
    print("- run: Execute a script")
    print("- rename: Rename a file or directory")
    print("- permissions: Show permissions of a file or directory")
    print("- info: Show information about a file or directory")
    print("- file_info: Show information about a file")
    print("- pwd: Show current directory")
    print("- clear: Clear the screen")
    print("- exit: Exit SimpOS")

def ls():
    files = os.listdir()
    for file in files:
        print(file)

def read(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def readlines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.rstrip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def show_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address: {ip_address}")

def cd(directory):
    try:
        if os.path.isdir(directory):
            os.chdir(directory)
        else:
            print(f"Error: '{directory}' is not a directory.")
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")

def mkdir(directory):
    try:
        os.mkdir(directory)
        print("Directory created:", directory)
    except FileExistsError:
        print("Directory already exists.")

def touch(filename):
    try:
        with open(filename, 'w') as file:
            pass
        print("File created:", filename)
    except PermissionError:
        print("Permission denied.")

def rm(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print("File deleted:", path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print("Directory deleted:", path)
        else:
            print("File or directory not found.")
    except FileNotFoundError:
        print("File or directory not found.")

def cat(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Contents of", filename + ":")
            print(content)
    except FileNotFoundError:
        print("File not found.")

def echo(filename):
    try:
        content = input("Enter text: ")
        with open(filename, 'a') as file:
            file.write(content)
            file.write('\n')
        print("Text appended to", filename)
    except PermissionError:
        print("Permission denied.")

def cp(source, destination):
    try:
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print("File copied:", source, "->", destination)
        elif os.path.isdir(source):
            shutil.copytree(source, destination)
            print("Directory copied:", source, "->", destination)
        else:            print("File or directory not found.")
    except FileNotFoundError:
        print("File or directory not found.")

def mv(source, destination):
    try:
        shutil.move(source, destination)
        print("Moved:", source, "->", destination)
    except FileNotFoundError:
        print("File or directory not found.")

def find(name, path):
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                if name in file:
                    print(os.path.join(root, file))
    except FileNotFoundError:
        print("Directory not found.")

def run(script):
    try:
        exec(open(script).read(), globals())
    except FileNotFoundError:
        print("Script not found.")
    except Exception as e:
        print("Error:", e)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def rename(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print("Renamed:", old_name, "->", new_name)
    except FileNotFoundError:
        print("File or directory not found.")

def pwd():
    print("Current directory:", os.getcwd())

def permissions(path):
    try:
        st = os.stat(path)
        permissions = stat.filemode(st.st_mode)
        print("Permissions:", permissions)
    except FileNotFoundError:
        print("File or directory not found.")

def info(path):
    try:
        st = os.stat(path)
        print("Path:", path)
        print("Size:", st.st_size, "bytes")
        print("Last modified:", time.ctime(st.st_mtime))
        print("Creation time:", time.ctime(st.st_ctime))
        print("Is directory:", os.path.isdir(path))
        print("Is file:", os.path.isfile(path))
    except FileNotFoundError:
        print("File or directory not found.")

def file_info(path):
    try:
        st = os.stat(path)
        print("File information for", path + ":")
        print("Size:", st.st_size, "bytes")
        print("Last modified:", time.ctime(st.st_mtime))
    except FileNotFoundError:
        print("File not found.")

def install_git():
    operating_system = os.name
    if operating_system == 'nt':
        print("Git installation is not supported on Windows.")
    elif operating_system == 'posix':
        try:
            subprocess.check_output(['apt', 'install', 'git', '-y'])
            print("Git installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to install Git. {e}")
    else:
        print("Unsupported operating system.")

def git_clone(url):
    try:
        subprocess.check_output(['git', 'clone', url])
        print("Repository cloned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to clone repository. {e}")

print("Welcome to SimpOS!")

while True:
    command = input("> ")

    if command == "help":
        help()
    elif command == "ls":
        ls()
    elif command.startswith("cd"):
        directory = command.split(" ")[1]
        cd(directory)
    elif command.startswith("mkdir"):
        directory = command.split(" ")[1]
        mkdir(directory)
    elif command.startswith("touch"):
        filename = command.split(" ")[1]
        touch(filename)
    elif command.startswith("info"):
        path = command.split(" ")[1]
        info(path)
    elif command.startswith("rm"):
        path = command.split(" ")[1]
        rm(path)
    elif command.startswith("cat"):
        filename = command.split(" ")[1]
        cat(filename)
    elif command.startswith("echo"):
        filename = command.split(" ")[1]
        echo(filename)
    elif command.startswith("cp"):
        source, destination = command.split(" ")[1], command.split(" ")[2]
        cp(source, destination)
    elif command.startswith("mv"):
        source, destination = command.split(" ")[1], command.split(" ")[2]
        mv(source, destination)
    elif command.startswith("find"):
        name, path = command.split(" ")[1], command.split(" ")[2]
        find(name, path)
    elif command.startswith("run"):
        script = command.split(" ")[1]
        run(script)
    elif command.startswith("rename"):
        old_name, new_name = command.split(" ")[1], command.split(" ")[2]
        rename(old_name, new_name)
    elif command == "pwd":
        pwd()
    elif command.startswith("permissions"):
        path = command.split(" ")[1]
        permissions(path)
    elif command.startswith("file_info"):
        path = command.split(" ")[1]
        file_info(path)
    elif command == "clear":
        clear()
    elif command == "exit":
        break
    elif command == "install_git":
        install_git()
    elif command.startswith("git_clone"):
        url = command.split(" ")[1]
        git_clone(url)
    else:
        print("Invalid command. Type 'help' for a list of available commands.")
