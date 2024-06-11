# @Time : 2024/6/4 21:31
# @Author : luoxin

import os

src_dir = r'./1'
tar_dir = r'./2'
def copy(src, target):
    # 判断传入的是否为文件夹路径
    if os.path.isdir(src) and os.path.isdir(target):
        # 查看原文件夹下所有的文件（列表返回）
        filelist = os.listdir(src)  # 第一层文件夹遍历结果：['aa.txt',...,'pp']；第二层文件夹遍历结果：['pp.txt',...]
        # 遍历得到的文件夹下的列表
        for file in filelist:
            # 对每一个文件拼接成新的路径
            path = os.path.join(src, file)  # 第一层文件夹与文件拼接结果： ...\p1\aa.txt；第一层文件夹与文件拼接结果： ...\p1\pp
            print("---",path)
            # 判断新拼接的路径是否有文件夹
            if os.path.isdir(path):
                # 将文件夹内的文件夹与目标文件夹拼接成一个新的路径
                target_path_1 = os.path.join(target, file)
                # 创建拼接成功后的文件夹
                os.mkdir(target_path_1)
                '''
                此处经过写过后发现，进入文件夹后的操作和第一次进入文件夹的操作一致，即可调用函数本身（递归函数）完成
                # #如果是文件夹，那就进入（切换）文件夹内，继续遍历
                # os.chdir(path)
                # #继续读文件夹内的内容
                # filelist_1 = os.listdir(path)
                # for file_1 in filelist_1:
                #     os.path.join(path,file_1)
                '''
                # 递归调用copy（）
                copy(path, target_path_1)  # 此处传值应为path，因为在第一遍遍历完成后，需要进入的是拼接后的文件夹内即...\p1\pp
            # 如果没有文件夹，则进行文件读取操作
            else:
                # 建立管道读取文件内容
                with open(path, 'rb') as rstream:
                    # 将读到的内容放入一个容器中
                    result = rstream.read()
                    # 构建一个目标文件夹中复制的文件名称
                    path_1 = os.path.join(target, file)
                    # 建立与目标文件夹的管道进行写文件
                    with open(path_1, 'wb') as wrstream:
                        wrstream.write(result)

        else:
            print('复制完毕')
    else:
        print('输入的不是文件夹路径！！！')


copy(src_dir, tar_dir)