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
z = lambda : four(lambda : five(lambda : five(f)))
w = lambda : four(f)
def final():
    z()
    w()
final()