##  第1关：原码转换  ##


      N = 8             #位数为8
      ########## Begin ##########
      def ZhenToYuan(num):
          num = list(num)
          if num[0] == '+':
              num[0] = '0'
          elif num[0] == '-':
              num[0] = '1'
          else:
              num.insert(0,'0')
          a = N -len(num)
          for i in range(1,a+1):
              num.insert(1,'0')
          num = ''.join(num)
          return num

      ########## End ##########
      z = input()        #真实值
      y = ZhenToYuan(z)  #转换成8位原码
      print('%s -> %s' % (z, y))
      
#### https://blog.csdn.net/qq_40498551/article/details/89278247        CSDN学习def()函数用法
#### https://blog.csdn.net/faihung/article/details/84587387            CSDN学习列表字符串转换
 
