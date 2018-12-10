"""
    File name: cache.py
    Author: Ovidiu Daniel Barba
    Date created: 10/12/2018
    Python Version: 3.7

    Decorator per velocizzare per funzioni ricorsive
"""


def functionCallCache(func):
    """
    Decorator che mantiene il risultato delle funzioni in
    un dizionario, dove le chiavi sono gli argomenti passati alle
    funzioni e i valori, i risultati della funzione chiamata con
    quei argomenti.
    Utile nelle funzioni ricorsive
    :param func: ricorsiva
    :return: funzione
    """
    cached_values = {}  # mantiene il risultato delle funzioni chiamate

    def wrapFunction(*args, **kwargs):
        if args not in cached_values:
            # salva il risultato della funzione
            cached_values[args] = func(*args, **kwargs)
        return cached_values[args]
    return wrapFunction


@functionCallCache
def fibonacci(n):
    print(f'Calling fibonacci({n})')
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(10))
    print(fibonacci(250))
    # print([fibonacci(n) for n in range(10000)])