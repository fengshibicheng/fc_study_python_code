counter = 100        # 整型变量
miles   = 1000.0     # 浮点型变量
name    = "runoob"   # 字符串

print(counter)
print(miles)
print(name)

print({x: x**2 for x in (2, 4, 6)})

char = "hello world"
print("更新后的语句为：", char[:6] + "runoob")

x = lambda a: a + 10
print(x(10))

sum = lambda arg1, arg2: arg1 + arg2
print(sum(15, 30))

numbers = [1, 2, 3, 4, 5]
print("映射的列表为：", list(map(lambda x: x**2, numbers)))

print("筛选的偶数列表为：", list(filter(lambda x: x % 2 == 0, numbers)))