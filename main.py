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
    import functions_class
except ModuleNotFoundError:
    print("Can't import modules for work. Try to install necessary modules.")


# List with names for buttons.
list_of_buttons = ['1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', '+', '-', '/', '*',
            '=', 'x!', 'Pi', 'CE',]


# Creating main window and give a title to it.
window = tk.Tk()
window.title('Чо это.')

# Creating Entry window for displaying numbers and actions.
calculating_display = tk.Entry(window, width=50)
calculating_display.grid(row=0, column=0, columnspan=50)

# Creating class object for functions.
func = functions_class.Functions()


def main():
    """
    Main function that contains all of the main graphics as
    window, buttons, out-print window.
    """

    # Variables for loop. Need for griding buttons.
    _column = 0
    _row = 1

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

    # If key is '=' -> using eval function that calculating
    # existing in Enrty field expression.
    if key == '=':
        try:
            # Calculating result...
            result = eval(calculating_display.get())

            # Then display '=' and after that we can display result.
            # In other way -> SyntaxError while calculating because
            # eval() does not understand '=' symbol.
            calculating_display.insert(tk.END, key)
            calculating_display.insert(tk.END, result)
        except SyntaxError:
            # Deleting all.
            calculating_display.delete(0, tk.END)
            # Show error.
            calculating_display.insert(tk.END,\
                    'Error. Clear display when more than one "=" in line.')
            # Wait for 2 seconds and clear display again.
            calculating_display.after(2000,\
                        lambda: calculating_display.delete(0, tk.END))

    # Using function class.
    elif key == 'x!':
        # Calculating factorial.
        calculating_display.insert(tk.END, '=' +\
                                str(func.factor(int(\
                                calculating_display.get()))))

    elif key == 'Pi':
        # Display pi.
        calculating_display.insert(tk.END, func.pi())

    # Clear display.
    elif key == 'CE':
        calculating_display.delete(0, tk.END)

    else:
        # Display pressed key.
        calculating_display.insert(tk.END, key)



if __name__ == "__main__":

    main()
