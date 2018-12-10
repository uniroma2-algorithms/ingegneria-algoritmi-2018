"""
    File name: repeat.py
    Author: Ovidiu Daniel Barba
    Date created: 10/12/2018
    Python Version: 3.7

    Decorator che ripete più volte la stessa funzione
"""

def repeat(num_times=2):
    """
    Funzione che ritorna un decorator
    :param num_times:
    :return:
    """
    def repeat_decorator(func):
        """
        Decorator che ripete num_times volte la funzione func
        :param func:
        :return:
        """
        def wrap_func(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrap_func
    return repeat_decorator


@repeat(num_times=100)
def printer():
    print("I'm printing once")


if __name__ == "__main__":
    printer()