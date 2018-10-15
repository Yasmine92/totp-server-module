import hashlib
import hmac
import binascii
import base64
import urllib
from random import *
import urllib2
from dateutil.parser import parse


__all__ = ( 'totp','hotp')


'''Truncate(HMAC(K,C))'''
def truncated_value(h):
    bytes = map(ord, h)
    offset = bytes[-1] & 0xf
    v = (bytes[offset] & 0x7f) << 24 | (bytes[offset+1] & 0xff) << 16 | \
            (bytes[offset+2] & 0xff) << 8 | (bytes[offset+3] & 0xff)
    return v


'''HOTP(K,C) mod 10p p: the desired number of digits'''

def dec(h,p):
    v = truncated_value(h)
    v = v % (10**p)
    return '%0*d' % (p, v)


def int2beint64(i):
    hex_counter = hex(long(i))[2:-1]
    hex_counter = '0' * (16 - len(hex_counter)) + hex_counter
    bin_counter = binascii.unhexlify(hex_counter) 
    return bin_counter

'''HOTP(K,C) = Truncate(HMAC(K,C)) & 0x7FFFFFFF'''
def __hotp(key, counter,encoding='hex', hash=hashlib.sha1):
    bin_counter = int2beint64(counter)
    if encoding=='hex':
       bin_key = binascii.unhexlify(key) 
    elif encoding=='ascii':
        bin_key= key
    elif encoding=='base32':
        bin_key=base64.b32decode(key, )
    else :
        print 'encoding format non supported'
    return hmac.new(bin_key, bin_counter, hash).digest()

def hotp(key,counter,encoding='hex',format='dec6',hash=hashlib.sha1):
    bin_hotp = __hotp(key, counter,encoding, hash)
    
    if (format == 'dec4'):
        return dec(bin_hotp, 4)
    elif (format == 'dec6'):
        return dec(bin_hotp, 6)
    elif (format == 'dec7'):
        return dec(bin_hotp, 7)
    elif (format == 'dec8'):
        return dec(bin_hotp, 8)
    elif (format == 'hex'):
        return hex(truncated_value(bin_hotp))[2:]
    elif (format == 'hex-notrunc'):
        return binascii.hexlify(bin_hotp)
    elif (format == 'bin'):
        return bin_hotp
    elif format == 'dec':
        return str(truncated_value(bin_hotp))
    else:
        raise ValueError('unknown format')


'''getservertime permet d'avoir le temps du serveur google,pour des raisons de synchronisation, on peut le remplacer par un autre serveur http'''
def getservertime():
    request = urllib2.Request('http://google.com')
    response=urllib2.urlopen(request)
    date=response.info().getheader('Date')
    d=parse(date)
    return d.strftime('%s')

'''t = int(time.time())'''
'''si on veut avoir le temps de la machine'''
'''key est de format hex'''
def totp(key,encoding='hex', format='dec6', step=30, t=None,initial_time=0, hash=hashlib.sha1):
     if t is None:
        t = int(getservertime());
     else:
        if isinstance(t, datetime.datetime):
            t = calendar.timegm(t.utctimetuple())
        else:
            t = int(t)
     T = int(t/step)
     return hotp(key, T,encoding, format=format, hash=hash)
	
def generate_key_ascii(symbols,length=30):
    set = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz';
    if symbols:
        set += '!@#$%^&*()<>?/[]{},.:;'
    key=''
    for i in range(length):
        key+=choice(set)
    return key


'''generation d'une cle secrete, en ascii, hex, et base32'''
'''google authenticator, prend en charge des cles en format base32'''
'''le lien vers le code a bare a scanner est genere aussi'''
def generate(length, name="secret key",symbols=True):
    key=generate_key_ascii(symbols,length)
    key_ascii=key;
    key_hex=key.encode("hex");
    key_base32=base64.b32encode(key).replace(' ','');
    google_auth_qr = 'https://chart.googleapis.com/chart?chs=166x166&chld=L|0&cht=qr&chl=otpauth://totp/' + urllib.quote(name.encode("utf-8")) + '%3Fsecret=' + urllib.quote(key_base32.encode("utf-8"))
    print "Generated key in ascii==> "+key_ascii
    print "Generated key in hex==> " +key_hex
    print "Generated key in base32==> "+key_base32
    print "google_auth_qr==>" +google_auth_qr


def is_it_correct(key,code,encoding='base32'):
      	code2=totp(key,encoding, )
	if code==code2:
	      print "your code is correct"
	else:
	      print "your code is not correct"

