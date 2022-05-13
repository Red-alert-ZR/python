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

#### 2.8字典的特点
- 字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
- 字典中的元素是无序的
- 字典中的key必须是不可变对象
- 字典也可以根据需要动态地伸缩
- 字典会浪费较大的内存，是一种使用空间换时间的数据结构

      dict={'name':'张三','name':'李四'} #key不允许重复
      print(dict)

      dict={'name':'张三','nikename':'张三'} #value允许重复
      print(dict)

      lst=[10,20,30]
      lst.insert(1,100)
      print(lst)
      #dict={lst:100} #key必须是不可变对象
      #print(dict)

#### 2.9字典生成式
- 内置函数zip()

用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组,然后返回由这些元组组成的列表.

      items=['Fruits','Book','Others']
      prices=[96,78,85,100,120]

      dict={item.lower():price for item,price in zip(items,prices)}
      print(dict)
      del dict['fruits']
      print(dict)

### 3元组
#### 3.1元组的定义
- 元组

python内置的数据结构之一，是一个不可变序列

- 不可变序列与可变序列
##### 不变可变序:字符串、元组

不变可变序列:没有增、删，改的操作

      s='hello' #字符串-->不可变序列
      print(id(s))
      s+='world'
      print(id(s))
      print(s) #内存地址改变
##### 可变序列:列表、字典

可变序列:可以对序列执行增、删、改操作，对象地址不发生更改

      lst=[10,20,45] #列表-->可变序列
      print(id(lst))
      lst.append(300)
      lst.insert(1,100)
      print(id(lst)) #内存地址没有更改

#### 3.2元组的创建方式
- 元组的创建方式
##### 直接小括号
      t=('Python','world',98)
      print(t)
      print(type(t))
      
      t2='Python','world',98 #省略了小括号
      print(t2)
      print(type(t2))
      
##### 只包含一个元组的元素需要使用逗号和小括号
      t3=('Python',) #元组中只有一个元素，逗号不能省
      print(t3)
      print(type(t3))

##### 使用内置函数
      t1=tuple(('Python','world',98))
      print(t1)
      print(type(t1))

##### 空元组的创建方式
      lst=[] #空列表
      lst1=list()

      dict1=dict()
      dict2={}

      t4=()
      t5=tuple()

      print('空列表',lst,lst1)
      print('空字典',dict1,dict2)
      print('空元组',t4,t5)

#### 3.3元组为什么是不可变序列
- 在多任务环境下，同时操作对象时不需要加锁
- 因此，在程序中尽量使用不可变序列

##### 注意事项:元组中存储的是对象的引用
1.如果元组中对象本身不可对象，则不能再引用其它对象。

2.如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变

      t=(10,[20,30],9)
      print(t)
      print(type(t))
      print(t[0],type(t[0]),id(t[0]))
      print(t[1],type(t[1]),id(t[1]))
      print(t[2],type(t[2]),id(t[2]))
      #尝试将t[1]修改为100
      print(id(100))
      #t[1]=100 #由于元组是不允许修改元素的
      #由于[20,30]列表，而列表是可变序列，所以可以向列表中添加元素，而列表的内存地址不变
      t[1].append(100) #向列表中添加元素
      print(t,id(t[1][2]))

#### 3.4元组的遍历
- 元组是可迭代对象，所以可以使用for...in进行遍历

      t=('Python','world',98)
      #使用索引
      print(t[0])
      print(t[1])
      print(t[2])
      #print(t[3]) #IndexError: tuple index out of range

      #遍历元组
      for i in t:
          print(i)

### 4集合
#### 4.1集合的定义
##### 集合
- Python语言提供的内置数据结构.
- 与列表、字典一样都属于可变类型的序列
- 集合是没有value的字典

#### 4.2集合的创建

- 第一种创建方式，直接使用{}

      s={2,3,4,5,5,6,6,7,7} #集合中的元素不允许重复
      print(s,type(s))

- 第二种创建方式,使用内置函数set()

      s1=set(range(6))
      print(s1,type(s1))
      s2=set([1,2,3,4,5,6,6,6])
      print(s2,type(s2))
      s3=set((29,1,2,3,4,'赵瑞',65))
      print(s3,type(s3))
      s4=set('Python')
      print(s4,type(s4))
      s5=set({123,123,1223,'hello'})
      print(s5,type(s5))
      s6=set() #空集合
      print(type(s6))
 
