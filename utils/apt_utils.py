import subprocess

def set_installed(program_id:str,install:bool=True):
    subprocess.run(["sudo", "apt" if install else "apt-get", "install" if install else "remove", program_id, "-y"])

def update():
    subprocess.run(["sudo", "apt", "update"])
                   