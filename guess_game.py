import random  # 导入随机数模块

print("欢迎来到猜数字游戏！")
secret_number = random.randint(1, 100) # 生成一个 1 到 100 之间的随机整数
guess_count = 0

while True:
    try: # 增加一个错误处理，防止用户输入字母导致程序崩溃
        guess = int(input("请输入你猜的数字 (1-100): "))
        guess_count += 1 # 次数加1
        
        if guess < secret_number:
            print("太小了，再试一次！")
        elif guess > secret_number:
            print("太大了，再试一次！")
        else:
            print(f"🎉 恭喜你，猜对了！就是 {secret_number}！")
            print(f"你一共猜了 {guess_count} 次。")
            break # 猜对之后跳出循环，结束游戏
    except ValueError:
        print("输入无效，请输入一个整数！")

print("游戏结束，Bye~")