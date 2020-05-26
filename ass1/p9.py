#to find harmonic divisor no.


nos = []
print("Harmonic Divisor Numbers are:")
for x in range(6,10000):
	if len(nos)>10:
		break
	list = []
	for i in range(1, x+1):
		if x%i == 0:
			list.append(i)
	sum=0
	for j in range(len(list)):
		sum=sum+(1/list[j])
	har = len(list)/sum
	if har.is_integer() :
		print(x)
		nos.append(x)

