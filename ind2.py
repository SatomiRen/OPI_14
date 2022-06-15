#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import pi, sin


class Angle:
    def __init__(self, degrees=0.0, minutes=0):
        self.__degrees = degrees
        self.__minutes = minutes
        self.__radians = 0

    def read(self):
        self.__degrees = float(input("Enter the degrees: "))
        self.__minutes = int(input("Enter the minutes: "))

    def to_degrees(self):
        return self.__degrees + self.__minutes / 60

    def to_radians(self):
        self.__radians = self.__degrees * pi / 180 \
                         + self.__minutes * pi / (180 * 60)
        return self.__radians

    def normalize_to_360(self):
        return self.to_degrees() % 360

    def inc_angle(self, value):
        self.__degrees += value
        print("The angle has been incremented")

    def dec_angle(self, value):
        self.__degrees -= value
        print("The angle has been decremented")

    def find_sin(self):
        return sin(self.to_radians())

    def compare(self, degrees):
        if self.to_degrees() == degrees:
            print(f"The angles {self.to_degrees()} and {degrees} are equal")
        else:
            print(
                f"The angles {self.to_degrees()} and {degrees} are not equal"
            )

    def display(self):
        print(f"The angle degrees: {self.__degrees}")
        print(f"The angle minutes: {self.__minutes}")
        print(f"The angle radians: {self.to_radians()}")
        print(f"The angle sin: {self.find_sin()}")


if __name__ == '__main__':
    print("The options are:\n"
          "1 - Convert to degrees\n"
          "2 - Convert to radians\n"
          "3 - Normalize to 0 - 360 diapason\n"
          "4 - Increment angle by the value\n"
          "5 - Decrement angle by the value\n"
          "6 - Find the sin of the angle\n"
          "7 - Compare with another angle\n"
          "8 - Read the angle degrees and minutes from the keyboard\n"
          "9 - Display the angle information\n"
          "0 - Exit the program\n"
          )
    angle = Angle()
    while True:
        command = int(input("Enter the command: "))
        if command == 1:
            print(angle.to_degrees())
        elif command == 2:
            print(angle.to_radians())
        elif command == 3:
            print(angle.normalize_to_360())
        elif command == 4:
            val = float(input("Enter the value to increment on: "))
            angle.inc_angle(val)
        elif command == 5:
            val = float(input("Enter the value to decrement on: "))
            angle.dec_angle(val)
        elif command == 6:
            print(angle.find_sin())
        elif command == 7:
            degrees2 = float(input("Enter the degrees of the 2nd angle"))
            minutes2 = int(input("Enter the minutes of the 2nd angle"))
            angle2 = Angle(degrees2, minutes2)
            angle.compare(angle2.to_degrees())
        elif command == 8:
            angle.read()
        elif command == 9:
            angle.display()
        elif command == 0:
            break
