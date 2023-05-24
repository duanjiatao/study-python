import os
from binascii import b2a_hex, a2b_hex

import toml
from Crypto.Cipher import AES

SECRET_KEY = 'K3N8b9p!prU4&<!A'
CODE_UTF8 = 'utf-8'
END_STR = '\0'

# 全局配置
CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'config.toml')
CONFIG = toml.load(CONFIG_FILE)


def get_mysql_connect_conf():
    """
    获取mysql连接配置
    :return:
    """
    db_conf = CONFIG['db']['mysql']['connect']
    db_conf['password'] = decrypt(db_conf['password'])
    return db_conf


def get_mysql_pool_conf():
    """
    获取mysql连接池配置
    :return:
    """
    pool_conf = CONFIG['db']['mysql']['pool']
    return pool_conf


def encrypt(plaintext):
    """
    加密
    :param plaintext:原文
    :return: 密文
    """
    key = SECRET_KEY.encode(CODE_UTF8)
    plaintext = plaintext + (16 - len(plaintext) % 16) * END_STR
    cipher = AES.new(key, AES.MODE_ECB)
    cipher_text = cipher.encrypt(plaintext.encode(CODE_UTF8))
    return b2a_hex(cipher_text).decode(CODE_UTF8)


def decrypt(ciphertext):
    """
    解密
    :param ciphertext:密文
    :return: 原文
    """
    key = SECRET_KEY.encode(CODE_UTF8)
    cipher = AES.new(key, AES.MODE_ECB)
    plain_text = cipher.decrypt(a2b_hex(ciphertext))
    return plain_text.decode(CODE_UTF8).rstrip(END_STR)


if __name__ == '__main__':
    e = encrypt("123456")
    d = decrypt(e)
    print("加密:", e)
    print("解密:", d)