#### 4.3集合的相关操作

- 集合元素的判断操作 
    * in 或 not in <br>

##### <br>
      s={10,20,30,405,60}
      print(10 in s) #Ture
      print(100 in s) #False
      print(10 not in s) # False
      print((100 not in s)) #True


- 集合元素的新增操作<br>
    * 1.调用add()方法，一次添中一个元素 <br>
    * 2.调用update()方法至少添中一个元素 <br>
 
 ##### <br>
      s.add(80) #add()依次添加一个元素
      print(s)
      s.update({200,400,300}) #一次至少添加一个元素
      print(s)
      s.update([100,99,88])
      print(s)
      s.update((77,55,92))
      print(s)
      s.update(['哈哈','world'])
      print(s)


- 集合元素的删除操作<br>
    * 1.调用remove()方法，一次删除一个指定元素，如果指定的元素不存在拋出KeyError <br>
    * 2.调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不拋异常 <br>
    * 3.调用pop()方法，一次只删除一个任意元素 <br>
    * 4.调用clear()方法，清空集合 <br>

##### <br>
      s.remove(100)
      print(s)
      #s.remove(500) ;print(s) #KeyError: 500(500不存在)
      s.discard(500);print(s) #没有也不报错
      s.discard(300)
      print(s)
      s.pop()
      print(s)
      s.pop()
      print(s)
      #s.pop(300);print(s) #TypeError: set.pop() takes no arguments (1 given)
      #pop()是无参数的
      s.clear() #清空集合当中的元素
      print(s)
      
#### 4.5集合间的关系

- 两个集合是否相等
    * 可以使用运算符==或!=进行判断
<br>

      s1={10,20,30,40}
      s2={30,40,20,10}
      print(s1==s2) #True
      print(s1!=s2) #False

- 一个集合是否是另一个集合的子集
    * 可以调用方法issubset进行判断
    * B是A的子集
<br>

      s1={10,20,30,40,50,60}
      s2={10,20,30,40}
      s3={10,20,90}
      print(s2.issubset(s1)) #True
      print(s3.issubset(s1)) #False
- 一个集合是否是另一个集合的超集
    * 可以调用方法issuperset进行判断
    * A是B的超集
<br>

      s1={10,20,30,40,50,60}
      s2={10,20,30,40}
      s3={10,20,90}
      print(s1.issuperset(s2)) #True
      print(s1.issuperset(s3)) #False
- 两个集合是否没有交集
    * 可以调用方 法isdisjoint进行判断
<br>

      s2={10,20,30,40}
      s3={10,20,90}
      s4={100,200,300}
      print(s2.isdisjoint(s3)) #False
      print(s2.isdisjoint(s4)) #True

#### 4.6集合的数据操作
- 交集

      s1={10,20,30,40}
      s2={20,30,40,50,60}
      print(s1.intersection(s2))
      print(s1&s2) #求交集： intersection() 与 & 等价操作

- 并集
 
      s1={10,20,30,40}
      s2={20,30,40,50,60}
      print(s1.union(s2))
      print(s1|s2) #求并集： union() 与 | 等价操作

- 差集

      s1={10,20,30,40}
      s2={20,30,40,50,60}
      print(s1.difference(s2))
      print(s1-s2) #求差集： different() 与 - 等价操作

- 对称差集

      s1={10,20,30,40}
      s2={20,30,40,50,60}
      print(s1.symmetric_difference(s2))
      print(s1^s2) #求对称差集： symmtric_difference() 与 ^ 等价操作

##### 原集合不会改变

#### 4.7集合生成式

      lst={i*i for i in range(6)}
      print(lst,type(lst))


### 5字符串
#### 5.1字符串的创建与驻留机制
- 字符串
    - 在Python中字符串是基本数据类型，是一个不可变的字符序列
- 什么叫字符串驻留机制呢?
    - 仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中，Python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量

- 驻留机制的几种情况(交互模式)
    - 字符串的长度为0或1时
    - 符合标识符的字符串
    - 字符串只在编译时进行驻留，而非运行时
    - \[-5,256]之间的整数数字
* sys中的intern方法强制2个字符串指向同一个对象
* PyCharm对字符串进行了优化处理

