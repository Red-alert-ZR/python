import os
filename='student.txt'

def modify():
    #show()  #之后会添加show()模块
    if os.path.exists(filename):
        with open(filename,'r',encoding='UTF-8') as rfile:
            student_old=rfile.readlines()
    else:
        return print('未找到学生信息')
    student_id=input('请输入要修改的学员的ID:')
    with open(filename,'w',encoding='UTF-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_id:
                print('找到学生信息了，可以修改他的信息了！！')
                while True:
                    try:
                        d['name']=input('请输入姓名:')
                        d['english']=input('请输入英语成绩:')
                        d['Python']=input('请输入Python成绩:')
                        d['Java']=input('请输入Java成绩:')
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功！！！')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改其他学生信息？y/n\n')
        if answer=='y':
            modify()
