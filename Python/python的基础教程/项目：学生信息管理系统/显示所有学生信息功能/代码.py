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