- 字符串驻留机制的优缺点
    - 当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁的创建和销毁，提升效率和节约内存，因此拼接字符串和修改字符串是会比较影响性能的。
    - 在需要进行字符串拼接时建议使用str类型的join方法，而非+ ,因为join()方法是先计算出所有字符中的长度，然后再拷贝，只new-次对象，效 率要比"+"效率高

#### 5.2字符串的常用操作

- 字符串的查询操作
<table>
    <tr>
        <th>功能</th>
        <th>方法名称</th>
        <th>作用</th>
    </tr>
    <tr>
        <td rowspan="4">查询方法</td>
        <td>index()</td>
        <td>查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError</td>
    </tr>
    <tr>
        <td>rindex()</td>
        <td>查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError</td>
    </tr>
    <tr>
        <td>find()</td>
        <td>查找子串sbustr第一次出现的位置，如果查找的子串不存在时，则返回-1</td>
    </tr>
    <tr>
        <td>rfind()</td>
        <td>查找子串substr最后一次出现的位置，如果查找的子串不存在时，则返回-1</td>
    </tr>
</table>

      s='hello,hello'
      print(s.index('lo')) #3
      print(s.find('lo')) #3
      print(s.rindex('lo')) #9
      print(s.rfind('lo')) #9

      #print(s.index('s')) #ValueError: substring not found
      print(s.find('s')) #-1，不会抛出异常

      #print(s.rindex('s')) #ValueError: substring not found
      print(s.rfind('s')) #-1，不会抛出异常  

- 字符串的大小写转换方法

<table>
    <tr>
        <th>方法</th>
        <th>方法名称</th>
        <th>作用</th>
    </tr>
    <tr>
        <td rowspan="4">字符串对齐  </td>
        <td>center()</td>
        <td>居中对齐，第1个参数指定宽度，第2个参数指定填充符,第2个参数是可选的，默认是空格,如果设置宽度小于实际宽度则则返回原字符串</td>
    </tr>
    <tr>
        <td>ljust()</td>
        <td>左对齐，第1个参数指定宽度，第2个参数指定填充符，第2个参数是可选的，默认是空格如果设置宽度小于实际宽度则则返回原字符串</td>
    </tr>
    <tr>
        <td>rjust()</td>
        <td>右对齐，第1个参数指定宽度，第2个参数指定填充符,第2个参数是可选的，默认是空格如果设置宽度小于实际宽度则则返回原字符串</td>
    </tr>
    <tr>
        <td>zfill()</td>
        <td>右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身</td>
    </tr>
</table>

      s='hello,python'
      a=s.upper() #转成大写之后，会产生一个新的字符串对象
      print(a,id(a))
      print(s,id(s))
      b=s.lower() #转换之后，会产生一个新的字符产对象
      print(b,id(b))
      print(s,id(s))

      s2='hello.Python'
      print(s2.swapcase()) #把字符串中所有大写字母转成小写字母，把所有小写字母都转成大写字母
      print(s2.title()) #把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写
      print(s2.capitalize()) #把第一个字符转换为大写，把其余字符转换为小写

- 字符串内容对齐操作方法

 |功能|方法名称|作用|
 |---- | :----: | -----
 |**字符串对齐**|center()|居中对齐，第1个参数指定宽度，第2个参数指定填充符,第2个参数是可选的，默认是空格,如果设置宽度小于实际宽度则则返回原字符串|
 |**字符串对齐**|ljust()|左对齐，第1个参数指定宽度，第2个参数指定填充符，第2个参数是可选的，默认是空格如果设置宽度小于实际宽度则则返回原字符串|
 |**字符串对齐**|rjust()|右对齐，第1个参数指定宽度，第2个参数指定填充符,第2个参数是可选的，默认是空格如果设置宽度小于实际宽度则则返回原字符串|
 |**字符串对齐**|zfill()|右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身|

      s='hello,Python'
      '''居中对齐'''
      print(s.center(20,'*'))
      '''左对齐'''
      print(s.ljust(20,'*'))
      print(s.ljust(10)) #如果设置宽度小于实际宽度则则返回原字符串
      print(s.ljust(20)) #默认是空格
      '''右对齐'''
      print(s.rjust(20,'*'))
      print(s.rjust(20)) #默认是空格
      print(s.rjust(10)) #如果设置宽度小于实际宽度则则返回原字符串
      '''右对齐，使用0进行填充'''
      print(s.zfill(20))
      print(s.zfill(10))
      print('-8910'.zfill(8))
      '''区别'''
      print(s.rjust(20,'0'))
      print('-8910'.rjust(10,'0'))

