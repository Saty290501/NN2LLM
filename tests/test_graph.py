from src.foundations.graph import print_graph
from src.foundations.value import Value


def main():

    a = Value(2.0, label="a")
    b = Value(3.0, label="b")

    c = a * b
    c.label = "c"

    d = a + b
    d.label = "d"

    e = c + d
    e.label = "e"

    print("\nCOMPUTATIONAL GRAPH\n")

    print_graph(e)


if __name__ == "__main__":
    main()