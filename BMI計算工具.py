# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:33:20 2022

@author: Derek Liu

BMI計算工具
"""

Height = int(input("請輸入身高(公分):"))
Weight = int(input("請輸入體重(公斤):"))
BMI = ((Weight // (Height * Height / 100000)) / 10)
print("您的BMI值為:" + str(BMI))
if BMI >= 27:
    print("您的體重「超重」，需要立刻力行「健康體重管理」！")
if BMI < 27 and BMI >= 24:
    print("您的體重「過重」，要小心囉，趕快力行「健康體重管理」！")
if BMI < 24 and BMI >= 18.5:
    print("您的體重「正常」，要繼續保持！")
if BMI < 18.5:
    print("您的體重「過輕」，需要多運動，均衡飲食，以增加體能，維持健康！")
IDEAL_MAX = (((Height * Height / 100)*24) // 10)/10
IDEAL_MIN = (((Height * Height / 100)*18.5) // 10)/10
if BMI > 24 or BMI < 18.5:
    print("您的理想體重介於" + str(IDEAL_MIN) + "公斤到" + str(IDEAL_MAX) + "公斤")
input("\n按ENTER鍵離開")
pass