- 字符串劈分操作方法 

<table>
    <tr>
          <th>功能</th>
          <th>方法名称</th>
          <th>作用</th>
    </tr>
    <tr>
          <td rowspan='6'>字符串的劈分</td>
          <td rowspan='3'>split()</td>
          <td>从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表</td>
    </tr>
    <tr>
          <td>以通过参数sep指定劈分字符串是的劈分符</td>          
    </tr>
    <tr>
          <td>通过参数maxsplit指定 劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独做为一部分</td>
    </tr>
    <tr>
         <td rowspan='3'>rsplit()</td>
         <td>从字符串 的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一一个列表   </td>
    </tr>
    <tr>
          <td>以通过参数sep指定劈分字符串是的劈分符</td>
    </tr>
    <tr>
          <td>通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独做为一部分</td>
    </tr>
</table>
          
      s='hello world Python'
      '''split()从左侧开始劈分'''
      lst=s.split()
      print(lst)
      s1='hello|world|Python'
      lst=s1.split(sep='|')
      print(lst)
      lst=s1.split(sep='|',maxsplit=1)
      print(lst)

      '''rsplit()从右侧开始劈分'''
      lst=s.rsplit()
      print(lst)
      lst=s1.rsplit(sep='|')
      print(lst)
      lst=s1.rsplit(sep='|',maxsplit=1)
      print(lst)

- 判断字符串操作的方法

<table>
    <tr>
        <th>功能</th>
        <th>方法名称</th>
        <th>作用</th>
    </tr>
    <tr>
        <td rowspan="6">判断字符串的方法</td>
        <td>isidentifier()</td>
        <td>判断指定的字符串是不是合法的标识符</td>
    </tr>
    <tr>
        <td>isspace()</td>
        <td>判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符）</td>
    </tr>
    <tr>
        <td>isalpha</td>
        <td>判断指定的字符串是否全部由字母组成</td>
    </tr>
    <tr>
        <td>isdecimal()</td>
        <td>判断指定的字符串是否全部由十进制的数字组成 </td>
    </tr>
    <tr>
        <td>isnumeric</td>
        <td>判断指定的字符串是否全部由数字组成</td>
    </tr>
    <tr>
        <td>isalnum</td>
        <td>判断指定的字符串是否全部由字母和数字组成</td>
    </tr>
</table>
          
      s='hello,Python'
      print('1.',s.isidentifier()) #False
      print('2.','hello'.isidentifier()) #True
      print('3.','张三_'.isidentifier()) #True
      print('4.','张三_123'.isidentifier()) #True

      print('5.','\t'.isspace()) #True
      print('6.','abc'.isalpha()) #True
      print('7.','张三'.isalpha()) #True
      print('8.','张三1'.isalpha()) #False

      print('9','123'.isdecimal()) #True
      print('10','123四'.isdecimal()) #False
      print('11','ⅡⅡⅡ'.isdecimal()) #False
      print('12.','123'.isnumeric()) #True
      print('13','123四'.isnumeric()) #True
      print('14','ⅡⅡⅡ'.isnumeric()) #True

      print('15','abc1'.isalnum()) #True
      print('16','张三123'.isalnum()) #True
      print('17','abc!'.isalnum()) #False

- 字符串的替换与合并
<table>
    <tr>
        <th>功能</th>
        <th>方法名称</th>
        <th>作用</th>
    </tr>
    <tr>
        <td >字符串替换</td>
        <td>replace()</td>
        <td>第1个参数指定被替换的子串,第2个参数指定替换子串的字符串,该方法返回替换后得到1的字符串,替换前的字符串不发生变化,调用该方法时可以通过第3个参数指定最大替换次数
            </td>
    </tr>
    <tr>
        <td>字符串的合并</td>
        <td>join()</td>
        <td>将列表或元组中的字符串合并成一个字符串</td>
    </tr>
</table>

      s='hello,Python'
      print(s.replace('Python','Java'))
      s1='hello,Python,Python,Python'
      print(s1.replace('Python','Java',2))

      lst=['hello','java','python']
      print('|'.join(lst))
      print(''.join(lst))
      print(' '.join(lst))

      t=('hello','Java','Python')
      print(''.join(t))
      print('*'.join('Python'))

