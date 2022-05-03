# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:53:42 2022

猜拳遊戲

@author: Derek LIU

"""

print ("遊戲開始!")
player = int(input("\n請出拳:剪刀按 1 石頭按 2 布按 3 → "))

if player == 1:
        print("\n您出了剪刀!")
if player == 2:
        print("\n您出了石頭!")
if player == 3:
        print("\n您出了布!")

import random
PC = int(random.randint(4, 6))

VICTORY = 0
LOSS = 0

"""
玩家出剪刀
"""

if player == 1 and PC == 4:
    print("電腦出了剪刀!\n平手!")
if player == 1 and PC == 5:
    print("電腦出了石頭!\n您輸了!")
    LOSS = LOSS + 1
if player == 1 and PC == 6:
    print("電腦出了布!\n您獲勝了!")
    VICTORY = VICTORY + 1

"""
玩家出石頭
"""

if player == 2 and PC == 4:
    print("電腦出了剪刀!\n您獲勝了!")
    VICTORY = VICTORY + 1
if player == 2 and PC == 5:
    print("電腦出了石頭!\n平手!")
if player == 2 and PC == 6:
    print("電腦出了布!\n您輸了!")
    LOSS = LOSS + 1

"""
玩家出布
"""

if player == 3 and PC == 4:
    print("電腦出了剪刀!\n您輸了!")
    LOSS = LOSS + 1
if player == 3 and PC == 5:
    print("電腦出了石頭!\n您獲勝了!")
    VICTORY = VICTORY + 1
if player == 3 and PC == 6:
    print("電腦出了布!\n平手!")

print("您贏了" + str(VICTORY) + "次! 電腦贏了" + str(LOSS) + "次!")

AGAIN = int(input("\n是否繼續遊玩? 是請按 1 否請按 2 → "))

while AGAIN == 1:
    player = int(input("\n請出拳:剪刀按 1 石頭按 2 布按 3 → "))

    if player == 1:
        print("\n您出了剪刀!")
    if player == 2:
        print("\n您出了石頭!")
    if player == 3:
        print("\n您出了布!")

    import random

    PC = int(random.randint(4, 6))
    """
    玩家出剪刀
    """

    if player == 1 and PC == 4:
        print("電腦出了剪刀!\n平手!")
    if player == 1 and PC == 5:
        print("電腦出了石頭!\n您輸了!")
        LOSS = LOSS + 1
    if player == 1 and PC == 6:
        print("電腦出了布!\n您獲勝了!")
        VICTORY = VICTORY + 1

    """
    玩家出石頭
    """

    if player == 2 and PC == 4:
        print("電腦出了剪刀!\n您獲勝了!")
        VICTORY = VICTORY + 1
    if player == 2 and PC == 5:
        print("電腦出了石頭!\n平手!")
    if player == 2 and PC == 6:
        print("電腦出了布!\n您輸了!")
        LOSS = LOSS + 1

    """
    玩家出布
    """

    if player == 3 and PC == 4:
        print("電腦出了剪刀!\n您輸了!")
        LOSS = LOSS + 1
    if player == 3 and PC == 5:
        print("電腦出了石頭!\n您獲勝了!")
        VICTORY = VICTORY + 1
    if player == 3 and PC == 6:
        print("電腦出了布!\n平手!")

    print("您贏了" + str(VICTORY) + "次! 電腦贏了" + str(LOSS) + "次!")
    AGAIN = int(input("\n是否繼續遊玩? 是請按 1 否請按 2 → "))
if AGAIN == 2:
    input("\n遊戲結束!請按ENTER鍵離開")
pass