#coding: UTF-8
# Author - 袁骏涛和家人共同完成

import time # 让程序停止
import os, subprocess
from colorama import init,Fore,Back,Style  # 导入颜色模块

init(autoreset=True)    # 初始化Colorama

class Light:
    # 构造函数
    def __init__(self):
        # 定义light列表
        self.light = []
        # 自动初始化
        self.prepare_light()

    def prepare_light(self):
        # 准备50行40列2000个灯
        for row in range(50):
            temp = [] # 每行40个
            for col in range(40):
                # 每一列的灯默认不亮
                temp.append(False)
            # 把每行的40个插入到light集合中
            self.light.append(temp)

class TrafficLight:
    # 构造函数
    def __init__(self,green_time,yellow_time,red_time):
        self.green_time = green_time    # 绿灯的时间
        self.yellow_time = yellow_time  # 黄灯的时间
        self.red_time = red_time    # 红灯的时间

        self.number01 = Light() # 显示第一个数字的电子屏
        self.number02 = Light() # 显示第二个数字的电子屏

    def bulid_LED_number(self,char:str):
        """
        根据提供的数字来构建电子屏上的数字显示
        数字显示设计为 - 横五竖六；并且每块电子屏幕的上、下、左各边空格行列数为5, 12, 5
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        :param char:提供的数字
        :return:返回构建的电子屏
        """
        temp_LED = Light()  # 新建一个电子屏屏幕，并定义显示的数字矩阵
        if char == "0":
            for row in range(50):
                for col in range(40):
                    if 4 < row < 10 and col > 11 : # 第0行到第4行共5行中的元素都点亮
                        temp_LED.light[row][col] = True
                    if 45 > row > 39 and col > 11: # 第45行到第49行共5行中的元素点亮
                        temp_LED.light[row][col] = True
                    if 11 < col < 18 and 45 > row > 4: # 第0列到第5列共6列中的元素点亮
                        temp_LED.light[row][col] = True
                    if col > 33 and 45 > row > 4: # 第34列到第39列共6列中的元素点亮
                        temp_LED.light[row][col] = True
        # 将上、下、左边各向内缩进两行

        elif char == "1":
            for row in range(50):
                for col in range(40):
                    if 4 < row < 45 and col > 33: # 第34列到第39列共6列中的元素点亮
                        temp_LED.light[row][col] = True
        # 将上、下边各向内缩进两行

        elif char == "2":
            for row in range(50):
                for col in range(40):
                    if 4 < row < 10 and col > 11:  # 第0行到第4行共5行中的元素都点亮
                        temp_LED.light[row][col] = True
                    if 4 < row <22 and col > 33:
                        temp_LED.light[row][col] = True
                    if 21 < row < 27 and col > 11: # row == 22 or row == 23 or row == 24 or row == 25 or row == 26:
                        temp_LED.light[row][col] = True
                    if 45 > row > 26 and 11 < col < 18:
                        temp_LED.light[row][col] = True
                    if 45 > row > 39 and col > 11:
                        temp_LED.light[row][col] = True

        elif char == "3":
            for row in range(50):
                for col in range(40):
                    if (4 < row < 10 and col > 11) or (45 > row > 39 and col > 11):
                        temp_LED.light[row][col] = True
                    if  22 <= row <= 26 and col > 11:  #row == 22 or row == 23 or row == 24 or row == 25 or row == 26: 注意此处写法等同于line69#写法
                        temp_LED.light[row][col] = True
                    if col > 33 and 4 < row < 45 :
                        temp_LED.light[row][col] = True

        elif char == "4":
            for row in range(50):
                for col in range(40):
                    if (row == 22 or row == 23 or row == 24 or row == 25 or row == 26) and col > 11:  #### 注意这个写法。。。
                        temp_LED.light[row][col] = True
                    if 11 < col < 18 and 4 < row < 22:
                        temp_LED.light[row][col] = True
                    if col > 33 and 45 > row > 4 :
                        temp_LED.light[row][col] = True

        elif char == "5":
            for row in range(50):
                for col in range(40):
                    if (4 < row < 10 and col > 11) or (45 > row > 39 and col > 11):
                        temp_LED.light[row][col] = True
                    if (row == 22 or row == 23 or row == 24 or row == 25 or row == 26) and col > 11:
                        temp_LED.light[row][col] = True
                    if 11 < col < 18 and 4 < row < 22:
                        temp_LED.light[row][col] = True
                    if col > 33 and 45 > row > 26:
                        temp_LED.light[row][col] = True

        elif char == "6":
            for row in range(50):
                for col in range(40):
                    if (4 < row < 10 and col > 11) or (45 > row > 39 and col > 11):
                        temp_LED.light[row][col] = True
                    if (row == 23 or row == 24 or row == 25 or row == 26 or row == 27) and col > 11:
                        temp_LED.light[row][col] = True
                    if 11 < col < 18 and 4 < row < 45 :
                        temp_LED.light[row][col] = True
                    if col > 33 and 45 > row > 27 :
                        temp_LED.light[row][col] = True

        elif char == "7":
            for row in range(50):
                for col in range(40):
                    if 4 < row < 10 and col > 11 :
                        temp_LED.light[row][col] = True
                    if col > 33 and 4 < row < 45:
                        temp_LED.light[row][col] = True

        elif char == "8":
            for row in range(50):
                for col in range(40):
                    if (4 < row < 10 and col > 11) or (45 > row > 39 and col > 11):
                        temp_LED.light[row][col] = True
                    if (row == 22 or row == 23 or row == 24 or row == 25 or row == 26) and col > 11:
                        temp_LED.light[row][col] = True
                    if (11 < col < 18  or col > 33) and 4 < row < 45: # row 重叠部分重复涂色，并没有增加色差！！！
                        temp_LED.light[row][col] = True

        elif char == "9":
            for row in range(50):
                for col in range(40):
                    if (4 < row < 10 and col > 11) or (45 > row > 39 and col > 11):
                        temp_LED.light[row][col] = True
                    if 6 < row < 22 and 11 < col < 18:
                        temp_LED.light[row][col] = True
                    if (row == 22 or row == 23 or row == 24 or row == 25 or row == 26) and col > 11:
                        temp_LED.light[row][col] = True
                    if col > 33 and 4 < row < 45:
                        temp_LED.light[row][col] = True
        # 返回这个LED
        return temp_LED

    def print_LED(self,color:str):
        for row in range(50):
            # 打印第一个数字
            for col01 in range(40):
                if self.number01.light[row][col01] == True:
                    if color == "green":
                        # print(Fore.GREEN + "○",end="")
                        print(Fore.GREEN + Back.GREEN + "袁",end="") # print函数默认换行，是end='\n'在起作用, 定义end=“”可以使打印的字符并列显示
                    elif color == "yellow":
                        # print(Fore.YELLOW + "○", end="")
                        print(Fore.YELLOW + Back.YELLOW + "骏", end="")
                    elif color == "red":
                        # print(Fore.RED + "○", end="")
                        print(Fore.RED + Back.RED + "涛", end="")
                else:
                    print(Fore.BLACK + "空",end="")
            print("\t",end="")  # 两个数字之间的空格 \t 代表的是制表符，表示空四个字符，也称缩进，就是按一下Tab键

            # 打印第二个数字
            for col02 in range(40):
                if self.number02.light[row][col02] == True:
                    if color == "green":
                        # print(Fore.GREEN + "○", end="")
                        print(Fore.GREEN + Back.GREEN + "袁" , end="")
                    elif color == "yellow":
                        # print(Fore.YELLOW + "○", end="")
                        print(Fore.YELLOW + Back.YELLOW + "骏", end="")
                    elif color == "red":
                        # print(Fore.RED + "○", end="")
                        print(Fore.RED + Back.RED + "涛", end="")
                else:
                    print(Fore.BLACK + "空", end="")
            # 换行
            print()

    def start_display(self,number:int,color:str):
        """
        把传递过来的数字用指定的颜色打印
        :param number: 指定的数字
        :param color: 指定的颜色
        :return: 无返回值
        """
        # 把数字格式化
        number_str = "%02d" % number # python格式化输出， 表示输出宽度为2的字符串，如果number的宽度不够，则左边补0
        # 构建LED上显示的两个数字
        # 第一块电子屏
        self.number01 = self.bulid_LED_number(number_str[0])
        # 第二块电子屏
        self.number02 = self.bulid_LED_number(number_str[1])
        # 在电子屏上展示
        self.print_LED(color)

    def start(self):
        """
        开始红绿灯的倒计时
        """
        while True:
            # 默认一直循环下去
            for number in range(self.green_time,-1,-1): # green_time-开始时间；-1 - 结束时间为 0 而不是-1 ，-1 - 每次按步长为1递减
                os.system("cls")  # 清屏(windows中换为cls)
                print()
                self.start_display(number,"green")  # 调用函数开始用特定的颜色打印
                # print(Fore.GREEN + "%02d" % number)    # 这里的2表示占用两个宽度，如果不够宽度，前面补零
                time.sleep(1)

            # 黄灯
            for number in range(self.yellow_time,-1,-1):
                os.system("cls")
                print()
                self.start_display(number, "yellow")
                # print(Fore.YELLOW +"%02d" % number)
                time.sleep(1)

            # 红灯
            for number in range(self.red_time,-1,-1):
                os.system("cls")
                print()
                self.start_display(number, "red")
                # print(Fore.RED + "%02d" % number)
                time.sleep(1)

    def input_time(color:str):
        while True:
            time = ""
            # 根据颜色提醒输入
            if color.lower() == "green":
                time = input(Fore.GREEN + " Input a pass time for the Green Light: ")
            if color.lower() == "yellow":
                time = input(Fore.YELLOW + " Input a warming time for the Yellow Light: ")
            if color.lower() == "red":
                time = input(Fore.RED + " Enter a waiting time for the Red Light: ")
            # 校验输入的是否符合要求：数字、正数、1-99
            # 如果不符合要求怎么处理：1. 出现异常，系统退出，报错；2.提醒重新输入
            if not time.isdigit(): # 验证time是否为数字类型，python类型检测方法
                print(u"验证输入的数字！因为是两块电子屏，输入的数字应该在1~99之间")
                continue    # 结束当前循环
            else:
                time_number = int(time)
                if time_number < 1 or time_number > 99:
                    print(u"输入的值不符合要求！输入的数字应该在1~99之间")
                    continue
                else:
                    # 符合要求
                    return time_number

if __name__ == '__main__':
    # 输入红绿黄灯的时间
    green_time = TrafficLight.input_time("green")
    yellow_time = TrafficLight.input_time("yellow")
    red_time = TrafficLight.input_time("red")
    # 实例化
    lello = TrafficLight(green_time, yellow_time, red_time)
    # 开始倒计时
    lello.start()
