v1=int(input(""))
op=int(input(""))
v2=int(input(""))

if op == 0:
	res = v1+v2
elif op ==1:
	res = v1- v2
elif op ==2:
	res = v1//v2
elif op ==3:
	res = v1*v2

print(res)