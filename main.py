from typing import Any


def prime_number(n):
    ''''
    input: n intreg
    '''
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def get_largest_prime_below(n):
    '''
    Parametrul n reprezinta numarul citit de utilizator
    Vom determinat cel mai mare numar prim, strict mai mic ca n
    '''
    for i in range(n - 1, 1, -1):
        if (prime_number(i)):
            return i


def get_base_2(n: str) -> str:
    ''''
    Variabila n_in_base2 va reprezenta scrierea in baza 2 a parametrului n scris in baza 10
    '''
    n_in_base2 = ""
    while n != 0:
        n_in_base2 = n_in_base2 + str(n % 2)
        n = n // 2
    return n_in_base2[::-1]

def test_get_base_2():
    assert get_base_2(12) == "1100"
    assert get_base_2(13) == "1101"
    assert get_base_2(15) == "1111"


def test_get_largest_prime_below():
    assert prime_number(2) == True
    assert prime_number(3) == True
    assert prime_number(4) == False


def oglindit(n):
    og = 0
    while n:
        og = og * 10 + n % 10
        n = n // 10
    return og


def is_palindrom(n) -> bool:
    return bool(oglindit(n) == n)


def test_is_palindrom():
    assert is_palindrom(123) == False
    assert is_palindrom(242) == True
    assert is_palindrom(2002) == True


def main():
    while True:
        print('1. Determinarea celui mai mare numar prim mai mic ca numarul dat.')
        print('2. Verificarea daca un numar este palindrom.')
        print('3. Scrierea unui numar din baza 10 in baza 2.')
        print('x. Iesire din program.')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            val = int(input("Introdu numarul: "))
            print(f'Numarul prim strict mai mic ca numarul dat este: {get_largest_prime_below(val)} ')
        elif optiune == '2':
            val = int(input("Introdu numarul: "))
            if is_palindrom(val):
                print('Numarul dat este palindrom')
            else:
                print('Numarul dat nu este palindrom')
        elif optiune == '3':
            val = int(input("Introdu numarul: "))
            print(get_base_2(val))
        elif optiune == 'x':
            return False


test_get_base_2()
test_get_largest_prime_below()
test_is_palindrom()

if __name__ == '__main__':
    main()
