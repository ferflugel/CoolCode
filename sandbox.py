def f():
    print('hi')
def five(k):
    k()
    k()
    k()
    k()
    k()
def four(l):
    l()
    l()
    l()
    l()
x = lambda : five(f)
y = lambda : five(x)
z = lambda : four(y)
w = lambda : four(f)
z()
w()
