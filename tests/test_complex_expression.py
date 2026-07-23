from src.foundations.value import Value


def main() -> None:
    # Input values
    a = Value(2.0, label="a")
    b = Value(3.0, label="b")
    c = Value(4.0, label="c")
    d = Value(5.0, label="d")

    # Step 1
    e = a * b

    # Step 2
    f = c + d

    # Step 3
    g = e + f

    # Step 4
    h = g ** 2

    # Step 5
    output = h / a

    print("========== INPUTS ==========")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"d = {d}")

    print("\n========== INTERMEDIATE ==========")
    print(f"e = {e}")
    print(f"f = {f}")
    print(f"g = {g}")
    print(f"h = {h}")

    print("\n========== OUTPUT ==========")
    print(output)

    # Assertions
    assert e.data == 6.0
    assert f.data == 9.0
    assert g.data == 15.0
    assert h.data == 225.0
    assert output.data == 112.5


if __name__ == "__main__":
    main()