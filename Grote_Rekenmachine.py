import tkinter as tk
root = tk.Tk()
root.title("Rekenmachine")

huidige = ""
operator = ""
eerste_getal = 0

def click(num):
    global huidige
    huidige += str(num)
    EntryA.delete(0, tk.END)
    EntryA.insert(0, huidige)

def optellen():
    global eerste_getal, operator, huidige
    eerste_getal = int(huidige)
    operator = "+"
    huidige = ""
    EntryA.delete(0, tk.END)

def aftrekken():
    global eerste_getal, operator, huidige
    eerste_getal = int(huidige)
    operator = "-"
    huidige = ""
    EntryA.delete(0, tk.END)

def vermenigvuldigen():
    global eerste_getal, operator, huidige
    eerste_getal = int(huidige)
    operator = "*"
    huidige = ""
    EntryA.delete(0, tk.END)

def delen():
    global eerste_getal, operator, huidige
    eerste_getal = int(huidige)
    operator = "/"
    huidige = ""
    EntryA.delete(0, tk.END)

def equal():
    global huidige
    tweede_getal = int(huidige)

    if operator == "+":
        resultaat = eerste_getal + tweede_getal
    elif operator == "-":
        resultaat = eerste_getal - tweede_getal
    elif operator == "*":
        resultaat = eerste_getal * tweede_getal
    elif operator == "/":
        resultaat = eerste_getal / tweede_getal

    EntryA.delete(0, tk.END)
    EntryA.insert(0, resultaat)
    huidige = str(resultaat)

def C():
    global huidige, eerste_getal, operator
    huidige = ""
    eerste_getal = 0
    operator = ""
    EntryA.delete(0, tk.END)


EntryA = tk.Entry(root)
EntryA.grid(row = 0, column = 1, columnspan=5 , ipadx= 30, pady= 15,padx= 30)

Button0 = tk.Button(root, text='0',command=lambda: click(0))
Button0.grid(row = 4, column = 1,ipadx= 28, ipady=20)

Button1 = tk.Button(root, text='1',command=lambda: click(1))
Button1.grid(row = 3, column = 1,ipadx= 28, ipady=20)

Button2 = tk.Button(root, text='2',command=lambda: click(2))
Button2.grid(row = 3, column = 2,ipadx= 28, ipady=20)

Button3 = tk.Button(root, text='3',command=lambda: click(3))
Button3.grid(row = 3, column = 3,ipadx= 28, ipady=20)

Button4 = tk.Button(root, text='4',command=lambda: click(4))
Button4.grid(row = 2, column = 1,ipadx= 28, ipady=20)

Button5 = tk.Button(root, text='5',command=lambda: click(5))
Button5.grid(row = 2, column = 2,ipadx= 28, ipady=20)

Button6 = tk.Button(root, text='6',command=lambda: click(6))
Button6.grid(row = 2, column = 3,ipadx= 28, ipady=20)

Button7 = tk.Button(root, text='7',command=lambda: click(7))
Button7.grid(row = 1, column = 1, ipadx= 28, ipady=20)

Button8 = tk.Button(root, text='8',command=lambda: click(8))
Button8.grid(row = 1, column = 2,ipadx= 28, ipady=20)

Button9 = tk.Button(root, text='9',command=lambda: click(9))
Button9.grid(row = 1, column = 3,ipadx= 28, ipady=20)

ButtonOp = tk.Button(root, text='+',command = optellen)
ButtonOp.grid(row = 1, column = 4,ipadx= 27, ipady=20)

ButtonVe = tk.Button(root, text='-',command = aftrekken)
ButtonVe.grid(row = 2, column = 4,ipadx= 28, ipady=20)

ButtonVx = tk.Button(root, text='x',command = vermenigvuldigen)
ButtonVx.grid(row = 3, column = 4,ipadx= 28, ipady=20)

ButtonDe = tk.Button(root, text='/',command = delen)
ButtonDe.grid(row = 4, column = 4,ipadx= 28, ipady=20)

ButtonCl = tk.Button(root, text='C',command = C)
ButtonCl.grid(row = 4, column = 2,ipadx= 28, ipady=20)

ButtonIs = tk.Button(root, text='=',command = equal)
ButtonIs.grid(row = 4, column = 3,ipadx= 28, ipady=20)


root.mainloop()
