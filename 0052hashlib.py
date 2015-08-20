#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
mes_str = 'Use md5 in python hashlib.'
md5 = hashlib.md5()
md5.update(mes_str.encode('utf-8'))
print(md5.hexdigest())
print(md5.digest())
md5.update(b'Use md5 ')
md5.update(b'in python hashlib.')	# if len(mes_str) > block_size
print(md5.hexdigest())
print(md5.digest())
print(md5.digest_size, md5.block_size)

print(hashlib.sha224(b'Use md5 in python hashlib.').hexdigest())

def calc_md5(password):
    if len(password) > md5.block_size:
        return
    return hashlib.md5(password.encode('utf-8')).hexdigest()
print(calc_md5("a12345678*"))

def loginOK(loginDateBase, user, password):
    if user in loginDateBase:
        password += user[:3] + 'the_Salt'					##
        if calc_md5(password) == loginDateBase.get(user):
            return True
        else:
            return False		
			
loginDateBase = {}
def register(user, password):
    global loginDateBase
    loginDateBase[user] = calc_md5(password + user[:3] + 'the_Salt')
	
register("Lily", '123456')
print(loginDateBase)
print(loginOK(loginDateBase, "Lily", '123456'))
	
    