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


generate(20, name="new secret key",symbols=True)
"""generation d'une cle secrete a partager avec l'application mobile"""
