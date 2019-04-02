def cong(a,b):
	return(a+b)
def tru(a,b):
	return(a-b)
def nhan(a,b):
	return(a*b)
def chia(a,b):
	return(a/b)
# n la so phan tu , d la mang
n=int(input('nhap so ptu ='))
d=[]
def  nhapmang(n,d):
	for i in  range(n):		
		d.append(input())
		print(d)


a=int(input('nhap a =' ))
b=int(input('nhap b = '))

print('tong = %d ' %cong(a,b))
print('hieu = %d ' %tru(a,b))
print('tich = %d ' %nhan(a,b))
print('thuong = %f ' %chia(a,b))
print(n)
print(d)
nhapmang(n,d) 
k=sorted(d)
print("sxeptang " ,k) # sxep tang dan
c=sorted(d,reverse= True) # sxep giam dan
print("sxepgiam " ,c)
print ("max = ",max(d))  # tim max
print("min = ",min(d)) # tim min
d2=[[1,4,2],[2,3,4],[5,6,7]]
d3=sorted(d2)  # sxep theo chieu tang dan tong 1 hang
d4=sorted(d2,reverse= True)  # sxep theo chieu giam dan tong cua hang
print(d2)
print("sxeptangmang " ,d3)
print("sxepgiammang" ,d4)

