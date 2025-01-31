Created on Fri Jan 31 20:22:59 2025

@author: LENOVO
"""

from cryptography.fernet import Fernet,MultiFernet
# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
token
b'...'

print(token)
k=f.decrypt(token)
#print('---------------------------------------------------------------------')

print(k)

print('---------------------------------------------------------------------')


#from cryptography.fernet import Fernet, MultiFernet
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
f1 = MultiFernet([key1, key2])
token1 = f1.encrypt(b"Secret message!")
#token1
print(token1)
#b'...'
k1=f1.decrypt(token1)
#b'Secret message!'

print(k1)
print('---------------------------------------------------------------------')

#print('---------------------------------------------------------------------')


#from cryptography.fernet import Fernet, MultiFernet
key3 = Fernet(Fernet.generate_key())
key4 = Fernet(Fernet.generate_key())
f2 = MultiFernet([key3, key4])
token2 = f2.encrypt(b"Secret message!")
print(token2)
#b'...'
l1=f2.decrypt(token2)
#b'Secret message!'
print(l1)
print('---------------------------------------------------------------------')
#print(-------------------------------------------------------------------------------)
key5 = Fernet(Fernet.generate_key())
f3 = MultiFernet([key5, key3, key4])
rotated = f3.rotate(token2)
print(rotated)
l2=f3.decrypt(rotated)

print(l2)
#b'Secret message!'

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password = b"password"
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=1_000_000,
)
key5 = base64.urlsafe_b64encode(kdf.derive(password))
f5 = Fernet(key5)
token5 = f5.encrypt(b"Secret message!")
token5
b'...'
f5.decrypt(token5)
b'Secret message!'



#b'A really secret message. Not for prying eyes.'
