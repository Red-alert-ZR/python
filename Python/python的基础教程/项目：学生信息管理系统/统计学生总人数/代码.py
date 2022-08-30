import os
filename = 'student.txt'
def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTF-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}多少名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息......')
    answer = input('是否继续y/n\n')
    if answer == 'y':
        total()
    else:
        return
