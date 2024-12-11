from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# AES加密函数
def aes_encrypt(key: bytes, plaintext: str) -> (bytes, bytes):
    cipher = AES.new(key, AES.MODE_CBC)  # 使用CBC模式
    iv = cipher.iv  # 随机生成的初始化向量
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))  # 填充数据并加密
    return iv, ciphertext

# AES解密函数
def aes_decrypt(key: bytes, iv: bytes, ciphertext: bytes) -> str:
    cipher = AES.new(key, AES.MODE_CBC, iv)  # 传入相同的IV
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)  # 解密并去除填充
    return plaintext.decode()

# 示例
if __name__ == "__main__":
    # 生成一个16字节的密钥 (128位)
    key = get_random_bytes(16)
    plaintext = "Hello, AES encryption!"

    print(f"原始文本: {plaintext}")
    print(f"加密密钥: {key.hex()}")

    # 加密
    iv, ciphertext = aes_encrypt(key, plaintext)
    print(f"初始化向量 (IV): {iv.hex()}")
    print(f"密文: {ciphertext.hex()}")

    # 解密
    decrypted_text = aes_decrypt(key, iv, ciphertext)
    print(f"解密后的文本: {decrypted_text}")