#### 5.3字符串的比较操作

- 运算符:>,>=,<,<=,==,!=

- 比较规则:首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较

- 比较原理:两上字符进行比较时，比较的是其ordinal value(原始值),调用内置函数ord可以得到指定字符的ordinal value。与内置函数ord对应的是内置函数chr,调用内置函数chr时指定ordinal value可以得到其对应的字符

      print('apple'>'app') #True
      print('apple'>'banana') #False
      print(ord('a'),ord('b'))
      print(ord('赵'),ord('瑞'))

      print(chr(97),chr(98))
      print(chr(36213),chr(29790))

      '''== 与 is 的区别
         == 比较的是 value
         is 比较的是id是否相等'''
      a=b='Python'
      c='Python'
      print(a==b) #True
      print(b==c) #True

      print(a is b) #True
      print(a is c) #True
      print(id(a))
      print(id(b))
      print(id(c))

#### 5.4字符串的切片操作
**字符串是不可改变类型**

不具备增，删，改等操作<br>
切片操作将产生新的对象

      s='hello,Python'
      s1=s[:5] #由于没有指定起始位置，所以从0开始
      print(s1) #由于没有指定结束位置，所以切到字符串的最后一个元素
      s2=s[6:]
      print(s2)
      s3='!'
      nuwstr=s1+s3+s2
      print(nuwstr)
      print('\n',id(s),'\n',id(s1),'\n',id(s2),'\n',id(s3),'\n',id(nuwstr),)

      print('-----------------切片[start:end:step]----------------------')
      print(s[1:5:1]) #从1开始截到5（不包括5），步长为1
      print(s[::2]) #默认从0开始，没有写结束，默认到字符串的最后一个元素，步长为2，两个元素的索引间隔为2
      print(s[::-1]) #默认从字符串的最后一个元素开始，到字符串的第一个元素结束，因为步长为负数
      print(s[-6::1]) #从索引为-6开始，到字符串的最后一个元素结束，步长为1

#### 5.5格式化字符串
**格式化字符串的两种方式**
- %做占位符
- {}做占位符

      # 1、%
      name='张三'
      age=20
      print('我叫%s,今年%d岁' %(name,age))

      # 2、{}
      print('我叫{0},今年{1}岁'.format(name,age))

      # 3、f-string
      print(f'我叫{name},今年{age}岁')

      print('%10d' % 99) #10表示的是宽度
      print('hellohello')
      print('%.3f' % 3.1415926) #%.3f 保留三位小数
      #同时表示宽度和精度
      print('%10.3f' % 3.1415926) #一共总宽度为10，小数点后3位

      print('{0:.3}'.format(3.1415926)) #{:.3}表示一共3位数
      print('{0:.3f}'.format(3.1415926)) #{:.3f}表示的是3位小数
      print('{:10.3f}'.format(3.1415926)) #{:10.3f}同时表示宽度和精度


**编码与解码的方式**
- 编码：将字符串转换为二进制数据(bytes)
- 解码：将bytes类型的数据转换成字符串类型

      s='天涯共此时'
      #编码
      print(s.encode(encoding='GBK')) #在GBK这种编码中，一个中文占两个字节
      print(s.encode(encoding='UTF-8')) #在UTF-8这种编码中，一个中文占三个字节

      #解码
      #byte代表的就是一个二进制数据(字节类型的数据)
      byte=s.encode(encoding='GBK') #编码
      print(byte.decode(encoding='GBK')) #解码

      byte=s.encode(encoding='UTF-8') #编码
      print(byte.decode(encoding='UTF-8')) #解码

      a='赵'
      byte1=a.encode(encoding='UTF-8')
      print(byte1.decode(encoding='UTF-8'))

#### 小结：
<img src='https://user-images.githubusercontent.com/99107924/166857447-b5bb56a2-1c61-4b16-8cef-8ad13e5cc17c.png' width='1000' height='400'>


## 5函数应用

#### 1函数的创建和调用 <br>
**函数就是执行特定任务和完成特定功能的一段代码** <br>
<br>
函数的作用: <br>
- 复用代码
- 隐藏实现细节
- 提高可维护性
- 提高可读性便于调试
**函数的创建

      def calc(a,b):
          c=a+b
          return c

      result=calc(10,20)
      print(result)

