
# Online Python - IDE, Editor, Compiler, Interpreter

a = 1
b = 1
n = 0
fibonacci_50 = []

for n in range(0,25):
    fibonacci_50.append(a)
    fibonacci_50.append(b)
    a+=b
    b+=a
    n+=1
else: 
    print(len(fibonacci_50))
