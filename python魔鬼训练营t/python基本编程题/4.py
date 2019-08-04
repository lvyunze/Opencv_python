# # 获得输入正整数N，反转输出该正整数，不考虑异常情况
# # N = int(input("请输入N:"))
# # print(reversed(N))
#
#
# # N = input()
# # print(N[::-1])
#
# # 给定一个数字123456，请用宽度为25、右对齐的方式打印输出，使用"+"填充
# # 注意使用format的使用使用的符号是.而不是,
# print("{:+>25}".format(123456))
#
#
# # 给定一个整数数字0X1010，请依次输出Python语言中的十六进制、十进制、八进制和二进制表示形式
# # 使用英文的逗号分隔
# # 0表示的是位置，要是没有0，后面的format中只有一个，不够填充
# print("0x{0:x},{0},0o{0:o},0b{0:b}".format(0x1010))
#
# # 获得用户输入的一个字符串，输出其中全部小写形式
# x=input("请输入字符串")
# print(x.lower())
# # 获得用户输入的一个字符串，输出其中全部大写形式
#
# y=input("请输入字符串")
# print(y.upper())
# print(y.capitalize())
# print(y.title())

# 獲得用戶輸入的字符串，輸出其中字母a的個數
# m=input("請輸入字符串：")
# n=0
# for i in m:
#     if i=='a':
#        n+=1
# print(n)
# 可以取而代之的是使用count
# n=input("请输入字符串")
# print(n.count("a"))

# 如下函数返回两个数的平方和
# def psum(a,b):
#     return  a**2+b**2
# print(psum(2,3))
# import jieba
# # txt="中华人民共和国教育部考试中心委托专家制定了全国计算机等级考试二级程序设计考试大纲"
# # # txt="中国是一个伟大的国家"
# # ls=jieba.lcut(txt,cut_all=True)
# # # ['中华人民共和国', '教育部考试中心', '委托', '专家', '制定', '了', '全国', '计算机',
# # # '等级', '考试', '二级', '程序设计', '考试', '大纲']
# # print(ls)

from turtle import *

color('red', 'pink')
begin_fill()
# 逆时针移动135度
left(135)
fd(100)
right(180)
circle(50, -180)
left(90)
circle(50, -180)
right(180)
fd(100)
end_fill()
hideturtle()
done()
