from random import randint 
from time import sleep   
from datetime import datetime  
print (" chuong trinh lay gia tri ngau nhien")
try:  #ma thuc thi co the xay ra loi khi thuc thi cac cau lenh con
        while(1):
                temperature = randint(28,30) 
                humidity = randint(80,90)
                time_now = datetime.now()
                print ("cap nhat luc %s" %str(time_now))
                print(" nhiet do :%s" %str(temperature))
                print("do am: %s" %str(humidity))
                sleep(1)
except keyboardInterrupt:  #  except xay ra loi voi keybeord..
        print('chuong trinh ket thuc')

