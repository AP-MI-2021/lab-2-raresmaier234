def prime_number (n):
    ''''
    input: n intreg
    '''
    if n<2:
        return False
    for d in range(2, n):
        if n%d==0:
            return False
    return True


def get_largest_prime_below(n):
    '''
    Parametrul n reprezinta numarul citit de utilizator
    Vom determinat cel mai mare numar prim, strict mai mic ca n
    '''
    for i in range(n-1, 1, -1):
        if(prime_number(i)):
            return i

def test_get_largest_prime_below():
    assert prime_number(2) == True

def oglindit (n):
    og = 0
    while n:
        og=og*10+n%10
        n=n//10
    return og

def is_palindrom(n) -> bool:
    return bool(oglindit(n)==n)

def test_is_palindrom():
    assert is_palindrom(123) == False

def main():
    while True:
        print ('1. Determinarea celui mai mare numar prim mai mic ca numarul dat.')
        print ('2. Verificarea daca un numar este palindrom.')
        print ('x. Iesire din program.')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            val = int(input("Introdu numarul: "))
            print(f'Numarul prim strict mai mic ca numarul dat este: {get_largest_prime_below(val)} ')
        elif optiune == '2':
            val =  int(input("Introdu numarul: "))
            if is_palindrom(val):
                print('Numarul dat este palindrom')
            else:
                print('Numarul dat nu este palindrom')
        elif optiune == 'x':
            return False

test_get_largest_prime_below()
test_is_palindrom()
main()