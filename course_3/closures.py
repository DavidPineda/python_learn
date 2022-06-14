def my_closure(num: int):
    def my_nested_function(string: str) -> str:
        assert type(string) == str, 'Solo puedes ingresar cadenas'
        return f'{string} ' * num

    return my_nested_function


def run():
    data_one: str = input('Ingrese la palabra: ')
    data_two: int = int(input('Ingrese la cantidad de veces a repetir: '))
    test = my_closure(data_two)
    result: str = test(data_one)
    print(result)


if __name__ == '__main__':
    run()
