##  第1关：原码转换  ##

                  N = 8             #位数为8  
                  ########## Begin ##########  
                  def ZhenToYuan(z): #真实值→原码  
                      if z[0] not in ['+', '-']:    #若无符号  
                          z = '+' + z                 #则补上正号，便于后面统一处理  
                      y = '0' if (z[0] == '+') else '1' #转换符号位  
                      y = y+'0'*(N-len(z))            #补0  
                      y = y+z[1:len(z)]               #转换数字部分  
                      return y  
                  ########## End ##########  
                  z = input()        #真实值  
                  y = ZhenToYuan(z)  #转换成8位原码  
                  print('%s -> %s' % (z, y))
      
#### https://blog.csdn.net/qq_40498551/article/details/89278247        CSDN学习def()函数用法
#### https://blog.csdn.net/faihung/article/details/84587387            CSDN学习列表字符串转换
 
##  第2关：反码转换  ##



                  N = 8             #位数为8
                  ########## Begin ##########
                  def ZhenToYuan(z): #真实值→原码
                      if z[0] not in ['+', '-']:    #若无符号
                          z='+' + z                 #则补上正号，便于后面统一处理
                      y = '0' if (z[0] == '+') else '1' #转换符号位
                      y = y+'0'*(N-len(z))            #补0
                      y = y+z[1:len(z)]               #转换数字部分
                      return y
                  def QuFan(y):   #数字部分按位取反
                      f=y[0]                        #符号位不变
                      for x in y[1:len(y)]:         #数字部分按位取反
                          if x == '1':
                              f = f+'0'
                          else:
                              f = f+'1'
                      return f
                  def ZhuanFan(z): #真实值-->反码
                      y = ZhuanYuan(z)            #先求原码
                      if y[0] == 0:               #若为正
                          return y                #反码等于原码
                      else:                       #否则为负
                          return QuFan(y)         #原码按位取反再加1

                  ########## End ##########
                  z = input()       #真实值
                  f = ZhuanFan(z)  #转换成8位反码
                  print('%s -> %s' % (z, f))
                  
### python 直接替换列表中的元素的方法

                  aaa=['Black','Red','White','Black']
                  bbb=['Yellow' if i =='Black' else i for i in aaa]
                  bbb

                  结果：
                  ['Yellow', 'Red', 'White', 'Yellow']
                  
           
      
 ##  第3关：补码转换  ##
 



                  N = 8             #位数为8
                  ########## Begin ##########
                  def ZhuanYuan(z):#真实值→原码
                      if z[0] not in ['+', '-']:    #若无符号
                          z='+' + z                 #则补上正号，便于后面统一处理
                      y = '0' if (z[0] == '+') else '1' #转换符号位
                      y = y+'0'*(N-len(z))            #补0
                      y = y+z[1:len(z)]               #转换数字部分
                      return y
                  def QuFan(y):   #数字部分按位取反
                      f=y[0]                        #符号位不变
                      for x in y[1:len(y)]:         #数字部分按位取反
                          if x == '1':
                              f = f+'0'
                          else:
                              f = f+'1'
                      return f
                  def PlusOne(f):   #加1
                      if f == '1'*N:                   #若为全1
                          return '0'*N               #直接返回全0
                      for i in range(len(f)):        #找最后一个0（肯定能找到，因为全1情况之前已处理）
                          if f[i] == '0':
                              pos = i
                      b = f[0:pos]                   #前面不变
                      b = b+'1'                      #最后一个0变为1
                      b = b+'0'*(len(f)-(pos+1))     #后面全0
                      return b
                  def ZhuanBu(z):  #真实值→补码
                      y=ZhuanYuan(z)                #先求原码
                      if y[0]=='0':                  #若为正
                          return y                   #补码等于原码
                      else:                          #否则为负
                          return PlusOne(QuFan(y)) #原码按位取反再加1
                  ########## End ##########
                  z = input()       #真实值
                  b = ZhuanBu(z)   #转换成8位补码
                  print('%s -> %s' % (z, b))


### 反码加 1 运算的思路：若反码是全 1，则直接返回全 0；否则找到最后一个 0，将其变为 1，其后为全 0，而前面保持不变，如下图。

