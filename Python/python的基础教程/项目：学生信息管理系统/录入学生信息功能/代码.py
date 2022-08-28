    filename='student.txt'
    
    def insert():
        student_list=[]
        while True:
            id=input('请输入id(如1001):')
            if not id:
                break
            name=input('请输入姓名:')
            if not name:
                break
            try:
                english=int(input('请输入英语成绩:'))
                Python=int(input('请输入Python成绩'))
                Java=int(input('请输入Java成绩'))
            except:
                print('输入无效，不是整数类型，请重新输入:')
                continue
            #将录入的学生信息保存到字典当中
            student={'id':id,'name':name,'english':english,'Python':Python,'Java':Java}
            #将学生信息添加到列表之中
            student_list.append(student)
            answert=input('是否继续添加？y/n\n')
            if answert=='y':
                continue
            else:
                break
        #调用save()函数
        save(student_list)
        print('学生信息录入完毕！！！')
    def save(lst):
        try:
            stu_txt=open(filename,'a',encoding='UTF-8')
        except:
            stu_txt=open(filename,'w',encoding='UTF-8')
        for item in lst:
            stu_txt.write(str(item) + '\n')
        stu_txt.close()
