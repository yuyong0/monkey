# ---格式化练习题
# name="传智"  # 公司名
# stock_code="003032" # 股票代码
# stock_price=19.99 # 当前股价
# stock_price_daily_growth_factor= 1.2# 股票增长系数
# growth_days=7 # 增长天数
# print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
# print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days , stock_price*stock_price_daily_growth_factor**growth_days))

#  -----if、else判断——我要买票吗
# print("欢迎来到动物园！")
# print("请输入你的身高（cm）：" , sep='')
# num = int(input())
# if num > 120 :
#     print("您的身高超过120cm，进园游玩需要买票，十元一张，谢谢惠顾！")
# else:
#     print("您的身高没有超过120cm，可以免费进园游玩。")
# print("祝您玩的愉快！")

# ------if、elif、else组合——猜猜心里的数字
# if int(input("请输入第一次猜想的数字：")) == 10:
#     print("恭喜你，你猜对了！")
# elif int(input("你猜错了，再猜一次：")) == 10:
#     print("恭喜你，你猜对了！")
# elif int(input("你猜错了，再猜一次：")) == 10:
#     print("恭喜你，你猜对了！")
# else:
#     print("三次全猜错了，我猜的是：10 ^_^")

# if判断嵌套——猜猜我心里数字
# import random
# num =random.randint(1,10)  # 获取随机数
# if int(input("猜猜我心里想的数字:"))==num:
#     print("恭喜你，你猜对了！")
# else:
#     if int(input("你猜错了，再猜一次:"))==num:
#         print("恭喜你，你猜对了！")
#     else:
#         if int(input("你猜错了，再猜一次:"))==num:
#             print("恭喜你，你猜对了！")
#         else:
#             print(f"我心中的数字是：{num}")

# -----------while循环——求1——100的和
# i = 1
# j = 0
# while i <= 100 :
#     j += i
#     i += 1
# print(j)

# -------------while循环——猜一百以内随机数（提示大了小了直到猜中）
# import random
# num = random.randint(1,100)
# num1=0
# num2=0
# while num != num1:
#     num2 += 1
#     num1 = int(input(f"这是第{num2}次猜，请输入你所猜测的1-100的数字："))
#     if num > num1:
#         print("你猜的数字小了！")
#     else:
#         print("你猜的数字大了！")
# print(f"恭喜你，你第{num2}次猜对了，正确答案就是{num1} ^_^ !")

# -----------------------------while循环——输出九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i :
#         print(f"{j}*{i}={i*j}\t" , end='')  # \t 是输出的字符串对齐，end=’‘ 是去掉输出print的回车
#         j += 1
#     i += 1
#     print()

# -------------------------------------------for循环——九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}+{i}={i*j}\t",end="")
#     print()

# -------------------------------------------发工资——一共一万元，二十人，绩效分大于五，一人一千元，发完就不发了
# import random    # 练习
# money = 10000
# for i in range(1, 21):
#     num = random.randint(1, 10)
#     if num < 5:
#         print(f"员工{i}，绩效分{num}，低于五分，不发工资，下一位")
#         continue
#     else:
#         money -= 1000
#         print(f"向员工{i}发员工发工资1000元,账户余额还剩{money}元")
#     if money == 0:
#         print("工资发完了，下个月再领吧！")
#         break

# --------------------------------------- ATM
# money = 5000000
# name = "none"
# # 用户输入姓名
# name = input("请输入您的姓名：")
# # 主菜单
# def main():
#     print(f"-------------------主菜单-------------------\n"
#           f"{name}，您好，欢迎来到德玛西亚ATM机，请选择操作：\n"
#           f"查询余额\t[输入1]\n"
#           f"存款\t\t[输入2]\n"
#           f"取款\t\t[输入3]\n"
#           f"退出\t\t[输入4]")
#     return input("请输入您的选择：")
#
# # 查询余额
# def query_balance(bul):
#     if bul:
#         print(f"------------------查询余额-------------------")
#     print(f"{name}，您好，您的余额剩余：{money}元\n")
#
# # 存款
# def deposit(num):
#     global money
#     money += num
#     print(f"------------------存款-------------------"
#           f"{name},您好,您存款5000元成功\n")
#     query_balance(False)
#
# # 取款
# def withdraw_money(num):
#     global money
#     money -= num
#     print(f"------------------取款-------------------"
#           f"{name},您好,您取款5000元成功\n")
#     query_balance(False)
#
# while True:
#     keyboard_input = main()
#     if keyboard_input == "1":
#         query_balance(True)
#         continue
#     elif keyboard_input == "2":
#         deposit(int(input("请输入您要存的金额：")))
#         continue
#     elif keyboard_input == "3":
#         num = int(input("请输入您要取的金额："))
#         if num > money:
#             print(f"您的余额不足，您的余额为{money}元!")
#         else:
#             withdraw_money(num)
#         continue
#     else:
#         print("德玛西亚ATM机退出成功，希望您下次光临!")
#         break

# mylist = [21, 25, 21, 23, 22, 20]
# mylist.append(31)
# mylist.extend([29, 33, 30])
# print(mylist)
# print(f"mylist的第一个元素是：{mylist[0]}")
# print(f"mylist的最后一个元素是：{mylist[-1]}")
# print(f"元素31在列表中的下标为:{mylist.index(31)}")

# ---------------------------------------- list列表的遍历
# mylist =[1,2,3]
# i = 0
# while i < len(mylist):
#     print(mylist[i])
#     i += 1
#
# for i in mylist:
#     print(i)

