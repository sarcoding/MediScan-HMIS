import tkinter as tk
import asyncio
from reception import add_new_patient

def reception_main():
    def submit_data():
        aNo = int(abha_no_entry.get())
        height = height_entry.get()
        weight = weight_entry.get()

        print("Abha No.:", aNo)
        print("Height:", height)
        print("Weight:", weight)

        asyncio.get_event_loop().run_until_complete(add_new_patient(aNo, height, weight))
        
        abha_no_entry.delete(0, tk.END)
        height_entry.delete(0, tk.END)
        weight_entry.delete(0, tk.END)


    root = tk.Tk()
    root.title("Receptionist's System")


    abha_no_label = tk.Label(root, text="Abha No.:")
    abha_no_label.grid(row=0, column=0)

    abha_no_entry = tk.Entry(root)
    abha_no_entry.grid(row=0, column=1)

    height_label = tk.Label(root, text="Height (cm):")
    height_label.grid(row=0, column=2)

    height_entry = tk.Entry(root)
    height_entry.grid(row=0, column=3)

    weight_label = tk.Label(root, text="Weight (kg):")
    weight_label.grid(row=0, column=4)

    weight_entry = tk.Entry(root)
    weight_entry.grid(row=0, column=5)

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=submit_data)
    submit_button.grid(row=1, columnspan=6)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    reception_main()