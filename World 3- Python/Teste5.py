#B tem ligação com S
a= [2,3,4,7]
b=a
b[2] = 8
print(a)
print(b)
print(f'Lista a {a}')
print(f'Lista b {b}')


#B perde a ligação com A
a= [2,3,4,7]
b=a[:]
b[2] = 8
print(a)
print(b)
print(f'Lista a {a}')
print(f'Lista b {b}')
