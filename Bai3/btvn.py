def sxepgiam(n,a):
	for i in range(0,n):
		for j in range(i,n):
			if(a[i]<a[j]):
				t=a[i]
				a[i]=a[j]
				a[j]=t

	for i in range(len(a)):
		print (a[i]),
def sxeptang(n,a):
        for i in range(0,n):
                for j in range(i,n):
                        if(a[i]>a[j]):
                                t=a[i]
                                a[i]=a[j]
                                a[j]=t
	for i in range(len(a)):
                print (a[i]),

def gthua(b):
	if(b<2):
		return 1
	else:
		return(b*gthua(b-1))
def timmax(n,a):
	max=a[0]
	for i in range(0,n):
                 if(a[i]>max):
			max=a[i]
	print(max)
def timmin(n,a):
        min=a[0]
        for i in range(0,n):
                 if(a[i]<min):
                        min=a[i]
        print(min)

