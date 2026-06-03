def reapt(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@reapt(3)
def say_hello():
    print("Hello!")

say_hello()

name = "菜鸟教程"
www = "http://www.runoob.com"
print(f"网站名字是{name}, 对应的网址为：{www}")
