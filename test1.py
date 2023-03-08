# print("Hello World!")

"""name="yu"
age=22
print(type(age))"""

# num=1
# num+=1
# name='oooa'
# name1="""耦合"""
# name2=name+name1
# print("""name2="""+name2)

# --------------------类型转换
# print(int("10"))
# print(float("1.0000"))
# print(float(int(1.000)))

# ---------------------格式化
# name = "yy"
# print("格式化字符串，我是：%s" % "yu")  # 可以格式化字符串和变量
# print("格式化整数,0后面是%d" % 1)
# print("格式化浮点数,二十点一一一一一一=%f" % 20.111111111111111)  #  默认不能控制小数点后的位数，保留六位
# print("格式化浮点数，二十点一一=%7.3f" % 20.00) # 小数点算以为有效位数
# print(f'格式化字符串，我是{"yy"}')
# name="yy1"
# print(f"格式化变量,我叫{name}")
# age = 2+4*5
# print(f"格式化表达式,我的年纪是{age}")

# ------------------控制台输入用input
# print("1+1等于几")
# num=input()
# print(f"原来是等于{num}啊！")
# print(type(num))  #控制台输入的都会转为字符串类型

# --------------------循环
# num = 1     #for循环
# if num > 2 :
#     print("对了")
# else:
#     print("错了")


# ----------------------------------while循环嵌套  表白一百天，每天送十朵
# i = 0   # 自己练习，感觉比答案更好，但逻辑不太对
# j = 0
# while i < 100:
#     i += 1
#     j += 1
#     while j % 10 != 0:
#         print(f"第{i}天，送第{j}朵表白玫瑰")
#         j += 1
#     print(f"第{i}天，送第{j}朵表白玫瑰")
#     print("-------------------------------------------------------")
# print("恭喜你，你表白成功了！")

# i = 1     # 答案
# j = 0
# while i <= 100:
#     j = 1
#     while j <= 10:
#         print(f"第{i}天，送第{j}朵表白玫瑰")
#         j += 1
#     i += 1
#     print("-------------------------------------------------------")
# print("恭喜你，你表白成功了！")

# ------------------------------------for循环——数一数有多少个a
# name = " ithema is a brand of itcast "
# num_a=0
# for i in name:
#     if i == "a":
#         num_a += 1
# print(f"ithema is a brand of itcast ,中共含有：{num_a}个字母a")

# --------------------------------------range
# print(range(3))
# i = 0
# for i in range(2,5):
#     print(i)
# print(i)
#
# for i in range(1,10,2):
#     print(i)

# -------------------------------------------- for循环-向小美表白-表白一百天，每天十朵玫瑰花
# for x in range(1,101):
#     print(f"向小美表白的第{x}天")
#     for y in range(1,11):
#         print(f"第{x}天的第{y}枝玫瑰花")
# print("恭喜你，表白成功！")

# ---------------------------------函数

# ---------------------------------定义函数算字符串长度，函数
# def my_len(data):
#     conut = 0
#     for i in data:
#         conut += 1
#     print(f"字符串{data}的长度是{conut}")
#
# str1 = "qwerty"
# my_len(str1)

# def hesuan():
#     print("欢迎您的到来!\n请出示您的核算检测证明!")
# hesuan()
#
# def avg(i,j):
#     print(f"{i}和{j}相加，等于{i+j}")
#
# avg(3,2)

# def avg(i,j):
#     """
#     :param i:
#     :param j:
#     :return:
#     """
#     print(f"{i}和{j}相加，等于{i+j}")

# ---------------------------------------数据容器

# ----------------------------------------list（数组）
# num_list = [[1, 2, 3], [4, 5, 6]]
# print(num_list[1][1])

# -----------------------------------------list中的方法
# mylist = [1,2,3]        #修改
# addlist = [4,5,6]
# mylist.append(4)
# print(mylist)
# mylist1 = [1,2,3]
# mylist1.extend(addlist)
# print(mylist1)

