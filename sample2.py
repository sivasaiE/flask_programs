# Custom Exception

class EvenError(Exception):
    pass
def fun():
    try:
        n = int(input())
        if n%2!=0:
            print(n*2)
        else:
            raise EvenError('num is already even')
    except EvenError():
        
fun()