![image (15)](https://user-images.githubusercontent.com/99107924/161666917-5e71cbf8-7949-4219-a41e-baefc963a372.png)


##  第4关：定点数  ##


## 定点小数

                  N = 8             #位数为8
                  ########## Begin ##########
                  def remove_char(str, n):
                      front = str[:n]  # 取去掉东西之后的数
                      back = str[n + 1:]  # 取去掉东西之前的数
                      return front + back
                  def ZhuanYuan_point(z):
                      if z[0] not in ['+', '-']:    #若无符号
                          z='+' + z                 #则补上正号，便于后面统一处理
                      y = '0' if (z[0] == '+') else '1' #转换符号位
                      y = y+z[3:len(z)]               #转换数字部分
                      y = y+'0'*(N-len(y))            #补0
                      return y
                  def ZhuanBu_point(z):
                      y = ZhuanYuan_point(z)
                      if y[0] == '0':  # 若为正
                          return y  # 补码等于原码
                      else:  # 否则为负
                          return PlusOne(QuFan(y))  # 原码按位取反再加1
                  ########## End ##########
                  z = input()             #真实值
                  y = ZhuanYuan_point(z) #求定点小数（原码形式）
                  b = ZhuanBu_point(z)#求定点小数（补码形式）
                  print('%s -> %s -> %s' % (z, y, b))



##  第5关：浮点数  ##


                  import myCoding                     #myCoding是原反补码辅助库
                  N = 8             #位数为8
                  ########## Begin ##########
                  def QiuEM(z): #求z的科学计数形式中的阶码和尾数
                      idx_point = z.index('.')         #小数点的编号
                      idx_firstOne = z.index('1')      #首个1的编号
                      idx_lastOne = 0                  #最后一个1的编号
                      for i in range(len(z)):
                          if z[i] == '1':
                              idx_lastOne = i
                      if idx_point > idx_firstOne:       #若不是纯小数，如'+10.0001'
                          E = idx_point-idx_firstOne   #则阶码是小数点编号减去首个1的编号
                      else:                            #否则是纯小数,如'+0.0001'
                          E = idx_point-idx_firstOne+1 #则阶码是小数点编号减去首个1的编号，再加1
                      E = bin(E)                       #将阶码转换成二进制
                      E = E.replace('0b','')           #删去二进制里面的'0b'
                      M = z[idx_firstOne:idx_lastOne+1]#提取从首个1到末个1的部分，如'+10.01'中提取'10.01'
                      M = M.replace('.','')            #删除这部分的小数点
                      M = z[0]+'0.'+M                  #在最开始处补上符号和'0.'
                      return M,E
                  def ZhuanFu(z):  #真实值→浮点数
                      if z == '0':                       #若为0
                          return '0'*N+' '+'0'*N       #直接返回全0（中间有个空格）
                      if z[0] not in ['+', '-']:       #若无符号
                          z = '+'+z                    #则在最前补上正号，便于统一处理
                      if '.' not in z:                 #若无小数点
                          z = z+'.'                    #则在最后补上小数点，便于统一处理
                      M,E = QiuEM(z)             #获取阶码和尾数
                      M = myCoding.ZhuanYuan_point(M) #将尾数转换成定点小数（原码形式）
                      M = myCoding.ZhuanBu_point(M)         #求定点小数的补码
                      E = myCoding.ZhuanYuan(E)   #将阶码转换成定点整数（原码形式）
                      E = myCoding.ZhuanBu(E)         #求定点整数的补码
                      return E+' '+M                   #阶码在前、尾数在后，中间有个空格
                  ########## End ##########% (z, f))
                  z = input()            #真实值
                  f = ZhuanFu(z)        #转换成浮点数
                  print('%s -> %s' % (z, f))
                  

### 辅助图片：

![image (16)](https://user-images.githubusercontent.com/99107924/161673971-b7c5b41a-ea54-498e-b2df-dd17a7448b10.png)


### myCording库：



                  ## 原码
                  N = 8             #位数为8
                  ########## Begin ##########
                  def ZhenToYuan(z): #真实值→原码
                      if z[0] not in ['+', '-']:    #若无符号
                          num='+' + z                #则补上正号，便于后面统一处理
                          y='0' if (z[0]=='+') else '1' #转换符号位
                          y=y+'0'*(N-len(num))            #补0
                          y=y+z[1:len(num)]               #转换数字部分
                          return y
                  ######### End ##########

                  ## 反码
                  N = 8             #位数为8
                  ########## Begin ##########
                  def ZhuanYuan(z): #真实值→原码
                      if z[0] not in ['+', '-']:    #若无符号
                              z='+' + z                 #则补上正号，便于后面统一处理
                      y = '0' if (z[0] == '+') else '1' #转换符号位
                      y = y+'0'*(N-len(z))            #补0
                      y = y+z[1:len(z)]               #转换数字部分
                      return y
                  def QuFan(y):   #数字部分按位取反
                    f=y[0]                        #符号位不变
                    for x in y[1:len(y)]:         #数字部分按位取反
                        if x == '1':
                            f = f+'0'
                        else:
                            f = f+'1'
                    return f
                  def ZhuanFan(z): #真实值-->反码
                    y = ZhuanYuan(z)            #先求原码
                    if y[0] == 0:               #若为正
                        return y                #反码等于原码
                    else:                       #否则为负
                        return QuFan(y)         #原码按位取反再加1

                  ########## End ##########


                  ## 补码
                  N = 8  # 位数为8
                  ########## Begin ##########
                  def ZhuanYuan(z):  # 真实值→原码
                      if z[0] not in ['+', '-']:  # 若无符号
                          z = '+' + z  # 则补上正号，便于后面统一处理
                      y = '0' if (z[0] == '+') else '1'  # 转换符号位
                      y = y + '0' * (N - len(z))  # 补0
                      y = y + z[1:len(z)]  # 转换数字部分
                      return y
                  def QuFan(y):  # 数字部分按位取反
                      f = y[0]  # 符号位不变
                      for x in y[1:len(y)]:  # 数字部分按位取反
                          if x == '1':
                              f = f + '0'
                          else:
                              f = f + '1'
                      return f
                  def PlusOne(f):  # 加1
                      if f == '1' * N:  # 若为全1
                          return '0' * N  # 直接返回全0
                      for i in range(len(f)):  # 找最后一个0（肯定能找到，因为全1情况之前已处理）
                          if f[i] == '0':
                              pos = i
                      b = f[0:pos]  # 前面不变
                      b = b + '1'  # 最后一个0变为1
                      b = b + '0' * (len(f) - (pos + 1))  # 后面全0
                      return b
                  def ZhuanBu(z):  # 真实值→补码
                      y = ZhuanYuan(z)  # 先求原码
                      if y[0] == '0':  # 若为正
                          return y  # 补码等于原码
                      else:  # 否则为负
                          return PlusOne(QuFan(y))  # 原码按位取反再加1

                  ## 定点小数

                  N = 8             #位数为8
                  ########## Begin ##########
                  def remove_char(str, n):
                      front = str[:n]  # 取去掉东西之后的数
                      back = str[n + 1:]  # 取去掉东西之前的数
                      return front + back
                  def ZhuanYuan_point(z):
                      if z[0] not in ['+', '-']:    #若无符号
                          z='+' + z                 #则补上正号，便于后面统一处理
                      y = '0' if (z[0] == '+') else '1' #转换符号位
                      y = y+z[3:len(z)]               #转换数字部分
                      y = y+'0'*(N-len(y))            #补0
                      return y
                  def ZhuanBu_point(y):
                      if y[0] == '0':  # 若为正
                          return y  # 补码等于原码
                      else:  # 否则为负
                          return PlusOne(QuFan(y))  # 原码按位取反再加1
                  ########## End ##########

#### 最后如果想加，就把ZhuanFu函数也加入到myCording库中：


      N = 8             #位数为8
      ########## Begin ##########
      def QiuEM(z): #求z的科学计数形式中的阶码和尾数
          idx_point = z.index('.')         #小数点的编号
          idx_firstOne = z.index('1')      #首个1的编号
          idx_lastOne = 0                  #最后一个1的编号
          for i in range(len(z)):
              if z[i] == '1':
                  idx_lastOne = i
          if idx_point > idx_firstOne:       #若不是纯小数，如'+10.0001'
              E = idx_point-idx_firstOne   #则阶码是小数点编号减去首个1的编号
          else:                            #否则是纯小数,如'+0.0001'
              E = idx_point-idx_firstOne+1 #则阶码是小数点编号减去首个1的编号，再加1
          E = bin(E)                       #将阶码转换成二进制
          E = E.replace('0b','')           #删去二进制里面的'0b'
          M = z[idx_firstOne:idx_lastOne+1]#提取从首个1到末个1的部分，如'+10.01'中提取'10.01'
          M = M.replace('.','')            #删除这部分的小数点
          M = z[0]+'0.'+M                  #在最开始处补上符号和'0.'
          return M,E
      def ZhuanFu(z):  #真实值→浮点数
          if z == '0':                       #若为0
              return '0'*N+' '+'0'*N       #直接返回全0（中间有个空格）
          if z[0] not in ['+', '-']:       #若无符号
              z = '+'+z                    #则在最前补上正号，便于统一处理
          if '.' not in z:                 #若无小数点
              z = z+'.'                    #则在最后补上小数点，便于统一处理
          M,E = QiuEM(z)             #获取阶码和尾数
          M = ZhuanYuan_point(M) #将尾数转换成定点小数（原码形式）
          M = ZhuanBu_point(M)         #求定点小数的补码
          E = ZhuanYuan(E)   #将阶码转换成定点整数（原码形式）
          E = ZhuanBu(E)         #求定点整数的补码
          return E+' '+M                   #阶码在前、尾数在后，中间有个空格
          
          
#### 这样一个完整的原反补码就完成了。
