'''
无参数的函数:

def func():
    print()
func()
--------------------
有参数的函数:
1.普通参数

def func(name,age):
    print()
func("aa",18)-------->形参和实参的个数要一致,不一致时会报错

2.可变参数

1)def func(*args):
    print(args)
func()--------->1：得到的是一个空的元组 “（）”
                2：函数调用时，实参的个数可以没有，也可以多个
                3：“*”：一颗星的时候，不能传关键字参数（key=value）
                例：可传：func(4)  func(5,‘h’)
                func()--->()；func(1)--->(1,)；func(1,2)--->(1,2)

2)def func(**kwargs):
    print()
func(a=1,b=2)---->1：得到的是一个字典：“{‘a’:1,'b':2}”
                  2：函数调用时，实参的个数可以没有，也可以多个
                  3：“**”：两颗星的时候，必须传的是关键字参数
                  4：例： func()--->{}；func(a=1)--->{'a':1}；func(a=1,b=2)--->{'a':1,'b':2}
3）def func(*args,**kwargs):
    print(args，kwarg)
list = [1,2,3,4,5]
dict = {'1':'a','2':'b'}
func(list,**dict)----->([1,2,3,4,5]) {'1':'a','2':'b'}){}
func(*list,**dict)---->(1,2,3,4,5) {'1':'a','2':'b'}
解释：【在给函数赋值的时候】func(*list,**dict)中加“*”号表示进行了拆包;其中对列表进行拆包时，在列表前加一个”*“即可；
     得到结果---->func(1,2,3,4,5,'1'='a','2'='b')

4)混用
def func(name,*args,**kwargs):----->一般在混用的情况下，已知确定的(不可变参数)放在最前面（name）,可变的参数
                                    一颗星（不知道数量的）放在两颗星（关键字参数）的前面
    print()
func('tom')----->必须要赋值（因为name是必传参数）

3.默认值+关键字
def func(name,age=18):
    print(name,age)
func('tom')---->tom 18
func('tom',age=20)---->关键字的赋值（可使用key来进行对原有age=18的覆盖）

4.关键字赋值
def func(a,b=1,c=2)--->可以使用关键字给参数默认的值
    result = a+b+c
    print(result)
func(1)--->1+1+2=4
func(1,2)--->1+2+2=5--->传入的2会将默认的b=1覆盖，得出b=2
func(1,2,3)--->1+2+3=6--->传入的2,3会将默认的b=1,c=3覆盖，得出b=2,c=3
func(1,c=3)--->1+1+3=5--->若只想覆盖其中的一个参数，则需要指定关键字key=value来复制
'''

def func(*args,**kwargs):
    print(args,kwargs)
list = [1,2,3,4,5]
dict = {'1':'a','2':'b'}
func(*list,**dict)