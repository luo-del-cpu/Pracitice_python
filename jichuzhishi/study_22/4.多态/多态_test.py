# @Time : 2025/2/21 00:41
# @Author : luoxin
# 父类 Animal
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# 子类 Dog
class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

# 子类 Cat
class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")

# Tiger 类（没有继承自 Animal）
class Tiger:
    def speak(self):
        print("ooo! ooo!")

# 使用多态
def animal_speak(animal: Animal):
    animal.speak()  # 统一调用 speak 方法

# 创建对象
dog = Dog()
cat = Cat()
tiger = Tiger()

# 调用相同的方法，但不同对象表现不同
animal_speak(dog)    # 输出: Woof! Woof!
animal_speak(cat)    # 输出: Meow! Meow!
animal_speak(tiger)
