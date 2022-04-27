## 一.计算机组成原理  
#### 1输出函数print()
      #可以输出数字
      print(5)
      print(5.4)

      #可以输出字符串
      print('hello world')
      print("hello world")

      #含有运算符的表达式
      print(3+1)

      #将数据输出文件中
      fp = open('D:/text.txt', 'a+') #注意：1，所指定的盘符要存在
      print('hello world',file=fp) #2，使用file=fp
      fp.close()

      #不进行换行输出（输出内容在一行中）
      print('hello','world','Python')


#### 2转义字符与元字符 

      #转义字符
      print('hello\nworld') #\ +转移功能的首字母  n-->newline的首字符表示换行
      print('hello\tworld') #\t -->水平制表符
      print('helloooo\tworld')  #\t 为四个空格
      print('hello\rworld') #\r -->world将hello进行了覆盖
      print('hello\bworld') #\b -->退一个格，将o退没了

      print('http:\\\\www.baidu.com')
      print('老师说:\'大家好！\'')

      #原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r,或R
      print(r'hello\nworld')
      #注意事项，最后一个字符不能是\
      #print(r'hello\nworld\')


#### 3二进制与字符编码 
      print(chr(0b100111001011000))
      print(ord('乘'))


####  4Python中的标识符和保留字  
      import keyword
      #Python保留字
      print(keyword.kwlist)

      #Python标识符
      '''
      变量、函数、类、模块和其它对象的起的名字就叫标识符
      规则:
      可以是字母、数字、下划线_
      不能以数字开头
      不能是我的保留字
      严格区分大小写的
      '''
  

##  二.Python变量  ##
      #变量的定义和使用
      name = '玛丽亚'
      print(name)
      print('标识 ',id(name))
      print('类型 ',type(name))
      print('值   ',name)
      #变量的多次赋值
      name = '楚留冰'
      print(name)

### 1数据类型  ##
##### 整数类型 --> int -->98
##### 浮点数类型 --> float --> 3.141519
##### 布尔类型 --> bool --> True,False
##### 字符串类型 --> str --> '人生苦短，我用python'

#### 1.1整数类型
##### 可以表示，整数，负数，0
      n1 = 90
      n2 = -76
      n3 = 0
      print(n1,type(n1))
      print(n2,type(n2))
      print(n3,type(n3))
      #整数可以表示为二进制，八进制，十进制，十六进制
      print('十进制',118)
      print('二进制',0b10101111) #二进制以0b开头
      print('八进制',0o176) #八进制以0o开头
      print('十六进制',0x1EAF) #十六进制以0x开头

#### 1.2浮点类型
      a = 3.14159
      print(a,type(a))
      n1 = 1.1
      n2 = 2.2
      print(n1+n2)

      #解决浮点数相加出现的精度问题
      from decimal import Decimal
      print(Decimal('1.1')+Decimal('2.2'))

#### 1.3布尔类型
##### 用来表示真或者假的值
##### True表示真，False表示假
##### True --> 1 False --> 0
      f1 = True
      f2 = False
      print(f1,type(f1))
      print(f2,type(f2))

      #布尔值可以转化成整数计算
      print(f1+1) #2   1+1的结果为2
      print(f2+1) #0   1+0的结果为1

#### 1.4字符串类型
##### 字符串类型
##### 字符串又被称为不可变的字符序列
##### 可以使用单引号''双引号""三引号''''''或""""""来定义
##### 单引号和双引号定义的字符串必须在一行
##### 三引号定义的字符串可以分布在连续的多行
      str1 = '人生苦短，我用Python'
      str2 = "人生苦短，我用Python"
      str3 = '''人生苦短，
      我用Python'''
      str4 = """人生苦短，
      我用Python"""
      print(str1,type(str1))
      print(str2,type(str2))
      print(str3,type(str3))
      print(str4,type(str4))

