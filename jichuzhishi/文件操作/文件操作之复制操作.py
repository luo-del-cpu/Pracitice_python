# 文件的复制

# 原文件：C:\Users\86176\Desktop\python\test.png
# 目标文件：C:\Users\86176\Desktop\python\p1\test.png
# with 结合open使用可以帮助我们自动释放资源


with open(r'C:\Users\86176\Desktop\python\test.png', 'rb') as stream:
    container = stream.read()  # 读取文件内容
    with open(r'C:\Users\86176\Desktop\python\p1', 'wb') as wstream:
        wstream.write(container)
print('文件复制完成！')
