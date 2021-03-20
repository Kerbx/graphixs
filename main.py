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
list_of_buttons = ['1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', '+', '-', '/', '*',]


def main():
    """
    Main function that contains all of the main graphics as
    window, buttons, out-print window.
    """

    # Creating main window and give a title to it.
    window = tk.Tk()
    window.title('Чо это.')

    # Variables for loop. Need for griding buttons.
    _column = 0
    _row = 1

    # Creating Entry window for displaying numbers and actions.
    calculating_display = tk.Entry(window, width=30)
    calculating_display.grid(row=0, column=0, columnspan=5)

    # This loop automatically creating buttons using "buttons" list.
    for _key in list_of_buttons:
        # Lambda function for buttons. It calls calculating function.
        command_for_button = lambda key = _key: foo(key)

        # Creating button and grid it in window.
        button = tk.Button(window, text=_key,\
                        command=command_for_button, width=5)
        # Griding created button.
        button.grid(row=_row, column=_column)

        # Automatically changing row and column values for griding.
        _column += 1
        # If there are 3 buttons in a row -> creating new row.
        if _column == 3:
            _row += 1
            _column = 0 # Reset to zero to make a row after fow.

    # Create window and start mainloop.
    window.mainloop()


def foo(key): # Temporate name for function.
    """
    Function for buttons.
    When clicked -> name of button displays on Entry field.
    This function maybe will be used for calculating.

    """

    pass


if __name__ == "__main__":
    main()
