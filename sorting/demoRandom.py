import random


if __name__ == "__main__":
    random.seed(1)
    for i in range(10):
        print(random.randint(0, 10))
    print("\n")
    random.seed(1)
    for i in range(10):
        print(random.randint(0, 10))
    print("\n")
    random.seed(12345)
    for i in range(10):
        print(random.randint(0, 10))
