import os
filename = 'student.txt'
def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存过数据')
    answer = input('选择返回主页面y/n\n')
    if answer == 'y':
        return
    else:
        show()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTF-8') as rfile:
            student_list=rfile.readlines()
        student_new=[]
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)
            rfile.close()
    else:
        return print('未储存学生信息！！！')
    asc_or_desc=input('请选择(0.升序 1.降序):')
    if asc_or_desc == '0':
        asc_or_desc = False
    elif asc_or_desc == '1':
        asc_or_desc = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode = input('请选择排序方式(1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 4.按总成绩排序)'
                 ':')
    if mode == '1':
        student_new.sort(key=lambda x : int(x['english']), reverse=asc_or_desc)
    elif mode == '2':
        student_new.sort(key=lambda x : int(x['Python']), reverse=asc_or_desc)
    elif mode == '3':
        student_new.sort(key=lambda x : int(x['Java']), reverse=asc_or_desc)
    elif mode == '4':
        student_new.sort(key=lambda x : int(x['english']) + int(x['Java']) + int(x['Python']), reverse=asc_or_desc)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)
    answer = input('是否继续查询: y/n\n')
    if answer == 'y' :
        sort()
    else:
        return

def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！！！')
        return
    #定义标题显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容的显示格式
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('Python'),
                                 item.get('Java'),
                                 int(item.get('english'))+int(item.get('Python'))+int(item.get('Java'))
                                 ))
