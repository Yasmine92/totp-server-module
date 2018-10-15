import hashlib
import hmac
import binascii
import base64
import urllib
import random
import urllib2
import cmd


from totp_module.hotptt import totp
from totp_module.hotptt import is_it_correct
'''print is_it_correct('JRTHSQRWIF4FCUDMIB3WYRTCINRVQRLR',030425, )'''
key, code = raw_input("Enter your key and code value (JRTHSQRWIF4FCUDMIB3WYRTCINRVQRLR 832987): ").split()
print key
print code
print is_it_correct(key,code, )

''' cle predifinie
key='JRTHSQRWIF4FCUDMIB3WYRTCINRVQRLR'
input_code = input("Enter your generated code(in this form '832987': ")

if input_code==totp(key,'base32', ):
    print "your code is correct"
else:
    print "your code is not correct"'''
