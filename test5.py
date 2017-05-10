def wine():
    print('first yield...')
    x = yield 1
    print(x)
    print('second yield...')
    yield 2


ww = wine()
print(next(ww))
# print(ww.send(None))
print(ww.send('the result of first yield'))
# print(next(ww))


def winewithfinally():
    try:
        print('|first yield')
        x = yield 1
        print('+++', x)
        print('|second yield')
        yield 2
    except Exception:
        pass
    finally:
        print('yield is closed')


ww2 = winewithfinally()
print(ww2.send(None))
print(ww2.send(1))
print(ww2.close())


def wine4():
    if True:
        return 10
    else:
        yield 2

try:
    print(type(wine4()))
    print(next(wine4()))
except StopIteration as e:
    print('e.value:', e.value)