c = input().strip().upper()
a = int(input())
b = int(input())
A = int(input())
B = int(input())
msj = int(input())

M = a*b-1
e = A*M+a
d = B*M+b
n = (e*d-1)/M


if  c == 'E':
	print(int(msj*e%n), end='')
else:
	print(int(msj*d%n), end='')
