import os
filename = 'student.txt'

def search():
    student_query = []
    while True:
        id = '' #定义一个空字符串'id'变量
        name = '' #定义一个空字符串'name'变量
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按姓名查找请输入2:')
            if mode == '1':
                id = input('请输入学生ID:')
            elif mode == '2':
                name = input('请输入学生姓名:')
            else:
                print('您的输入有误，请重新输入！！！')
                search()
            with open(filename,'r',encoding='UTF-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item)) #使用eval函数将item变为字典变量
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            rfile.close()
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否继续查询？y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return
def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！！！')
        return
    #定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    #定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('Python'),
                                 item.get('Java'),
                                 int(item.get('english')) + int(item.get('Python')) + int(item.get('Java'))
                                 ))
