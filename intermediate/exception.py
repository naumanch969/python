# a = 5 + 'string'; print(a)- TypeError
# import somemodule         - ImportError
# a = b                     - NameError
# f = open('somefile.txt')  - 
# a = [1,2,4]; a.remove(4)  - 
# a = [12,2,4]; print(a[5]) - IndexError
# mydict = {'x':'d','y':'e'}
# print(mydict['z'])        - KeyError

# x = -5
# assert ( x > 5 ), 'x is not positive'   - AssertionError

try: a = 5/0
except Exception as e : print(e)
else: print('no error occur')
finally: print('run anyway')



class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value) -> None:
        self.message = message
        self.value = value

def test_value(x):
    if x > 100: raise ValueTooHighError('value is too high')
    elif x < -100: raise ValueTooSmallError('Value is too small',x)

try:
    test_value(-200)
except ValueTooHighError as e :
    print(e)
except ValueTooSmallError as e :
    print(e.message,e.value)