#### 2函数的参数传递
#### 2.1函数的位置实参和关键字实参
**位置实参:**
根据形参对应的位置进行实参传递
<br>
**关键字实参:**
根据形参名称进行实参传递

      def calc(a,b): #a,b称为形式参数，简称形参，形参的位置是在函数的定义处
          c=a+b
          return c

      result=calc(10,20) #10,20称为实际参数的值，简称实参，实参的位置是在函数的调用处
      print(result)

      result=calc(b=10,a=20) #=左侧的变量的名称称为关键字参数
      print(result)

#### 2.2函数参数传递的内存分析
      def fun(arg1,arg2):
          print('arg1=',arg1)
          print('arg2=',arg2)
          arg1=100
          arg2.append(10)
          print('arg1=',arg1)
          print('arg2=',arg2)
          #return

      n1=11
      n2=[22,33,44]
      print('n1=',n1)
      print('n2=',n2)
      print('-----------------')
      fun(n1,n2) #将位置传参，arg1，arg2，是函数定义的形参，n1和n2是函数调用处的实参，总结：实参名称和形参名称可以不一致
      print('n1=',n1)
      print('n2=',n2)

      '''在函数调用过程中，进行参数的传递
      如果是不可变对象，在函数体内的修改不会影响实参的值: arg1的修改为100，不会影响n1的值
      如果是可变对象，在函数体内的修改会影响到实参的值： arg2的修改为.append(10)，会影响到n2的值'''

#### 3函数的返回值
**函数返回多个值时，结果为元组**

      print(bool(0))
      print(bool(123))
      def fun(num):
          odd=[] #存奇数
          even=[] #存偶数
          for i in num:
              if i%2:
                  odd.append(i)
              else:
                  even.append(i)
          return odd,even

      print(fun([10,29,34,23,44,53,55]))

      '''
      函数的返回值
          1、如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】 return可以不写。
          2、函数的返回值，如果是1个，直接返回原类型。
          3、函数的返回值如果是多个，返回的结果为元组。
      '''

      def fun1():
          print('hello')
      fun1()
      
      def fun2():
          return 'hello'
      res=fun2()
      print(res)

      def fun3():
          return 'hello','world'
      res=fun3()
      print(res)

      '''函数在定义时，是否需要返回值，视情况而定'''

#### 4函数的参数定义
#### 4.1函数定义_默认值参数
- 函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参

      def fun(a,b=10): #b称为默认值参数
          print(a,b)

      #函数的调用
      fun(100)
      fun(20,30)

#### 4.2函数参数的定义_个数可变的位置参数_个数可变的关键数形参
**个数可变的位置参数**
- 定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
- 使用*定义个数可变的位置形参
- 结果为一个元组

      def fun(*args): #函数定义时的可变的位置参数
          print(args)                 

      fun(10)
      fun(10,30)
      fun(30,405,50)

**个数可变的关键字形参**
- 定义函数时，无法事先确定传递的关键字实参的个数，使用可变的关键字形参
- 使用**定义个数可变的关键字形参
- 结果为一个字典

      def fun1(**kwargs):
          print(kwargs)

      fun1(a=10)
      fun1(a=20,b=30,c=40)

      '''def fun2(*args,*args1):
          pass
          以上代码，程序会报错，个数可变的位置参数，只能是1个

      def fun2(**args,**kwargs):
          pass
          以上代码，程序会报错，个数可变的关键字参数，只能是1个
          '''
      def fun2(*args1,**args2):
          pass

      '''def fun3(**args1.*args2):
          pass
          在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求：个数可变的位置形参放在个数可变的关键字形参之前
      '''

