
data=['6','/','!',':','!','#','7','$']
key=['t','h','e','_','f','l','a','g']
flag=[]
x=len(data)
y=len(key)
for i in range(y):
	a=ord(data[i])
	b=ord(key[i%x])
	flag.append(chr(a^b))
print("".join(x for x in flag))