#### 1.5数据类型转换
![image](https://user-images.githubusercontent.com/99107924/162921178-a9933ecd-f711-4c59-9d72-58b73c8850e0.png)     
      
      name = '张三'
      age = 20
      print(name,type(name),age,type(age)) #说明name与age的数据类型不同
      #print('我叫'+name+'，今年'+age+'岁') 当将str类型与int类型进行连接时，报错，解决方案:类型转换
      print('我叫'+name+'，今年'+str(age)+'岁') #将int类型通过str()函数转成了str类型

      print('------str()将其他类型装成str类型------')
      a = 10
      b = 198.8
      c = False
      print(type(a),type(b),type(c))
      print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

      print('------int()将其他的类型转int类型-------')
      s1 = '128'
      f1 = 98.7
      s2 = '32.21'
      ff = True
      s3 = 'Hello'
      print(type(s1),type(f1),type(s2),type(ff),type(s3))
      print(int(s1),type(s1))  #str转成int类型，字符串为 数字串
      print(int(f1),type(f1))  #float转成int类型，截取整数部分，舍掉小数部分
      #print(int(s2),type(s2)) #str转为int类型，报错，因为字符串为小数串
      print(int(ff),type(ff))  #bool转为int类型，True-->1,False-->0
      #print(int(s3),type(s3)) #str转为int类型时，字符串必须为数字串（整数），非数字串是不允许被转换的

      print('-------float()函数，将其他数据类型转成float类型')
      s1 = '128.98'
      s2 = '76'
      ff = True
      s3 = 'hello'
      i = 98
      print(type(s1),type(s2),type(ff),type(s3),type(i))
      print(float(s1),type(float(s1)))
      print(float(s2),type(float(s2)))
      print(float(ff),type(float(ff)))
      #print(float(s3),type(float(s3))) #字符串中的数据是非数字串，则不允许转换
      print(float(i),type(float(i)))

#### 2注释
##### 在代码中对代码的功能进行解释说明的标注性文字，可以提高代码的可读性
##### 注释的内容会被Python解释器忽略
##### 通常包括三种类型的注释
##### 单行注释->以"#"开头，直到换行结束
##### 多行注释->并没有单独的多行注释标记，将一对三引号之间的代码称为多行注释
##### 中文编码声明注释->在文件开头加上中文声明注释，用以指定源码文件的编码格式

      #coding:UTF-8
      #输入功能 （单行注释）
      print('hello')

      '''嘿嘿，
      我是
      多行注释哦'''

##  三.流程控制语句  ##
### 1Python的输出函数input()
#### 1.1input的高级使用
##### 从键盘录入两个整数，计算两个整数的和
      a = int(input('请输入一个加数：'))
      b = int(input('请输入另一个加数：'))
      #a = int(a) #将转换之后的结果存储到a中
      #b = int(b)
      print(type(a),type(b))
      print(a+b)
      
### 2Python的运算符
<img src="https://user-images.githubusercontent.com/99107924/163781347-de11782c-4cce-433f-bf5a-94e6b54ad781.png" width="600px" alt="Python运算符" />

***
***
***

#### 2.1运算符1_算术运算符
<img src="https://user-images.githubusercontent.com/99107924/163781371-83690916-31f7-4c36-b2f7-27ae7e3d9ee2.png" width="700px" alt="Python运算符" />

      print(1+1) #加法运算
      print(1-1) #减法运算
      print(2*4) #乘法运算
      print(1/2) #除法运算
      print(11//2) #整除运算
      print(11%2) #取余运算
      print(2**2) #幂运算
      print(9//4)
      print(-9//-4)
      print(-9//4)
      print(9//-4) #一正一负的整数公式，向下取整
      print(9%-4) # 公式 余数=被除数-除数*商 9-(-4)*(-3) --> 9-12 = -3
      print(-9%4) # (-9)-4*(-3) --> -9+12 = 3
***
#### 2.2运算符2_赋值运算符
<img src="https://user-images.githubusercontent.com/99107924/163786651-78430f87-78c6-45a8-926c-d910a39fe51a.png" width="650"/>

      
      print('------运算顺序从左到右---------')
      i=3+4
      print(i)
      print('--------支持链式赋值------------')
      a=b=c=20 #链式赋值
      print(a,id(a))
      print(b,id(b))
      print(c,id(c))
      print('----------支持参数赋值-----------')
      a=20
      a+=30 #相当于a=a+30
      print(a)
      a-=10 #相当于a=a-10
      print(a)
      a*=2 #相当于a=a*2
      print(a)
      print(type(a)) #float
      a/=3 #相当于
      print(a)
      print(type(a))
      a//=2
      print(a)
      print(type(a))
      a%=3
      print(a)
      print('-------支持系列解包赋值------------')
      a,b,c=20,30,40
      print(a,id(a),'\n',b,id(b),'\n',c,id(c))
      #左右变量的个数和值的个数必须对应
      print('--------交换两个变量的值------------')
      a,b=10,20
      print('交换之前:',a,b)
      #交换
      a,b=b,a
      print('交换之后:',a,b)
***
#### 2.3运算符3_比较运算符
<img src="https://user-images.githubusercontent.com/99107924/163789519-b7281225-1aa4-49c5-b6be-bed05c6dc9bb.png" width="650"/>

      print('比较运算符的结果为bool类型')
      a,b=10,20
      print("a>b吗？",a>b)
      print("a<b吗？",a<b)
      print("a<=b吗？",a<=b)
      print("a>=b吗？",a>=b)
      print("a==b吗？",a==b)
      print("a!=b吗？",a!=b)

      ''' 一个 = 称为赋值运算符
          两个 == 称为比较运算符
          一个变量由三部分组成：‘标识’，‘类型’，‘值’
          == 比较的是值还是标识呢？ 
          比较的是‘值’
          比较对象的标识，用的是 'is'
      '''
      a=10
      b=10
      print(a==b) #说明a与b的value相等
      print(a is b) #说明a与b的id标识也相等
      # 呵呵
      list1 = [11,22,33,44]
      list2 = [11,22,33,44]
      print(list1==list2) #value
      print(list1 is list2) #id
      print(id(list1),'\t',id(list2))
      print(a is not b)
      print(list1 is not list2)


#### 2.4运算符4_布尔运算符
<img src="https://user-images.githubusercontent.com/99107924/163823247-36b4f8f3-7722-45f8-9256-9014da6d2a70.png" width="650" />
      
      a,b=1,2
      print('-----------------and 并且----------------------')
      print(a==1 and b==2) #True   True and True --> True
      print(a==1 and b<2) #False  True and False --> False
      print(a!=1 and b==2) #False  False and True --> False
      print(a!=1 and b!=2) #False  False and False --> False
      
      print('--------------------or 或者--------------------')
      print(a==1 or b==2) #True   True or True --> True
      print(a==1 or b<2) #True  True or False --> True
      print(a!=1 or b==2) #True  False or True --> True
      print(a!=1 or b!=2) #False  False or False --> False

      print('-------------not 对bool类型的操作数取反-------------')
      f1=True
      f2=False
      print(not f1)
      print(not f2)

      print('-------------------in 与 not in  ---------------------------')
      s='Hello World'
      print('W' in s)
      print('k' in s)
      print('W' not in s)
      print('k' not in s)


#### 2.5运算符5_位运算符
<img src="https://user-images.githubusercontent.com/99107924/164036205-e87af3c2-0bbd-41aa-a1b0-92b2dea4c8b3.png" width="650"/>



      print(4&8) #按位与&，同为1时结果为1
      print(4|8) #按位或|，同为0时结果为0
      print(4<<1) #左移一位（移动一个位置），相当于乘以2
      print(4<<2) #左移两位（移动两个位置），相当于乘以4

      print(4>>1) #右移一位，相当于除以2
      print(4>>2) #右移两位，相当于除以4

#### 2.6运算符的优先级
<img src="https://user-images.githubusercontent.com/99107924/164485659-25488485-35b8-4998-b949-e60777d58fcd.png" width="650"/>

### 3程序的组织结构

#### 3.1顺序结构
##### 程序从_上到下顺序地执行代码，中间没有任何的判断和跳转，直到程序结束

      '''把大象装冰箱一共分几步'''
      print('------程序开始-------')
      print('1,把冰箱门打开')
      print('2，把大象放冰箱')
      print('3，把冰箱门关上')
      print('------程序结束-------')

#### 3.2对象的布尔值
##### Python-切皆对象，所有对象都有一个布尔值
##### 获取对象的布尔值
##### 使用内置函数bool()


|以下对象的布尔值为False|代码|
|:-|:-:|
|False|print(bool(False))|
|数值0|print(bool(0))|
|None|print(bool(None))|
|空字符串|print(bool(''))|
|空列表|print(bool([]))|
|空元组|print(bool(()))|
|空字典|print(bool({}))|
|空集合| print(bool(set()))|

      print(bool(False)) #False
      print(bool(0)) #False
      print(bool(0.0)) #False
      print(bool(None)) #False
      print(bool('')) #False
      print(bool("")) #False
      print(bool([])) #空列表
      print(bool(list())) #空列表
      print(bool(())) #空元组
      print(bool(tuple())) #空元组
      print(bool({})) #空字典
      print(bool(dict())) #空字典
      print(bool(set())) #空集合
      print('-----------以上对象的布尔值为False-----------------')

      print('-----------其他对象的布尔值均为True----------------')
      print(bool(18))
      print(bool('hello world'))

#### 3.3选择结构
#### 3.3.1分支结构_单分支结构

      money=1000 #余额
      s=int(input("请输入取款金额：")) #取款金额
      #判断余额是否充足
      if money>=s:
          money-=s
          print("取款成功，余额为：",money)

#### 3.3.2分支结构_双分支结构
##### 双分支结构if...else,二选一

      '''从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数'''
      num=int(input("请输入一个整数:"))

      #条件判断
      if num%2==0:
          print(num,'是偶数')
      else:
          print(num,'是奇数')

#### 3.3.3分支结构_多分支结构

      '''多分支结构，多选一执行
      从键盘录入一个整数 成绩
      90-100 A
      80-89  B
      70-79  C
      60-69  D
      0-59   E
      小于0或大于100为非法数据（不是有效成绩）'''

      score=int(input('请输入一个成绩：'))
      #判断
      if 90<=score<=100:
          print('A级')
      elif 80<=score<=89:
          print('B级')
      elif 70<=score<=79:
          print('C级')
      elif 60<=score<=69:
          print('D级')
      elif 0<=score<=59:
          print('E级')
      else:
          print('对不起，成绩不再有效的范围。')

#### 3.3.4分支结构_嵌套if的使用

      '''会员 >= 200 8折
         会员 >= 100 9折
              不打折
         非会员 >= 200 9.5折
              不打折'''
      a=input('您是会员吗？y/n')
      money=float(input('请输入你的购物金额：'))
      #外层判断是非为会员
      if a=='y': #会员
          if money>=200:
              print('打8折,付款金额为:',money*0.8)
          elif money>100:
              print('打9折，付款金额为:',money*0.9)
          else:
              print('不打折，付款金额为:',money)
      else: #非会员
          if money>=200:
              print('打9.5折，付款金额为:',money*0.95)
          else:
              print('不打折，付款金额为:', money)


#### 3.3.5条件表达式

      '''从键盘录入两个整数，比较两个整数的大小'''
      num_a=int(input('请输入第一个整数'))
      num_b=int(input('请输入第二个整数'))
      #比较大小
      '''if num_a>=num_b:
          print(num_a,'大于等于',num_b)
      else:
          print(num_a,'小于',num_b)
      '''
      print('使用条件表达式进入比较') #可以简化操作
      print( str(num_a)+' 大于等于 '+str(num_b) if num_a>=num_b else str(num_a)+' 小于 '+str(num_b) )

### 3.3.6pass语句
##### pass语句，只是做一个占位符，用到需要写语句的地方
      a=input('您是会员吗？y/n')

      #判断是否为会员
      if a=='y':
          pass #程序不会报错
      else:
          pass
      #循环结构的判断是根据对象的布尔值为True或False
      age=int(input('请输入你的年龄:'))
      if age:
          print(age)
      else:
          print('年龄为:',age)
##### 小结图片
<img src="https://user-images.githubusercontent.com/99107924/164725337-32eb8eb2-7d88-4dc6-98fb-c50eb5e29f5d.png" width="650" />

#### 3.4循环结构
#### 3.4.1range()函数的使用

<img src="https://user-images.githubusercontent.com/99107924/164913115-ed652340-c440-4981-be8e-a7d1526fb061.png" width="650"/>

      #range()的三种创建方式
      '''第一种创建方式，只有一个参数（小括号中只给了1个数）'''
      r=range(10) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，默认从0开始，默认相差1的步长
      print(r) #range(0,10)
      print(list(r)) #用于查看range对象中的整数队列 --> list

      '''第二种创建方式，给了两个参数（小括号中给了2个数）'''
      r=range(1,10) #指定的起始值，从1开始，到10结束（不包括10），默认步长为1
      print(list(r)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

      '''第三种创建方式，给了三个参数（小括号中给了3个数）'''
      r=range(1,10,2)
      print(list(r)) #[1, 3, 5, 7, 9]

      '''判断指定的整数 在序列中是否存在in not in'''
      print(10 in r) #False,10不再当前的r整数序列之中
      print(9 in r) #True,9在当前的r整数序列之中

      print(10 not in r) # True
      print(9 not in r) # False

      print(range(1,20,1)) #[1,.....19]
      print(range(1,101,1)) #[1,.....100]
      
#### 3.4.2while循环结构
<img src="https://user-images.githubusercontent.com/99107924/164913981-1eb30d67-5e87-40ce-9e87-a30efdc6a2cc.png" width="650"/>

      a=1
      #判断条件表达式
      while a<10:
          #执行条件执行体
          print(a)
          a+=1

      #计算0到4之间的累加和
      '''
      4步循环法
       1，初始化变量
       2，条件判断
       3，条件执行体（执行体）
       4，改变变量
       总结：初始化的变量与条件变量的变量也改变的变量为同一个
      '''
      sum=0 #用来存储累加
      '''初始化变量为0'''
      a=0
      '''条件判断'''
      while a<5:
          '''条件执行体（循环体）'''
          sum+=a
          '''改变变量'''
          a+=1
      print('和为',sum)
      #1到100之间的偶数和
      sum=0
      '''初始化变量'''
      a=0
      '''条件判断'''
      while a<=100:
          '''条件执行体（求和）'''
          #条件判断是否为偶数
          if not bool(a%2): #if a%2==0:
              sum+=a
              '''改变变量'''
              a+=1
          else:
              '''改变变量'''
              a+=1
      print('1-100之间的偶数和',sum)

#### 3.4.3for_in循环
<img src="https://user-images.githubusercontent.com/99107924/164954800-f5dbec45-4a0f-4075-bc45-3b766d496f28.png" width="650"/>

      for item in 'Python': #第一次去出来的是P，将P赋值给item，将item的值输出
          print(item)

      #range() 产生一个整数序列 --> 也是一个可迭代对象
      for i in range(10):
          print(i)

      #如果在循环体中不需要使用自定义变量，可以定义为“_”
      for _ in range(5):
          print('人生苦短，我用Python')

      print('使用for循环，计算1-100之间的偶数和')
      sum=0 #用于存储偶数和
      for item in range(1,101):
          if item%2==0:
              sum+=item
      print('1-100之间的偶数和为：',sum)
      #练习
      '''输出100到999之间的水仙花数     
          举例
          153=3*3*3+5*5*5+1*1*1
      '''
      for item in range(100,1000):
          ge=item%10      #个位
          shi=item//10%10 #十位
          bai=item//100   #百位
          #print(bai,shi,ge)
          #判断
          if ge**3+shi**3+bai**3==item:
              print(item)

#### 3.4.4流程控制语句_break
<img src="https://user-images.githubusercontent.com/99107924/164954903-7b89b23e-f51d-4d99-91b0-26b80ff73a72.png" width="650"/>

      '''从键盘录入密码，最多录入3次，如果正确就结束循环'''
      for item in range(3):
          pwd=input('请输入密码：')
          if pwd=='8888':
              print('密码正确')
              break #退出循环
          else:
              print('密码不正确')

      a=0
      while a<3:
          pwd=input('请输入密码：')
          if pwd=='8888':
              print('密码正确')
              break
          else:
              print('密码不正确')
          '''改变变量'''
          a+=1

#### 3.4.5流程控制语句_continue
<img src="https://user-images.githubusercontent.com/99107924/164954814-d21f5ffc-b202-4ca1-a48a-a9769da6956a.png" width="650"/>

      '''要求输出1到50之间所有5的倍数，5，10，15，20，25
          5的倍数的共同点：   和5的余数为0的数都是5的倍数
          什么样的数不是5的倍数，    1，2，3，4，6，7，8，9（和5的余数为0的数都不是5的倍数）    
          使用continue来实现
      '''
      for item in range(1,51):
          if item%5==0:
              print(item)

      print('-----------使用continue-------------------')
      for item in range(1,51):
          if item%5!=0:
              continue
          print(item)

#### 3.4.6流程控制语句_else
<img src="https://user-images.githubusercontent.com/99107924/164954870-eb62f4bd-64c0-46da-8692-9a5811da2d8e.png" width="650"/>

      for item in range(3):
          pwd=input('请输入密码：')
          if pwd=='8888':
              print('密码正确')
              break
          else:
              print('密码不正确')
      else:
          print('对不起，三次密码均输入错误')

      a=0
      while a<3:
          pwd=input('请输入密码：')
          if pwd == '8888':
              print('密码正确')
              break
          else:
              print('密码不正确')
          '''改变变量'''
          a+=1
      else:
          print('对不起，三次密码均输入错误')

#### 3.5嵌套结构
<img src="https://user-images.githubusercontent.com/99107924/164955161-3b5bf7aa-b2d5-4b70-bf60-2967d7cd3f95.png" width="650" />

      '''输出一个三行四列的矩形'''
      for i in range(1,4): #行数，执行三次，一次是一行
          for j in range(1,5):
              print('*',end='\t') #不换行输出
          print() #打行

      for i in range(1,10): #行数
          for j in range(1,i):
              print(i,'*',j,'=',i*j,end='\t') #不换行输出
          print()

#### 3.5.1二重循环中的break和continue
<img src="https://user-images.githubusercontent.com/99107924/164955430-a726097d-36c4-428f-84a3-2174dc498853.png" width="650" />

      for i in range(5): #代表外层循环要执行5次
          for j in range(1,11):
              if j%2==0:
                  #break
                  continue
              print(j,end='\t')
          print()


## 四.高级变量类型

### 1列表
#### 1.1列表的创建

      '''创建列表的第一种方式，使用[]'''
      lst1=['hello','world',98]
      '''创建列表的第二种方式，使用内置函数list()'''
      lst2=list(['hello','world','98'])

#### 1.2列表的特点
<img src="https://user-images.githubusercontent.com/99107924/164955965-8aa21229-a211-4693-a5b7-ab7114a5833a.png" width="650" />

      lst=[1,2,3,4,5.1]
      print(lst)
      print(lst[0],lst[-1])

#### 1.3获取列表中指定元素的索引

      lst=['hello','world',98,'hello']
      print(lst.index('hello')) #如果列表中有相同元素只返回列表中相同元素的第一个元素的索引
      #print(lst.index('Python')) #ValueError: Python is not in list
      print(lst.index('hello',1,4))

#### 1.4获取列表中指定元素
<img src="https://user-images.githubusercontent.com/99107924/164982929-66af2da1-ce47-4e00-85ad-04db8755b399.png" width="650"/>

      lst=['hello','world',98,'hello','world',234]
      print(lst[2])   #获取索引为2的元素
      print(lst[-3])  #获取索引为-3的元素

#### 1.5获取列表中的多个元素_切片操作

      lst = [10, 20, 30, 40, 50, 60, 70, 80]
      # start=1,stop=6,step=1
      print(lst[1:6:1])  # 新的列表对象
      print('原列表', id(lst))
      lst2 = lst[1:6:1]
      print('切的片段', id(lst2))
      # start=1,stop=6,step采用默认
      print(lst[1:6])
      print(lst[1:6:],'默认步长为1')  # 默认步长为1
      # start=1,stop=6,step=2
      print(lst[1:6:2])
      # stop=6,step=2,start采用默认
      print(lst[:6:2],' 默认从0开始')  # 默认从0开始
      # start=1,step=2,stop采用默认
      print(lst[1::2],'默认到最后一个结束')  # 默认到最后一个结束

      print('----step步长为负数的情况-----')
      print('原列表', lst)
      print('新列表', lst[::-1])
      print('会将原列表的元素倒叙排列')
      # start=7,stop 省略 step=-1
      print(lst[7::-1])
      # start=6,stop=0,step=-2
      print(lst[6:0:-2])

#### 1.6    列表元素的判断和遍历

##### 判断元素在列表当中是否存在

      print('p' in 'python')
      print('k' not in 'python')

      lst=[10,20,'python','hello']
      print(10 in lst) # True
      print(100 in lst) # False
      print(10 not in lst) # False
      print(100 not in lst) # True

##### 遍历列表元素
      for i in lst:
          print(i)

#### 1.7列表元素的添加操作
<img src='https://user-images.githubusercontent.com/99107924/165215159-a86e0001-1f99-4144-8e7e-e011a98b4d99.png' width='650'/>


##### 向列表的末尾添加一个元素
      lst=[10,20,30]
      print('添加元素之前',lst,id(lst))
      lst.append(100)
      print('添加元素之后',lst,id(lst))

##### 将lst2作为一个元素添加到列表的末尾(append)
      lst2=['hello','world']
      lst.append(lst2)
      print(lst)

##### 向列表的末尾一次性添加多个元素(extend)
      lst.extend(lst2)
      print(lst)

##### 在任意位置上添加一个元素(insert)
      lst.insert(1,90) # 在位置为1的位置上添加
      print(lst)

##### 在任意位置上添加N多个元素(切片)
      lst3=[True,False,'hello']
      lst[1:]=lst3
      print(lst)

#### 1.8列表元素的删除操作
<img src='https://user-images.githubusercontent.com/99107924/165252727-c6ac845f-6587-40ea-b3b1-7bd2135e6ac4.png' width='400' height='400'/>

##### remove()从列表中移除第一个元素，如果有重复元素的话。
      lst=[10,20,30,40,50,60,30]
      lst.remove(30)
      print(lst)
      #lst.remove(100) #如果元素不存在，会报错（ValueError:  x not in list）

##### pop()根据索引来移除元素
      lst.pop(1)
      print(lst)
      #lst.pop(5) #超出范围会抛出异常，（IndexError: pop index out of range）
      lst.pop() #如果不指定索引，默认删除列表最后的元素
      print(lst)

##### 切片操作，删除至少一个元素，将产生一个新的列表对象
      new_lst=lst[1:3]
      print('原列表',lst)
      print('切片后的列表',new_lst)

##### 不产生新的列表对象，而是删除源列表中的内容
      lst[1:3]=[]
      print(lst)

##### clear()清楚列表中的所有元素
      lst.clear()
      print(lst)

##### del()语句将列表对象删除
      del lst
      print(lst) #无定义 （NameError: name 'lst' is not defined）


#### 1.9列表元素的修改操作


##### 一次修改一个值
      lst=[10,20,30,40] #原列表
      print(lst)
      lst[2]=100
      print(lst)

##### 一次修改多个值
      lst[1:3]=[300,400,500,600]
      print(lst)

#### 1.10列表元素的 排序操作

- 列表元素的排序操作 
- 常见的两种方式：  
1. 调用sort()方法，列有中的所有元素默认按照从小到大的顺序进行排序，可以指定reverse=True，进行降序排序 。  
2. 调用内置函数sorted()， 可以指定reverse=True， 进行降序排序，原列表不发生改变。

##### 开始排序，调用列表对象的sort的方法，升序排列
      lst=[20,40,10,98,54]
      print('排序前的列表',lst,id(lst))
      lst.sort()
      print('排序后的列表',lst,id(lst))

##### 通过指定关键字参数，将列表中的元素进行降序排列
      lst.sort(reverse=True) #reverse=True，表示降序排列；reverse=False，表示升序排列
      print('降序排列   ',lst)
      lst.sort(reverse=False)
      print('升序排列   ',lst)

##### 使用内置函数sorted()对列表进行排列，将产生一个新的列表对象
      lst=[20,40,10,98,54]
      new_lst=sorted(lst)
      print('原列表',lst,id(lst))
      print('新列表',new_lst,id(new_lst))

##### 通过指定关键字参数，将列表中的元素进行降序排列
      desc_lst=sorted(lst,reverse=True)
      print('降序列表',desc_lst,id(desc_lst))


#### 1.10列表生成式
- 列表生成式简称"生成列表的公式"
语法格式：
      
      [i*i for i in range(1,10)]
注意事项: 表示列表元素的表达式中通常包括自定义变量

      lst=[i*i for i in range(1,10)]
      print(lst)

##### 列表中的元素的值为2，4，6，8，10
      lst2=[i for i in range(2,11,2)]
      print(lst2)

#### 小结：
<img src='https://user-images.githubusercontent.com/99107924/165261801-25fa47d5-0b0f-45bd-849a-917c6e9547c1.png' width='800' height='350'/>



### 2字典
#### 2.1字典的定义
- 字典
- Python内置的数据结构之一，与列表一样是一个可变序列。
- 以键值对的方式存储数据，字典是一个无序的序列。
#### 2.2字典的实现原理
-字典的实现原理与查字典类似，查字典是先根据部首或拼音查找对应的页码，Python中的字典是根据key查找value所在的位置。
#### 2.3字典的创建
- 最常用的方式：使用花括号{}创建字典
      scores={'张三':100,'李四':98,'王五':45}
      print(scores)
      print(type(scores))

- 使用内置函数dict()创建字典
      student=dict(name='jack',age=20)
      print(student)

- 使用空字典
      d={}
      print(d)
#### 2.4字典元素的获取
- []取值与使用get()取值的区别
1. 如果字典中不存在指定的key，拋出keyError异常
2. get()方法取值，如果字典中不存在指定的key，并不会拋出KeyError而 是返回None，可以通过参数设置默认的value，以便指定的key不存在时返回

- 第一种方式，使用[]
 
      scores={'张三':100,'李四':98,'王五':45}
      print(scores['张三'])
      #print(scores['陈六']) #KeyError: '陈六'

- 第二种方式，使用get()方法
 
      print(scores.get('张三'))
      print(scores.get('陈六')) #None
      print(scores.get('麻七',99)) #99是在查找'麻七'所对应的value不存在时，提供的一个默认值

#### 2.5字典的常用操作

- key的判断

      score={'张三':100,'李四':98,'王五':45}
      print('张三' in score)
      print('张三' not in score)

- key的删除和清空

      del score['张三'] #删除指定的key-value对
      print(score)
      score.clear() #请空字典的元素
      print(score)

-key的新增和修改

      score={'李四': 98, '王五': 45}
      score['陈六']=98 #新增元素
      print(score )
      score['陈六']=100 #修改元素
      print(score)

#### 2.6字典的视图获取

- 获取所有的key
 
      score={'张三':100,'李四':98,'王五':45}
      keys=score.keys()
      print(keys)
      print(type(keys)) #将所有key组成的视图转成列表

- 获取所有的value

      values=score.values()
      print(values)
      print(type(values))
      print(list(values))

- 获取所有的key-value对
      
      items=score.items()
      print(items)
      print(list(items)) #转换之后的列表元素是由元组组成的（元组之后在讲解）

#### 2.7字典元素的遍历

- 字典元素的遍历

      score={'张三':100,'李四':98,'王五':45}
      for item in score:
          print(item,score[item],score.get(item))












      
      
      
      
