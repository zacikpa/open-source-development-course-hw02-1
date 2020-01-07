from ossdev import Vector


def main():
    a = Vector([0, 1, 2, 3, 4])
    b = Vector([4, 3, 2, 1, 0])
    print('Vector a: %s' % a)
    print('Vector b: %s' % b)
    print('Vector a+2: %s' % (a+2))
    print('Vector a+b: %s' % (a+b))


if __name__ == '__main__':
    main()
