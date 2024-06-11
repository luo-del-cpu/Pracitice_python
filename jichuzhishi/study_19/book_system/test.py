def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            # 在这里处理文件内容  
            print(f"文件内容:\n{contents}")
    except FileNotFoundError:
        print(f"文件 {filename} 不存在。")
    else:
        print(f"文件 {filename} 已成功读取。")
    finally:
        # 注意：在这个例子中，finally块是多余的，因为with语句会自动关闭文件  
        # 但它通常用于执行无论是否发生异常都需要进行的清理操作  
        print("执行了清理操作（如果有的话）。")

    # 调用函数


read_file('example.txt')