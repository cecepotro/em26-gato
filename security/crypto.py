from cryptography.fernet import Fernet

key = b'qG_2ShDlQmyCcoMOW-475pNRaxlnf-3NxlqP1P2Pzao='

fernet = Fernet(key)

def encrypt(value):
    return fernet.encrypt(value.encode()).decode()

def decrypt(value):
    return fernet.decrypt(value.encode()).decode()