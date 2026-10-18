import random

def play_game():
    choices = ["石头", "剪刀", "布"]
    
    while True:
        user_choice = input("请出拳 (石头/剪刀/布) , 输入 '退出' 结束游戏:")
        
        if user_choice == "退出":
            print("游戏结束！")
            break
        
        if user_choice not in choices:
            print("无效的选择，请重新输入。")
            continue 
        
        computer_choice = random.choice(choices)
        print(f"电脑出拳: {computer_choice}")
        
        if user_choice == computer_choice:
            print("平局！")
        elif (user_choice == "石头" and computer_choice == "剪刀") or \
             (user_choice == "剪刀" and computer_choice == "布") or \
             (user_choice == "布" and computer_choice == "石头"):
            print("你赢了！")
        else:
            print("你输了！")

play_game()