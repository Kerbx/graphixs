"""
This project is a calculator with a simple graphics.
I want it to be done.
I hope i will finish it.


"""

# Trying to import necessary modules.
try:
    import sys
    import math
    import decimal as dcml # Using module for more accuracy that float has.
    import tkinter as tk
except ModuleNotFoundError:
    print("Can't import modules for work. Try to install necessary modules.")


# List with names for buttons.
buttons = ['1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0' '+', '-', '/', '*']


def main():
    """
    Main function that contains all of the main graphics as
    window, buttons, out-print window.
    """

    # Creating main window and give a title to it.
    window = tk.Tk()
    window.title('Чо это.')

    # This loop automatically creating buttons using "buttons" list.
    for i in buttons:
        pass

    window.mainloop()


main()
