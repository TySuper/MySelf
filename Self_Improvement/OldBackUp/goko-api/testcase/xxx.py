# -*- coding: utf-8 -*-

"""
清明同学的学号为首字母大写且只含有字母与数字组成的长度为8的字符串，
他的成绩书纯数字且小于100，并且得知清明同学今年的成绩比去年有所提升，
请从下列字符串中找到清明同学的学号，清明同学去年的成绩，今年的成绩，成绩提升的百分点，并用字符串格式化显示出‘xx.x%’。
如最终打印结果    清明的学号为：.....，
去年的成绩为：......，今年的成绩为：.......，
成绩提升的百分点为：xx.x%    双击执行程序后可以查看到输出结果。
字符串：sma12 34,Ak‘12345,123snm,5 9,67,AK1234567,123,87,Ak234567\n
"""
student_str = "sma12 34,Ak‘12345,123snm,5 9,67,AK1234567,123,87,Ak234567\n"
list_str = student_str.split(",")
import time


def if_student_number(list_str):
    """判断学生的学号"""
    for i in list_str:
        # i.replace(" ", '')  # 将所有空格取消
        i = i.strip()  # 去除换行符
        if i.istitle() and len(i) == 8 and i.isalnum():
            if not i.isdigit() and not i.isalpha():
                print("清明同学的学号: %s" % i)


def if_student_score(list_str):
    """判断学生的成绩"""
    score = []
    for i in list_str:
        i = i.strip()  # 去除换行符
        if i.isdigit() and int(i) < 100:
            score.append(i)
        bubble_sort(score)
    print("去年的成绩为：%s " % score[0])
    print("今年的成绩为：%s " % score[1])
    res = int(score[1])-int(score[0])
    res = res / int(score[0])
    res = '%.1f%%' % (res * 100)
    print("成绩提升的百分点为：%s" % res)


def bubble_sort(nums):
    """将成绩排序"""
    for i in range(len(nums) - 1):
        ex_flag = False
        for j in range(len(nums) - i - 1):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                ex_flag = True
        if not ex_flag:
            return nums
    return nums


if_student_number(list_str)
if_student_score(list_str)

time.sleep(10)
