# 加密算法:md5 sha1 sha256
import hashlib

msg = '加密测试'
md5 = hashlib.md5(msg.encode('utf-8'))  # 使用时必须进行编码

print(md5.hexdigest())  # 转换成16进制的表示方法：f447f32b28217406a6fb8772cdec471c
