import hashlib
import hmac
import binascii
import base64
import urllib
import random
import urllib2

from totp_module.hotptt import generate
from totp_module.hotptt import hotp
from totp_module.hotptt import totp

'''remplacer la cle, avec celle qui est generee'''
print 'Ce sont des tests avec la cle: JRTHSQRWIF4FCUDMIB3WYRTCINRVQRLR'
print 'hex==> '+totp('4c66794236417851506c40776c46624363584571','hex')
print 'base32==> '+totp('JRTHSQRWIF4FCUDMIB3WYRTCINRVQRLR','base32')
print 'ascii==> '+totp('LfyB6AxQPl@wlFbCcXEq','ascii')



