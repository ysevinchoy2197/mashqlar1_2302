#1-misol
def raqam(a, b):
    c = a * a, b * b
    return c
x = raqam(1, 6)
print(f"Kvadrat: {x}")


#2-misol
def qoshish(a, b):
    return  a + b
res = qoshish(12, 2)
print(res)


#3-misol
def faktorial(n):
    f = 2
    for i in range(2, n + 1):
        f *= i
        return f
print(faktorial(5))

