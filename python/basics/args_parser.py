import argparse


def parseArgs():
    """
    Example of Argument Parser with required
    and optional args
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="The user name")                    # required
    parser.add_argument("-a", "--age", type=int, help="The user's age")  # optional
    args = parser.parse_args()

    if args.age: # check if optional is set
        print(f"User's name is {args.name} and he is {args.age} years old")
    else:
        print(f"User's name is {args.name}")


if __name__ == "__main__":
    parseArgs()
