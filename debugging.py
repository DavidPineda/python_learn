def divisors(num):
    return [i for i in range(1, num + 1) if num % i == 0]


def run():
    is_correct = False
    while is_correct == False:
        num = input('Ingresa un numero: ')
        try:
            if int(num) < 0:
                raise ValueError('Por favor ingrese un número positivo')
            num = int(num)
            is_correct = True
            print(divisors(num))
            print('Termino mi programa')
        except ValueError as ve:
            print(ve)


if __name__ == '__main__':
    run()
