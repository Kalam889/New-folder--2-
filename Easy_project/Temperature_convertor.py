# unit = input("Enter temperature in fahrenheit or celsius. F/C: ").upper()
# temp = float(input("Enter temperature: "))

# if unit == "C":
#     convert = temp * 9/5 + 32
#     print(f"Temperature in fahrenheit is {convert}F.")
    
# elif unit == "F":
#     convert = (temp - 32) * 5/9
#     print(f"Temperature in celsius is {convert}C")
# else:
#     print("Please select valid input")

from tkinter import *
window = Tk()
window.title("Temperator conversion")
window.geometry("300x400")
def fahrenheit_to_celsius():
    fahrenheit_data = float(fahrenheit_entry.get())
    
    convert = (fahrenheit_data - 32) * 5/9
    celsius_entry.delete(0, END)
    celsius_entry.insert(0,f"{convert}")

def celsius_to_fahrenheit():
    celsius_data = float(celsius_entry.get())
    convert = celsius_data * 9/5 + 32
    fahrenheit_entry.delete(0, END)
    fahrenheit_entry.insert(0, f"{convert}")
    
def convert_both():
    fahrenheit_to_celsius()
    celsius_to_fahrenheit()


fahrenheit_label = Label(window,text="Fahrenheit")
fahrenheit_label.grid(row=0, column=0)
fahrenheit_entry = Entry(window)
fahrenheit_entry.grid(row=0, column=3,padx=10,pady=20)
celsius_label = Label(window,text="Celsius")
celsius_label.grid(row=1, column=0)
celsius_entry = Entry(window)
celsius_entry.grid(row=1, column=3,padx=10,pady=10)
btn = Button(window, text="Convert",command=convert_both)
btn.grid(column=3)
window.mainloop()



# from tkinter import *

# root = Tk()

# entry = Entry(root, font=("Arial", 14))
# entry.pack(pady=10)

# def show_text():
#     # user_text = entry.get()   # get() reads what user typed
#     entry.insert(0, "Hello, Kalam!")  # inserts at position 0

#     # print("You typed:", user_text)

# Button(root, text="Show Text", command=show_text).pack(pady=5)

# root.mainloop()
