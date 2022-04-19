## 计算机组成原理  ##
#### 输出函数print()
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


#### 转义字符与元字符 

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


#### 二进制与字符编码 
      print(chr(0b100111001011000))
      print(ord('乘'))


####  Python中的标识符和保留字  
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
  

##  Python变量  ##
      #变量的定义和使用
      name = '玛丽亚'
      print(name)
      print('标识 ',id(name))
      print('类型 ',type(name))
      print('值   ',name)
      #变量的多次赋值
      name = '楚留冰'
      print(name)

### 数据类型  ##
##### 整数类型 --> int -->98
##### 浮点数类型 --> float --> 3.141519
##### 布尔类型 --> bool --> True,False
##### 字符串类型 --> str --> '人生苦短，我用python'

#### 整数类型
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

#### 浮点类型
      a = 3.14159
      print(a,type(a))
      n1 = 1.1
      n2 = 2.2
      print(n1+n2)

      #解决浮点数相加出现的精度问题
      from decimal import Decimal
      print(Decimal('1.1')+Decimal('2.2'))

#### 布尔类型
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

#### 字符串类型
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

#### 数据类型转换
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

#### 注释
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

##  流程控制语句  ##
#### Python的输出函数input()
#### input的高级使用
##### 从键盘录入两个整数，计算两个整数的和
      a = int(input('请输入一个加数：'))
      b = int(input('请输入另一个加数：'))
      #a = int(a) #将转换之后的结果存储到a中
      #b = int(b)
      print(type(a),type(b))
      print(a+b)
      
### Python的运算符
<img src="https://user-images.githubusercontent.com/99107924/163781347-de11782c-4cce-433f-bf5a-94e6b54ad781.png" width="600px" alt="Python运算符" />

***
***
***

#### 运算符1_算术运算符
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
#### 运算符2_赋值运算符
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
#### 运算符3_比较运算符
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


#### 运算符4_布尔运算符
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


#### 运算符5_位运算符
<img src="https://user-images.githubusercontent.com/99107924/164036205-e87af3c2-0bbd-41aa-a1b0-92b2dea4c8b3.png" width="650"/>



      print(4&8) #按位与&，同为1时结果为1
      print(4|8) #按位或|，同为0时结果为0
      print(4<<1) #左移一位（移动一个位置），相当于乘以2
      print(4<<2) #左移两位（移动两个位置），相当于乘以4

      print(4>>1) #右移一位，相当于除以2
      print(4>>2) #右移两位，相当于除以4




