#### 4.3函数的参数总结
<table>
    <tr>
        <th>序号</th>
        <th>参数的类型</th>
        <th>函数的定义</th>
        <th>函数的调用</th>
        <th>备注</th>
    </tr>
    <tr>
        <td rowspan="2">1</td>
        <td>位置实参</td>
        <td></td>
        <td>✔</td>
        <td></td>
    </tr>
    <tr>
        <td>将序列中的每个元素都转换为位置实参</td>
        <td></td>
        <td>✔</td>
        <td>使用*</td>
    </tr>
    <tr>
        <td rowspan="2">2</td>
        <td>关键字实参</td>
        <td></td>
        <td>✔</td>
        <td></td>
    </tr>
    <tr>
        <td>将字典中的每个键值对都转换为关键字实参</td>
        <td>✔</td>
        <td></td>
        <td>使用**</td>
    </tr>
    <tr>
        <td>3</td>
        <td>默认值形参</td>
        <td>✔</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>4</td>
        <td>关键字形参</td>
        <td>✔</td>
        <td></td>
        <td>使用*</td>
    </tr>
    <tr>
        <td>5</td>
        <td>个数可变的位置形参</td>
        <td>✔</td>
        <td></td>
        <td>使用*</td>
    </tr>
    <tr>
        <td>6</td>
        <td>个数可变的关键字形参</td>
        <td>✔</td>
        <td></td>
        <td>使用**</td>
    </tr>
</table>

      def fun1(a,b,c): #a,b,c在函数的定义处，所以是形式参数
          print('a=',a)
          print('b=',b)
          print('c=',c)

      #函数的调用
      fun1(10,20,30) #函数调用时的参数传递，称为位置传参
      lst=[11,22,33]
      fun1(*lst) #在函数调用时，将列表中的每个元素都转换为位置实参传入
      print('--------------------------')
      fun1(a=100,c=300,b=200) #函数的调用，所以是关键字实参
      dic={'a':111,'b':222,'c':333}
      fun1(**dic) #在函数调用时，将字典中的键值对都转换为关键字实参传入
      print('**********************************************************************')

      #函数的定义
      def fun1(a,b=10): #b是在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
          print('a=',a)
          print('b=',b)

      def fun2(*args1): #个数可变的位置形参
          print(args1)

      def fun3(**args2): #个数可变的关键字形参
          print(args2)

      fun1(1)
      fun2(10,20,30,40)
      fun3(a=11,b=22,c=33,d=44,e=55)

      def fun4(a,b,*,c,d): #从这颗星之后的参数，在函数调用时，只能采用关键字参数传递
          print('a=', a)
          print('b=', b)
          print('c=', c)
          print('d=', d)

      #调用fun4()函数
      #fun4(10,20,30,40) #位置实参传递
      fun4(a=10,b=20,c=30,d=40) #关键字实参传递
      fun4(10,20,c=30,d=40) #前两个参数，采用的是位置实参传递，而c，d采用的是关键字实参传递
      '''需求，c，d只能采用关键字实参传递'''

      '''函数定义时的形参的顺序问题'''
      def fun5(a,b,*,c,d,**kwargs):
           pass

      def fun6(*args,**kwargs):
          pass

      def fun7(a,b=10,*args,**kwargs):
          pass

#### 5变量的作用域
- 程序代码能访问该变量的区域
- 根据变量的有效范围可分为
    - 局部变量
        - 在函数内定义并使用的变量，只是函数内部有效，局部变量使用global声明，这个变量就会成为全局变量
    - 全局变量
        - 函数体外定义的变量，可作用于函数体外
<br>

      def fun1(a,b):
          c=a+b #c,就称为局部变量，因为c是函数体内进行定义的变量,a,b为函数的形参，作用范围也是函数内部，相当于局部变量
          print(c)

      #print(a);print(c) #因为a,c,超出了起作用的范围（超出了作用域）

      name='赵瑞' #name的作用范围为函数内部和外部都可以使用--->称为全局变量
      print(name)
      def fun2():
          print(name)
      #调用函数
      fun2()

      def fun3():
          global age
          age=20
          print(age)
      fun3()
      print(age)

#### 6递归函数
- 递归函数
    - 如果在一个函数的函数体内调用了该函数本身，这个函数就称为递归函数
- 递归的组成部分
    - 递归调用与递归终止条件
- 递归的调用过程
    - 每递归调用一次函数，都会在栈内存分配一个栈帧,
    - 每执行完一次函数，都会释放相应的空间.
- 递归的优缺点
    - 缺点:占用内存多，效率低下
    - 优点:思路和代码简单
<br>

      '''使用递归来计算阶乘'''
      def fac(n):
          if n==1:
              return 1
          else:
              res=n*fac(n-1)
              return res

      print(fac(25))

      #斐波那契数列
      def fun(n):
          if n==1:
              return 1
          elif n==2:
              return 1
          else:
              res=fun(n-1)+fun(n-2)
              return res

      print(fun(6))
      for i in range(1,7):
          print(fun(i))

