def round_function(data, key):
    """轮函数，对每个元素进行按位异或操作"""
    return [x ^ key for x in data]  # 遍历列表，对每个元素进行异或操作

def feistel_cipher_encrypt(data, keys, num_rounds):
    """Feistel加密"""
    left, right = data[:len(data)//2], data[len(data)//2:]  # 分成左右两部分
    for round in range(num_rounds):
        # 轮加密，右半部分通过轮函数加密
        new_right = round_function(right, keys[round])
        # 左右部分交换，同时更新左部分
        left, right = right, [x ^ y for x, y in zip(left, new_right)]
    return left + right

def feistel_cipher_decrypt(data, keys, num_rounds):
    """Feistel解密"""
    left, right = data[:len(data)//2], data[len(data)//2:]
    keys = keys[::-1]  # 反转密钥顺序
    for round in range(num_rounds):
        # 轮解密，左半部分通过轮函数加密
        new_left = round_function(left, keys[round])
        # 左右部分交换，同时更新右部分
        left, right = [x ^ y for x, y in zip(new_left, right)], left
    return left + right

# 测试数据
data = [0x12, 0x34, 0x56, 0x78]  # 明文数据
keys = [0xAB, 0xCD, 0xEF]        # 子密钥
num_rounds = len(keys)           # 加密轮数

# 加密和解密
encrypted_data = feistel_cipher_encrypt(data, keys, num_rounds)
decrypted_data = feistel_cipher_decrypt(encrypted_data, keys, num_rounds)

# 输出结果
print("Original data:", data)
print("Encrypted data:", encrypted_data)
print("Decrypted data:", decrypted_data)