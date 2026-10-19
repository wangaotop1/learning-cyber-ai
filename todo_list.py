my_tasks = []

my_tasks.append("C语言学习")
my_tasks.append("Python学习")
my_tasks.append("kali学习")

print(f"有{len(my_tasks)}个任务")

for task in my_tasks:
    print(f"任务: {task}")
    
my_tasks.remove("C语言学习")
print("\n删除C语言学习后:")
for task in my_tasks:
    print(my_tasks)
    
print("\n前两项任务:", my_tasks[0:2])  