n1=int(input(""))
n2=int(input(""))

if n1%2==0:
	res = n1*n2
elif n2%3==0:
	res = n1+n2
else:
	res=n1-n2

print(res)
input("")