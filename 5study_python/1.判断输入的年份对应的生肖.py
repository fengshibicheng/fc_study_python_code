'''
这是一个注释

'''

year = int(input('请输入四位数的年份, 示例：2000：'))
n = year % 2000
sheng_xiao_list = ['子鼠', '丑牛', '寅虎', '卯兔', '辰龙', '巳蛇', '午马', '未羊', '申猴', '酉鸡', '戌狗', '亥猪']
print(sheng_xiao_list[n])