import base64
from Crypto.Cipher import AES
from Crypto.Util import Counter
 
def aes_ctr_encode(data, key):
    ctr = Counter.new(128) 
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CTR, counter=ctr)
    return base64.b64encode(cipher.encrypt(data.encode('utf-8')))
 
def aes_ctr_decode(enc, key):
    ctr = Counter.new(128)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CTR, counter=ctr)
    return cipher.decrypt(base64.b64decode(enc)).decode('utf-8')
 
if __name__ == '__main__':
    key = 'asdfzxcvg0qwerab'
    data = input()
    encrypted_data = aes_ctr_encode(data, key)
    print("encrypted data:", encrypted_data)
 
    decrypted_data = aes_ctr_decode(encrypted_data,key)
    print("decrypted data:", decrypted_data)
