import sys


def checkArgs():
    """
    Checks number of passed arguments. Remember that argv[0]
    is always the file name!
    :return: void
    """
    if len(sys.argv) != 3:  # 3 = 1 for program name + 2 arguments
        print("You should pass exactly two argument")
        return
    print("Program name is {}".format(sys.argv[0]))
    print(f"First passed argument is {sys.argv[1]}")
    print(f"Second passed argument is {sys.argv[2]}")
    intArg = int(sys.argv[2])
    floatArg = float(sys.argv[2])
    print(f"Second argument conversion int is {intArg} and float is {floatArg}")


if __name__ == "__main__":
    checkArgs()