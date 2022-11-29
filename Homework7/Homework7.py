import sys
from functools import wraps
ENABLE_TRACE = True # False

def super_trace(func=None, *, file=sys.stdout):
    if func is None:
        def deco(func):
            return super_trace(func, file=file)
        return deco

    @wraps(func)
    def wrapper(*args, **kwargs):
        if ENABLE_TRACE:
            res1 = len(args)
            res2 = []
            for item in args:
                res2.append(tuple((item, type(item))))
            res3 = len(kwargs)
            res4 = []
            for item in kwargs:
                res4.append(tuple((item, type(item))))
            res5 = []

            if func(*args, **kwargs) is None:
                res5.append(('Func reurns None'))
            else:
                res5.append((len(func(*args, **kwargs)), type(func(*args, **kwargs)), func(*args, **kwargs)))
            print(f'1. {res1}')
            print(f'2. {res2}')
            print(f'3. {res3}')
            print(f'4. {res4}')
            print(f'5. {res5}')
            print()
        else:
            return func(*args, **kwargs)
    return wrapper


@super_trace(file=sys.stderr)
def test1(a, b, c):
    return [a, b, c], a, str(b), float(c)


@super_trace()
def test2(a, b, *, c, d):
    return [a, b, c, d], a, str(b), float(c), d


@super_trace(file=sys.stderr)
def test3(*, a, b, c, d):
    return [a, b, c, d], a, str(b), float(c), d


@super_trace()
def test4(a, b, *, c, d):
    print([a, b, c, d], a, str(b), float(c), d)


@super_trace()
def test5():
    return [1, 2, 3]



if __name__ == '__main__':
   # test ENABLE_TRACE = False
   ENABLE_TRACE = False
   test1(1, 2, 3)
   test2(1, 2, c=3, d=4)
   test3(a=1, b=2, c=3, d=4)
   test4(1, 2, c=3, d=4)
   test5()

   # test ENABLE_TRACE = True
   ENABLE_TRACE = True
   test1(1, 2, 3)
   test2(1, 2, c=3, d=4)
   test3(a=1, b=2, c=3, d=4)
   test4(1, 2, c=3, d=4)
   test5()