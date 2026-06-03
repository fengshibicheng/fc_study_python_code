
'''
斐波那契数列为： 0,1,1,2,3,5,8,13,21....
'''
num = int(input('请输入你需要计算的位数？'))

n1 = 0
n2 = 1
i = 2

if num < 1:
    print('输入数据错误，请输入大于等于1的数')
elif num == 1:
    print(f'你需要的斐波那契数列为：{n1}')
else :
    print(f'你需要的斐波那契数列为：{n1}, {n2},', end='')
    while i <= num:
        n3 = n1 + n2
        print(f'{n3},', end='')
        n1, n2 = n2, n3
        i +=1

