class father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dayin(self):
        print(f'这是一个实验，他叫{self.name}，今年{self.age}岁了')

class person(father):
    def __init__(self, name, age, pp):
        super().__init__(name, age)
        self.pp = pp

    def dayin1(self):
        print(f'打印{self.pp}')

if __name__ == "__main__":
    per = person('李华', 25, '测试')
    per.dayin()
    per.dayin1()



x = 1
try:
    print(x)
except:
    print('这是一个错误没有定义')