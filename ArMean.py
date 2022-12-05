n = int(input('enter the size of the array '))
a = []
for i in range(0,n):
	a.append(int(input('Enter number ')))
a.sort()
print(a)
b = sum(a) / len(a)
c = sum(i**2 for i in a) / n
print('Arithmetical Mean =',b)
disp = c - b**2
print('Dispersion of array = ', disp)
