from src.foundations.value import Value


def main():

    a = Value(12.0, label="a")
    b = Value(4.0, label="b")
    print(a)
    print(b)
    print()

    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    power = b ** 2

    print(add)
    print(sub)
    print(mul)
    print(div)
    print(power)

    assert add.data == 16.0
    assert sub.data == 8.0
    assert mul.data == 48.0
    assert div.data == 3.0
    assert power.data == 16.0


if __name__ == "__main__":
    main()