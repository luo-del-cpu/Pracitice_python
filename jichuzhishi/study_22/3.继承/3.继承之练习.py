# 工资管理系统：具体要求看B站视频中“继承练习”的内容
class Person():
    def __init__(self, no, name, salary):
        self.no = no
        self.name = name
        self.salary = salary

    def __str__(self):
        msg = '工号：{} 姓名：{} 工资：{}'.format(self.no, self.name, self.salary)
        return msg

    def getSalary(self):
        return self.salary


class Worker(Person):
    def __init__(self, no, name, salary, hours, per_hour):
        super().__init__(no, name, salary)
        self.hours = hours
        self.per_hour = per_hour

    def getSalary(self):
        money = self.hours * self.per_hour
        self.salary += money
        return self.salary


class Saleman(Person):
    def __init__(self, no, name, salary, sale_money, per):
        super().__init__(no, name, salary)
        self.sale_money = sale_money
        self.per = per

    def gerSalary(self):
        money = self.sale_money * self.per
        self.salary += money
        return self.salary


# 创建子类对象
w1 = Worker('001', '张三', 2000, 160, 100)
s = w1.getSalary()
print('月薪是：', s)
print(w1)
