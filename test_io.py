
a = []
file = open("data.txt", "r")
for i in range(3):
	a.append(float(file.readline()))
file.close()
print(type(a[0]))
