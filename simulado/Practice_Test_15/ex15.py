# what is the expected behavior of the following snipped?

try:
    raise Exception
except:
    print('c')
except BaseException:
    print('c')
except Exception:
    print('b')