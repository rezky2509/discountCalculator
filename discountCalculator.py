import tkinter as tk

# creates the main application window
# Instantiate or initialize
root = tk.Tk()

# Name the application label 
root.title('Discount Calculator')

# Set the Window size 
root.geometry('400x400') 

# Label for Original Price
tk.Label(root, text="Original Price",justify="center").grid(row=0, column=2)
# Placed the label inside the window
# Input field for original Price
entry1 = tk.Entry(root)
entry1.grid(row=1, column=2)

# Label for Discount
tk.Label(root, text="Discount",justify="center").grid(row=2, column=2)
# Input Field for Discount
entry2 = tk.Entry(root)
entry2.grid(row=3, column=2)


def calculateFinalPrice():
    tk.Label(root, text="The Final Price is ").grid(row=5,column=2)
    originalPrice: float = float(entry1.get())
    discountPrice: float = float(entry2.get()) / 100
    total: float = round(originalPrice - (originalPrice * discountPrice),0)
    tk.Label(root, text=total).grid(row=6,column=2)

# Button
calculateButton = tk.Button(root, command=calculateFinalPrice, text="Calculate").grid(row=4,column=2)

# Starts the event loop and keep the window responsive
root.mainloop()
