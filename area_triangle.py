#!usr/bin/env python3
# Created By: Marli Peters
# Date: Nov. 28, 2023
# This program creates a function that asks user for the width and
# length of a triangle then calculates the area and displays it for them
# in the main function.


def triangle_area(base_str, height_str):
    try:
        base_int = int(base_str)
        height_int = int(height_str)

    except:
        print("Please enter valid integers")

    else:
        # calculate temperature in fahrenheit

        area = base_int * height_int / 2

        # display area

        if base_int <= 0 or height_int <= 0:
            print("Please enter positive numbers")
        else:
            print("The temperature in fahrenheit is {}cm^2.".format(area))


def main():
    # get base and height of triangle

    base_str = str(input("Enter the base of the triangle: "))
    height_str = str(input("Enter the height of the triangle: "))

    # call temp triangle area function

    triangle_area(base_str, height_str)


if __name__ == "__main__":
    main()
