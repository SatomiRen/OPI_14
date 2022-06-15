#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_number(s):
    try:
        float(s)
    except ValueError:
        return False
    return True


def make_product(first, second):
    if is_number(first) and is_number(second) and first > 0 and second > 0:
        product = Product(first, second)
        return product
    else:
        raise ValueError


class Product:
    def __init__(self, first=0.0, second=0):
        if is_number(first) and is_number(second):
            if first > 0 and second > 0:
                self.__first = first
                self.__second = second
            else:
                raise ValueError
        else:
            raise ValueError

    def read(self):
        self.__first = float(input("Enter the first value: "))
        self.__second = int(input("Enter the second value: "))

    def display(self):
        print(f"First value: {self.__first}")
        print(f"Second value: {self.__second}")

    def cost(self):
        return self.__first * self.__second


if __name__ == '__main__':
    p1 = make_product(2.25, 4)
    p1.display()
    print(f"The product's cost: {p1.cost()}")
    p1.read()
    print(f"The product's cost: {p1.cost()}")
    p2 = make_product("aadfd", 4)
    p2.display()
    p2.cost()
