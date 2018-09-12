#!/usr/bin/env python
# _*_ coding:utf-8 _*_


'''
规则：
石头赢剪刀
剪刀赢布
布赢石头
实现：

1.系统随机出一个数(0,1,2)，分别代表石头，剪刀，布

2.用户输入一个数(0,1,2),分别代表石头，剪刀，布

3.将随机数与用户所输入的数相比较

4.注意用户输入的数只能为(0,1,2),不可输错。
'''


import random
print("规则如下:\n石头(0),剪刀(1),布(2)")
while True:
    ran_num = random.randrange(0, 3)   # 系统所出的手势
    user_num = int(input("请输入你的手势："))
    if user_num not in (0, 1, 2):
        print('输入不符合规则，请重新输入!')
    else:
        if (user_num == 0 and ran_num == 1) or (user_num == 1 and ran_num == 2) or (user_num == 2 and ran_num == 0):
            print("哎哦，你赢了!")
            if input("还想来吗?yes or no:") == 'no':
                break
        elif (user_num == 0 and ran_num == 2) or (user_num == 1 and ran_num == 0) or (user_num == 2 and ran_num == 1):
            print("哈哈哈，你输了，哼~")
            if input("还想来吗?yes or no:") == 'no':
                break
        else:
            print("平局，别跑再来!")
            if input("还想来吗?yes or no:") == 'no':
                break
print("退出成功")
