# @Time : 2023/11/21 22:16
# @Author : luoxin


"""
可变参数+关键字参数(key=value)

"""
print("*"*50+"关键字传参"+"*"*50)

def add(a, b=10):
    res = a + b
    print(res)


add(5)

add(4, 7)  # 得出11：如果给了值，那么就会覆盖给出的10


def add1(a, b=10, c=4):
    res = a + b + c
    print(res)


add1(2, 6)  # 得出12：这里的6就会覆盖原有的10
add1(2, c=6)  # 得出18：如果想给某个关键字赋值，需要明确指明

print("*"*100)

print("*"*50+"可变参数传参"+"*"*50)

def test(**kwargs):  # 这里**kwargs在函数调用时，可传参数也可以不传；会准备一个字典{};若要传参，必须是关键字参数:key=value
    print(kwargs)


dict1 = {"001": "python", "002": "java", "003": "go", "004": "php"}

# test(a=1, b=2)  # 得出：{'a': 1, 'b': 2}
# test({'a': 1, 'b': 2}) # 不能直接传入一个字典，必须先进行解包的操作（解包成关键字参数key=value的形式）

# **dict1:给函数赋值的时候，会将字典拆包成关键字参数的形式，然后传给**kwargs，这时又会将拆的包重新装成字典
test(**dict1)  # 得出：{'001': 'python', '002': 'java', '003': 'go', '004': 'php'}

print(*dict1) # 001 002 003 004
