import random


def adivinar_numero(numero):
    next = True
    user_number = int(input('Ingrese un numero: '))
    while (next):
        if (user_number > numero):
            user_number = int(input('Ingrese un numero menor: '))
        elif (user_number < numero):
            user_number = int(input('Ingrese un numero mayor: '))
        else:
            next = False
    print('Encontraste el número: ' + str(user_number))


def run():
    random_number = random.randint(0, 100)
    adivinar_numero(random_number)


if __name__ == '__main__':
    run()
