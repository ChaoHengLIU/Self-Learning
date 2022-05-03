# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:57:29 2022

猜拳對戰

@author: Derek Liu
"""

def GAMES():
    """
    確認遊玩次數
    """
    
    TIMES = int(input("遊戲開始!請輸入欲遊玩回合數 → "))
    while TIMES <= 0 or TIMES > 10:
        TIMES = int(input("\n回合數只能介於1到10!請輸入欲遊玩回合數 → "))
    CHECK = int(input("您將與電腦遊玩" + str(TIMES) + "回合 確認請按 1 修改回合數請按 2 → "))
    while CHECK == 2:
        TIMES = int(input("\n請輸入欲遊玩回合數 → "))
        while TIMES <= 0 or TIMES > 10:
            TIMES = int(input("\n回合數只能介於1到10!請輸入欲遊玩回合數 → "))
        CHECK = int(input("您將與電腦遊玩" + str(TIMES) + "回合 確認請按 1 修改回合數請按 2 → "))
    
    """
    玩家出拳
    """
    
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
    
    """
    檢測是否繼續遊戲
    """
    
    print("您贏了" + str(VICTORY) + "次! 電腦贏了" + str(LOSS) + "次!")
    TIMES2 = TIMES
    TIMES2 = (TIMES2 // 2)
    TIMES = (TIMES - 1)
    
    while TIMES != 0 and TIMES2 >= VICTORY and TIMES2 >= LOSS:
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
        TIMES = (TIMES - 1)
    
    if VICTORY > LOSS:
        print("您總共贏了" + str(VICTORY) + "次! 電腦總共贏了" + str(LOSS) + "次! !!!恭喜獲勝!!!")
    if VICTORY < LOSS:
        print("您總共贏了" + str(VICTORY) + "次! 電腦總共贏了" + str(LOSS) + "次! !!!再接再厲!!!")
    if VICTORY == LOSS:
        print("您總共贏了" + str(VICTORY) + "次! 電腦總共贏了" + str(LOSS) + "次! !!!平手!!!")
GAMES()
AGAIN = int(input("\n是否繼續遊玩? 是請按 1 否請按 2 → "))
while AGAIN == 1:
    GAMES()
    AGAIN = int(input("\n是否繼續遊玩? 是請按 1 否請按 2 → "))
if AGAIN == 2:
    input("\n遊戲結束!請按ENTER鍵離開")
    pass