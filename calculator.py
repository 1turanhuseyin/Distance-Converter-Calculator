from tkinter import *


def calculate():
    mile = float(user_input.get())
    result_output = 0

    if radio_state.get() == 1:
        result_output = round((mile * 1.609344), 1)
        warning_label.config(text="")
    elif radio_state.get() == 2:
        result_output = round((mile * 0.621371), 1)
        warning_label.config(text="")
    else:
        warning_label.config(text="Please select \nthe calculation method!")


    result_label.config(text=result_output)


def miles_to_kilometers_radiobutton():
    miles_label.config(text="Miles")
    km_label.config(text="Km")
    if user_input.get() != "":
        calculate()


def kilometers_to_miles_radiobutton():
    miles_label.config(text="Km")
    km_label.config(text="Miles")
    if user_input.get() != "":
        calculate()


window = Tk()
window.title("Mile to Km Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

radio_state = IntVar()
miles_to_km_radiobutton = Radiobutton(text="Miles to Kilometers", font=("Arial", 10, "bold"), value=1, variable=radio_state, command=miles_to_kilometers_radiobutton)
km_to_miles_radiobutton = Radiobutton(text="Kilometers to Miles", font=("Arial", 10, "bold"), borderwidth=16, value=2, variable=radio_state, command=kilometers_to_miles_radiobutton)
miles_to_km_radiobutton.grid(column=0, row=1)
km_to_miles_radiobutton.grid(column=0, row=2)

warning_label = Label(text="", font=("Arial", 16, "bold"), fg="red")
warning_label.grid(column=0, row=0)

user_input = Entry(width=8, font=("Arial", 16, "bold"))
user_input.grid(column=1, row=3)

miles_label = Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=2, row=3)
miles_label.config(padx=20)

is_equal_to_label = Label(text="is equal to", font=("Arial", 16, "bold"))
is_equal_to_label.grid(column=0, row=4)

result_label = Label(text="0", fg="red", font=("Arial", 16, "bold"))
result_label.grid(column=1, row=4)

km_label = Label(text="Km", font=("Arial", 16, "bold"))
km_label.grid(column=2, row=4)
miles_label.config(padx=20)

calculate_button = Button(text="Calculate", command=calculate, width=16, font=("Arial", 10, "normal"))
calculate_button.grid(column=1, row=5)





















window.mainloop()
