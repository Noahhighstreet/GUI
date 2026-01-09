import tkinter as tk


def Bereken():
    g1 = float(getal1.get())
    g2 = float(getal2.get())
    som = g1 + g2
    resultaat.delete(0,tk.END)
    resultaat.insert(0,som)

def Clear():
    getal1.delete(0, tk.END)
    getal2.delete(0, tk.END)
    resultaat.delete(0, tk.END)

root = tk.Tk()
label1 = tk.Label(root, text="Getal 1")
label1.grid(row=0, column=0)
getal1 = tk.Entry(root)
getal1.grid(row=0, column=1)

label2 = tk.Label(root, text="Getal 2")
label2.grid(row=1, column=0)
getal2 = tk.Entry(root)
getal2.grid(row=1, column=1)

button1= tk.Button(root, text="Bereken", command=Bereken)
button1.grid(row=2, column=0)
button2 = tk.Button(root, text="Clear", command=Clear)
button2.grid(row=2, column=1)

label3 = tk.Label(root, text="Resultaat")
label3.grid(row=3, column=0)
resultaat = tk.Entry(root)
resultaat.grid(row=3, column=1)

root.mainloop()
