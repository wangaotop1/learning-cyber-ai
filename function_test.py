def calculate_average(score1, score2, score3):
    total = score1 +score2 + score3
    average = total / 3
    return average

my_avg = calculate_average(80,90,100)
print(f"我的平均分是： {my_avg}")

your_avg = calculate_average(60,70,80)
print(f"你的平均分是： {your_avg}")
