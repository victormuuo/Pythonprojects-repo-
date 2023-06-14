from cryptography.fernet import Fernet
import base64


#def write_key():
    #key=Fernet.generate_key()
    #with open("key.key","wb") as key_file:
        #key_file.write(key)
#write_key()

def load_key():
    file=open("key.key", "rb")
    key=file.read()
    file.close()
    return key


master_pwd=input("Enter master password: ")

key=load_key() + master_pwd.encode()
fer=Fernet(key)

def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw=data.split("|")
            print("Username:", user, " |Password:",
                  fer.decrypt(passw))
                 # base64.decode(fer.decrypt(passw, encoding="ascii")))
           

def create():
    name=input("username: ")
    pwd=input("password: ")

    with open("passwords.txt",'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode=input("Create a new password or view existing ones (view, create), press x to quit? ").lower()
    if mode=="x":
        break

    if mode=="view":
        view()
    elif mode=="create":
        create()
    else:
        print("Invalid mode.")
        continue

