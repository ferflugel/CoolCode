L = range(NUMBER, 0, -1)
def multiple_prints(_list):
    try:
        dummy = 100 / _list[0]
        print(':)' + str(_list[0]))
        multiple_prints(_list[1:])
    except:
        exit
multiple_prints(L)