# mylist = [1, 2, 3]      # 删除1
# del mylist[1]
# index = mylist.index(3)
# print(index)

# mylist = [1, 2, 3]      # 删除2,会取出并删除
# num = mylist.pop(0)
# print(mylist,num)

# ------------------------------------------- 元组
# t1 = ("哦豁", 22, ["football", "music"])
# print(f"年龄的下标是：{t1.index(22)}")
# print(f"姓名是：{t1[0]}")
# del t1[2][0]
# t1[2].insert(0, "coding")
# print(t1)

# --------------------------------------------- 字符串
# str = "yu yong"    # replace——字符串的替换
# str = str.replace("yong", "heng")
# print(str)

# str1 = "yu yong heng"  # split——字符串的分割
# str1 = str1.split( )
# print(str1)

# str2 = "12yu12yong21"  # strip——字符串的规整
# str2 = str2.strip("12")
# print(str2)

# str = "itheima itcast yuyong"
# print(f"it的数量为：{str.count('it')}")
# print(f"空格换|后：{str.replace(' ','|')}")
# print(f"按照空格分割后：{str.split()}")

# str = "万过薪月，员序程马黑来，nohtyP学"
# print(f"{str[::-1][9:14]}")
# print(f"{str[5:10][::-1]}")

# ------------------------------------------------ 集合
# s = set()
# mylist = ["y","u","y","o","n","g","y","U"]
# for i in mylist:
#     s.add(i)
# for j in s:
#     print(j)

# ------------------------------------------------- 字典
# mydict = {
#     "王力宏": {
#         "部门": "科技部",
#         "工资": "3000",
#         "级别": "1",
#     },
#     "周杰伦": {
#
#     }
# }
#PythonDraw.py
#coding=gbk

# ------------------------------------------------- 摸鱼

# from turtle import *
# import turtle
# #人
# color('red','red')
# turtle.setup(1000,700)
# turtle.circle(60)
# turtle.right(90)
# turtle.fd(150)
# turtle.right(40)
# turtle.fd(80)
# turtle.right(180)
# turtle.fd(80)
# turtle.right(50)
# fd(100)
# turtle.right(135)
# fd(80)
# penup()
# goto(0,-50)
# turtle.left(135)
# pendown()
# fd(100)
# turtle.left(45)
# fd(50)
# penup()
# goto(0,-80)
# turtle.right(45)
# pendown()
# fd(100)
# turtle.right(45)
# fd(50)
# penup()
# goto(-20,80)
# turtle.right(45)
# pendown()
# fd(30)
# penup()
# goto(20,80)
# pendown()
# fd(30)
#
# #爱心
# penup()
# goto(300,-150)
# pendown()
# turtle.left(90)
# def curvemove():
#     for i in range(200):
#         right(1)
#         fd(1)
# color('red','pink')
# begin_fill()
# left(140)
# fd(111.65)
# curvemove()
# left(120)
# curvemove()
# forward(111.65)
# end_fill()
# penup()
# goto(-15,30)
# pendown()
# turtle.left(55)
# turtle.circle(16, 180)
#
# #气球
# penup()
# goto(300,200)
# turtle.seth(0)
# pendown()
# begin_fill()
# color('red','red')
# turtle.circle(30)
# end_fill()
# turtle.right(90)
# for i in range(1):
#     turtle.circle(40, 80)
#     turtle.circle(-40, 80)
# turtle.left(90)
#
#
# penup()
# goto(220,50)
# turtle.write("模会儿鱼",move=False,align="left",font=("Arial",16,"normal"))
# turtle.hideturtle()
#
# done()

# # coding:utf-8
# import threading
# import time
#
# def job1():
#     print("T1 start")
#     for i in range(5):
#         time.sleep(1)
#         print(i)
#     print("T1 finish")
#
#
# def main():
#     # 新创建一个线程
#     new_thread = threading.Thread(target=job1, name="T1")
#     # 启动新线程
#     start = new_thread.start()
#     print("All done...")
#
#
# if __name__ == "__main__":
#     main()

