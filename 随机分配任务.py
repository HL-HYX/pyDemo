#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 随机分配工作
"""
规则:
一个学校有八个老师，三个办公室，编写程序完成随机分配

实现:
[[1], [2], [3]]    1,2,3,4,5,6,7,8随机放到1,2,3里面

随便抽一个老师，然后往办公室里面塞

每个办公室只能至少装俩个人

0 0 8
0 1 7
0 2 6
0 3 5
0 4 4
1 1 6
1 2 5
1 3 4
2 2 4
2 3 3
"""
import random   # 导入random模块

# 分配老师
classRoom = [[], [], []]  # 全部教室
Max = []
Min_1 = []
Min_2 = []
teacher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # 老师人数
i, j, k, f = 0, 0, 0, 0
while True:
    classRoomNum = random.randrange(0, 3)
    classRoom[classRoomNum].append(teacher[i])
    i += 1
    if i == teacher.__len__():
        break

# 经过调整，使每个教室的老师个数不低于2个人
for temp in classRoom:
    if temp.__len__() < 2:  # 判断是否有低于2个老师的教室
        for tempNum in classRoom:
            if tempNum.__len__() > 3:
                Max = tempNum      # 将人数最多的教室里面的老师转移到Max，便于以后的调整
            elif tempNum.__len__() < 2 and k == 0:
                Min_1 = tempNum
                k += 1
            elif tempNum.__len__() < 2 and k == 1:   # 如果有2个教室里面的老师人数都低于2人，则执行此操作
                Min_2 = tempNum
                k += 1
            else:
                continue
        j = 0
        # 将Max,Min_1(和Min_2)里面的老师进行调整
        while k == 2:
            if Min_1.__len__() >= 2 and Min_2.__len__() >= 2:
                break
            elif Min_1.__len__() < 2:
                Min_1.append(Max[classRoomNum])
                del Max[classRoomNum]
            elif Min_2.__len__() < 2:
                Min_2.append(classRoomNum)
                del Max[classRoomNum]
        while k == 1:
            if Min_1.__len__() >= 2:
                break
            Min_1.append(Max[classRoomNum])
            del Max[classRoomNum]

# 输出每个办公室老师信息
for tempNum in classRoom:
    print("第%d个办公室的老师有:" % (f+1))
    for temp in tempNum:
        print(temp, end='  ')
    print("\n")
    f += 1
