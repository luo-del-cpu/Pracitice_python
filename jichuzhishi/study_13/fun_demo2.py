# # @Time : 2023/11/19 21:31
# # @Author : luoxin
#
#
# """
# 可变参数：
# 定义方式：
def add(*args):
    print(args)



def add(*args):  # 这里参数可传可不传，这里系统会自动准备一个元组(),将函数调用的参数放入这个元组
    sum = 0
    print(args)
    if len(args) > 0:
        for i in args:
            sum += i
        print("得出的和是：", sum)
    else:
        print("没有可加的元素")


add()
add(1)
add(1, 2)
add(1, 2, 3, 4)


def add(name, *args):
    sum = 0
    if len(args) > 0:
        for i in args:
            sum += i
        print(f"{name}得出的和是:{sum}")
    else:
        print("没有可加的元素")


add('张三', 1, 2, 3, 4)  # 在有不可变参数和可变参数同时存在时，不可变的参数必须放在前面


def test(*args):
    print(args)


t1 = [1, 2, 3, 4]
test(t1)  # 得出：([1, 2, 3, 4],)
test(*t1)  # 得出：(1, 2, 3, 4)

# 如果传参时，直接传1个列表或者元组，那么就会作为一个整体传给函数，函数进行装包
# 但是如果传参时，加了*，那么就会先进行拆包，在将参数传进函数，函数进行一个装包


def test(m):
    print(111)
a=[1,2,3]
test(a)