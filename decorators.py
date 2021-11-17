#En este simpático programa crearemos un decoradorque servirá 
#para saber cuanto tiempo dura ejecutándose una función

from datetime import datetime


def run():
    def execution_time(func):
        def wrapper(*args,**kwargs):
            initial_time = datetime.now()
            func(*args,**kwargs)
            final_time = datetime.now()
            time_elapse = final_time - initial_time
            print('pasaron ' + str(time_elapse.total_seconds()) + ' segundos')

        return wrapper


    @execution_time
    def random_func():
        for _ in range(1, 1000001):
            pass

    @execution_time
    def sum(a: int, b: int) -> int:
        return a + b

    @execution_time
    def saludo(name):
        print('Hola ' + name)


    random_func()
    sum(5, 5)
    saludo('Pedro')


if __name__ == '__main__':
    run()