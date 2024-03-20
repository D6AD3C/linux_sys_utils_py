import subprocess

def firewall_allow_openssh():
    subprocess.run(["ufw", "allow" "OpenSSH"])

def firewall_set_enabled(enabled:bool=True):
    subprocess.run(["ufw", "enable" if enabled else "disable", "-y"])

def firewall_status():
    subprocess.run(["ufw", "status"])


