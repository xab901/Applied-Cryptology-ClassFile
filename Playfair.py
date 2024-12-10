def locate(char: chr, cipher_table: list) -> tuple:
    """查找字符在矩阵中的位置"""
    for i in range(1, 6):
        for j in range(1, 6):
            if cipher_table[i][j] == char:
                return i, j
    return -1, -1


def encrypt(plaintext_ls: list, cipher_table: list) -> list:
    """加密函数"""
    ciphertext_ls = []
    cur = 0
    while cur < len(plaintext_ls) - 1:
        x1, y1 = locate(plaintext_ls[cur], cipher_table)
        x2, y2 = locate(plaintext_ls[cur + 1], cipher_table)
        if x1 == x2:  # 同一行，右移
            ciphertext_ls.append(cipher_table[x1][(y1 % 5) + 1])
            ciphertext_ls.append(cipher_table[x2][(y2 % 5) + 1])
        elif y1 == y2:  # 同一列，下移
            ciphertext_ls.append(cipher_table[(x1 % 5) + 1][y1])
            ciphertext_ls.append(cipher_table[(x2 % 5) + 1][y2])
        else:  # 不同行不同列，交换列坐标
            ciphertext_ls.append(cipher_table[x1][y2])
            ciphertext_ls.append(cipher_table[x2][y1])
        cur += 2
    return ciphertext_ls


def decrypt(ciphertext_ls: list, cipher_table: list) -> list:
    """解密函数"""
    plaintext_ls = []
    cur = 0
    while cur < len(ciphertext_ls) - 1:
        x1, y1 = locate(ciphertext_ls[cur], cipher_table)
        x2, y2 = locate(ciphertext_ls[cur + 1], cipher_table)
        if x1 == x2:  # 同一行，左移
            plaintext_ls.append(cipher_table[x1][y1 - 1 if y1 > 1 else 5])
            plaintext_ls.append(cipher_table[x2][y2 - 1 if y2 > 1 else 5])
        elif y1 == y2:  # 同一列，上移
            plaintext_ls.append(cipher_table[x1 - 1 if x1 > 1 else 5][y1])
            plaintext_ls.append(cipher_table[x2 - 1 if x2 > 1 else 5][y2])
        else:  # 不同行不同列，交换列坐标
            plaintext_ls.append(cipher_table[x1][y2])
            plaintext_ls.append(cipher_table[x2][y1])
        cur += 2
    return plaintext_ls


def generate_cipher_table(key: str) -> list:
    """生成密码表"""
    letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I 和 J 合并
    used_letters = set(key)  # 密钥中的字符
    cipher_table = [[0] * 6 for _ in range(6)]  # 初始化矩阵

    # 填入密钥
    idx = 0
    for i in range(1, 6):
        for j in range(1, 6):
            if idx < len(key):
                cipher_table[i][j] = key[idx]
                idx += 1
            else:
                break
        if idx >= len(key):
            break

    # 填入剩余字母
    letters = [ch for ch in letters if ch not in used_letters]
    for i in range(1, 6):
        for j in range(1, 6):
            if cipher_table[i][j] == 0:
                cipher_table[i][j] = letters.pop(0)

    return cipher_table


def preprocess_plaintext(plaintext: str) -> list:
    """处理明文字符串"""
    plaintext = plaintext.upper().replace(" ", "").replace("J", "I")
    plaintext_ls = list(plaintext)
    cur = 0
    while cur < len(plaintext_ls) - 1:
        if plaintext_ls[cur] == plaintext_ls[cur + 1]:  # 相同字符插入 X
            plaintext_ls.insert(cur + 1, 'X')
        cur += 2
    if len(plaintext_ls) % 2:  # 补充 X
        plaintext_ls.append('X')
    return plaintext_ls


# 主函数流程
print('请输入明文：', end='')
plaintext = input().strip()
print('请输入密钥：', end='')
key = ''.join(dict.fromkeys(input().strip().upper()))  # 去重并保持顺序
cipher_table = generate_cipher_table(key)

# 展示密码本
print('本次加密所使用的密码本如下：')
for i in range(1, 6):
    print(' '.join(cipher_table[i][1:]))

# 处理明文
plaintext_ls = preprocess_plaintext(plaintext)
print(f'处理后的明文为：{"".join(plaintext_ls)}')

# 加密
ciphertext_ls = encrypt(plaintext_ls, cipher_table)
ciphertext = ''.join(ciphertext_ls)
print(f'加密后的密文为：{ciphertext}')

# 解密
print('请输入想要解密的密文：', end='')
ciphertext = input().strip()
ciphertext_ls = list(ciphertext)
plaintext_ls = decrypt(ciphertext_ls, cipher_table)
plaintext = ''.join(plaintext_ls)
print(f'解密后的明文为：{plaintext}')