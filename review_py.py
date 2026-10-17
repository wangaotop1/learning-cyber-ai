print("进入年龄判断程序,输入 'q' 退出。")

while True:
  user_input = input("请输入你的年龄：")

  if user_input == 'q':
     print("程序已退出，再见!")
     break
  try: 
     age = int(user_input)

     if age <18:
        print("你是一名未成年人")

     elif age >=18 and age <60:
        print("你是一名成年人")

     else:
        print("你已进入老年")


  except ValueError:
        print("输入无效,请输入一个整数或'q'")
