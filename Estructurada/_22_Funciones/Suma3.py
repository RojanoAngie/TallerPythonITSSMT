def suma(a:int, b: int, c: int) -> int:
    return a+b+c

def suma(a, b, c):
    return a+b+c
if __name__ == '__main__':
    a:int=50
    b:int=200
    c:int=150

    print(suma(a,b,c))
    print(suma(str(a),str(b),str(c)))