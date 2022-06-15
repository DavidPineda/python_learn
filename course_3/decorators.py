from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Time elapsed is: {str(time_elapsed.total_seconds())} seconds')
    return wrapper

@execution_time
def ramdom_func():
    for _ in range(1, 100000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre: str = 'David') -> str:
    return f'Hola {nombre}'


if __name__ == '__main__':
    ramdom_func()
    suma(5, 10)
    saludo('Alejandra')