#### 函数总结：

<img src='https://user-images.githubusercontent.com/99107924/166904486-27f41c95-159f-4ca7-9fb7-e13e61d4498d.png'  width='1000' height="400" />


## 6异常处理
#### 1Bug的由来及其分类
#### 1.1粗心导致的语法错误
- Bug的由来
    - 世界上第一部用玩用计算机的进化版-马克2号
1. 漏了末尾的冒号，如if语句，循环语句,else子句等
2. 缩进错误，该缩进的没缩进，不该缩进的瞎缩进
3. 把英文符号写成中文符号，比如说:引号，冒号，括号
4. 字符串拼接的时候，把字符串和数字拼在一起
5. 没有定义变量，比如说while的循环条件的变量
6. “==”比较运算符和”=”赋值运算符的混用

- 粗心导致的语法错误

      '''age = (input('请输出你的年龄'))
      if age>=18:
          print('成年人')'''
      age = eval(input('请输出你的年龄'))
      if age>=18:
          print('成年人')

      '''
      while i<10: #i没有指定
          print（i） #采用中文符号 ,死循环'''
      i=0
      while i<10:
          print(i)
          i+=1

      '''for i in range(3):
          uname=input('请输入用户名：')
          pwd=input('请输入密码：')
          if uname='admin' and pwd='admin': # = 是赋值符号； == 是比较
              print('登陆成功')
              break
          else #没有冒号
              print('输入错位')
      else #没有冒号
          print('对不起，三次均输入错误')'''
      for i in range(3):
          uname=input('请输入用户名：')
          pwd=input('请输入密码：')
          if uname=='admin' and pwd=='admin':
              print('登陆成功')
              break
          else:
              print('输入错位')
      else:
          print('对不起，三次均输入错误')
  
#### 1.2知识点不熟练导致的错误
- 索引越界问题inderError

      lst=[11,22,33,44]
      #print(lst[4]) #IndexError: list index out of range
      print(lst[3])

- append()方法的使用掌握不熟练

      lst=[]
      #lst=append('A','B','C') #lst方法，append()只能放一个元素
      lst.append('A')
      print(lst)

#### 1.3思路不清导致的问题解决方案
- 使用print()函数
    - 使用#注释

            lst=[{'rating':[9.7, 2062397],'id':'1292052','type':['犯罪','剧情'],'title':'肖申克的救赎','actors':['蒂姆.罗宾斯','摩根·弗里曼']},
                {'rating' :[9.6, 1528760],'id':'1291546','type' :['剧情','爱情','同性'],'title':'霸王别姬','actors':['张国荣','张丰毅','巩俐','葛优']},
                {'rating':[9.5, 1559181],' id':'1292720','type':['剧情','爱情'],'title':'阿甘正传','actors':['汤姆.汉克斯','罗宾.怀特']}
                 ]

            name=input('请输入你要查询的演员:')
            for i in lst: #遍历列表 --> {} i 是一个又一个的字典
                act_lst=i['actors'] #找寻字典中的'actors' value 使用act_lst来接受key(列表)
                for actor in act_lst:
                    if name in actor:
                        print(name + ' 出演了:' + i['title'])
                '''for movie in i: #遍历字典，得到movie是一个字典中的key
                    print(movie)
                print('-------')
                actors=movie['actors']
                if name in actors:
                    print(name+'出演了:'+movie)'''

#### 1.4被动掉坑
- 程序代码逻辑没有错，只是因为用户错误操作或者一 些“例外情况”而导致的程序崩溃
- 被动掉坑问题的解决方案
    - Python提供了异常处理机制，可以在异常出现时即时捕获，然后内部“消化”，让程序继续运行

                  try:
                      a=int(input('请输入第一个整数'))
                      b=int(input('请输入第二个整数'))
                      result=a/b
                      print('结果为:',result)
                  except ZeroDivisionError:
                      print('对不起，除数不允许为0')
                  except ValueError:
                      print('只能输入数字串')
                  except BaseException as e:
                      print(e)
                  print('程序结束')
      - 多个except结构捕获异常的顺序按照先子类后父亲类的顺序，为了避免遗漏可能出现的异常，可以在最后增加BaseException

#### 2不同异常类型的处理方式
#### 3异常处理机制
#### PyCharm的调试模式

          
          
          
          
          
          
          
          
          
