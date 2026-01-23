from tkinter import *
import tkinter.messagebox as messagebox

root = Tk()
root.title("BMI Calculator")

def BMI():
    try:
        lengte = float(entry2.get())
        gewicht = float(entry3.get())

        if lengte <= 0 or gewicht <= 0:
            messagebox.showerror("Fout", "Lengte en gewicht moeten groter dan 0 zijn")
            return

        bmi = gewicht / (lengte ** 2)
        entry4.delete(0, END)
        entry4.insert(0, round(bmi, 2))

    except ValueError:
        messagebox.showerror("Fout", "Geef geldige cijfers in")

# Labels
Label(root, text="Leeftijd").grid(row=0, column=0, padx=10, pady=5)
Label(root, text="Lengte (m)").grid(row=1, column=0, padx=10, pady=5)
Label(root, text="Gewicht (kg)").grid(row=2, column=0, padx=10, pady=5)
Label(root, text="BMI").grid(row=3, column=0, padx=10, pady=5)

# Entries
entry1 = Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

entry3 = Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=5)

entry4 = Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=5)

# Button
btn = Button(root, text="Bereken BMI", command=BMI)
btn.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
