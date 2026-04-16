def f(x):
    print("In f, x =", x)
    x += 5
    return x

def g(x):
    y = f(x*2)
    print("In g, x =", x)
    z = f(x*3)
    print("In g, x =", x)
    return y + z

print(g(2))
