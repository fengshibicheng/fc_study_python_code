# num = 1
# while num <= 100:
#     print('*', end=' ')
#     if num % 10 == 0:
#         print('')
#     num +=1

# num = 1
# while num <= 100:
#     if num%2 ==1:
#         print('*', end=' ')
#     else:
#         print('&', end=' ')
#
#     if num % 10 == 0:
#         print('')
#     num +=1

num = 0
while num < 100:

    if num // 10 % 2 == 0:
        print('&', end=' ')
    else:
         print('*', end=' ')

    if num % 10 == 9:
        print('')
    num += 1
''' 隔一行换一个形状
& & & & & & & & & & 
* * * * * * * * * * 
& & & & & & & & & & 
* * * * * * * * * * 
& & & & & & & & & & 
* * * * * * * * * * 
& & & & & & & & & & 
* * * * * * * * * * 
& & & & & & & & & & 
* * * * * * * * * * 
'''