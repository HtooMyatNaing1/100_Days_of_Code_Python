import tkinter

def mile_to_km():
    mile = mile_input.get()
    km = float(mile)*1.609
    km_result_label.config(text=f"{round(km, 2)}")
    return km

window = tkinter.Tk()
window.title("Mile to Kilometer Converter")

window.config(padx=20, pady=20)

mile_input = tkinter.Entry(width=7)
mile_input.grid(column=1, row=0)

mile_label = tkinter.Label(text="miles")
mile_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = tkinter.Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
