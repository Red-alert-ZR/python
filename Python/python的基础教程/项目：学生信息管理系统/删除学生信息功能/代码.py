import os 
filename='student.txt'

def delete():
    while True:
        student_id = input('请输入要删除的学生的ID:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='UTF-8') as file:
                    student_old=file.readlines()
            else:
                student_old = []
            flag = False #标记是否删除
            if student_old:
                with open(filename,'w',encoding='UTF-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item)) #将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                            wfile.close()
                        else:
                            flag=True
                    if flag:
                        print('id为{}的学生信息已被删除'.format(student_id))
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()      #删除之后要重新显示学生信息
            answer=input('是否继续删除？y/n\n')
            if answer=='y':
                continue
            else:
                break
