# from operator import mul as mul_two

""" # type string
a="belle"
# type int
b=12
# type float
fl=98.6
# type lists
li=[3,4,5]
# type dict
di={"name":"Andrea","surname":"damato"}
# type tuples
tu=(1,"bello",40.2)
# type sets
se={1,2,3,4,5,6}
# type book
bo=False
# print("ciao" )

belle = {'name':'Belle','gender':'female','birth':2022}

print(belle['name'])
 """
""" num=8
print(num ** 3 )
print(type(tu)) """

""" # print('Python {r}'.format(r = 'rules!'))
def func (a: int, b:int) -> int:
    return mul_two(a,b)

assert func (3,5) == 15

print(func(2,4)) """
""" myfile = open('test.txt')

print(myfile.read())


myfile.close() """

""" # Create and write on a new file
with open('andrea.txt',mode='w') as f:
    f.write('hey whatsup \nAll good bro?')

# How to read a file and print on screen
with open('andrea.txt',mode='r') as f:
    print(f.read()) """

a=[1,2,3]
for item in a:
    print(item)