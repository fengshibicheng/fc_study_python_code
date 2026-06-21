# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/10
@Auth ： fc
@File ： 4.2 for.py
@IDE ： PyCharm
"""
# -*- coding: utf-8 -*-
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

users = {'hans': 'active', 'eleonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status =='active':
        active_users[user] = status
print(active_users)

for i in range(5):
    print(i)

a = ['marry', 'hard', 'a', "little", 'lamb']
for i in range(len(a)):
    print(i, a[i])

a = sum(range(10))
print('range（10）的求和结果为：',a)