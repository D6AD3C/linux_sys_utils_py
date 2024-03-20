import subprocess

def add_super_user_with_input():
    user_name = input("Enter the super username: ")
    add_super_user(user_name)

def add_super_user(user_name):
    subprocess.run(["adduser", user_name])
    subprocess.run(["usermod", "-aG", "sudo", user_name])