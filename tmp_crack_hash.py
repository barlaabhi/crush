import subprocess
#from pwn import *
import base64
import hashlib


hash_val = input("Hash: ")
str_len  = input("Length: ")
res = subprocess.check_output(['python3','projects/crush/crush.py','-s',hash_val,'-b','-l',str_len]).decode().split('\n')


print(res[2])