"""
    File name: fib_profiling.py
    Author: Ovidiu Daniel Barba
    Date created: 1/10/2018
    Python Version: 3.7

    Profiling delle varie implementazioni di Fibonacci (2,3,4)
    usando cProfile e pstats
"""
import pstats
import cProfile
import fibonacci

fibNumber = 35                      # fibonacci number used
statsFileName = "fib_stats"         # statistics output names


def fib_profile():
    """
    Chiama le varie versioni di Fibonacci per
    avere statistiche sul tempo di esecuzione
    :return:
    """
    fibonacci.fibonacci2(fibNumber)
    fibonacci.fibonacci3(fibNumber)
    fibonacci.fibonacci4(fibNumber)


if __name__ == "__main__":
    cProfile.run('fib_profile()', statsFileName)
    stats = pstats.Stats(statsFileName)
    stats.strip_dirs().sort_stats('time').print_stats()
