## 1输出函数print  ##
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


## 2转义字符与元字符  ##

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


## 3二进制与字符编码  ##
      print(chr(0b100111001011000))
      print(ord('乘'))


##  4Python中的标识符和保留字  ##
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
  

##  5变量  ##
      #变量的定义和使用
      name = '玛丽亚'
      print(name)
      print('标识 ',id(name))
      print('类型 ',type(name))
      print('值   ',name)
      #变量的多次赋值
      name = '楚留冰'
      print(name)




























