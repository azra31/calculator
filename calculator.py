def exit():
    window.destroy()
     
def clear_all():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    e5.config(state='normal')
    e5.delete(0,tk.END)
    e5.config(state='disabled')
 
def cal_savings():
    e5.config(state='normal')
    e5.delete(0,tk.END)
    e5.config(state='disabled')
    salary = int(e1.get())
    total_expenditure = int(e2.get())+int(e3.get())+int(e4.get())
    savings = salary - total_expenditure
    e5.config(state='normal')
    e5.insert(0,savings)
    e5.config(state='disabled')
 
import tkinter as tk
window = tk.Tk()
window.geometry("300x400")
window.config(bg="#FF1493")
window.resizable(width=False,height=False)
window.title('Savings Calculator')
 
v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()
v4 = tk.StringVar()
v5 = tk.StringVar()
 
l1 = tk.Label(window,text="Unesite vrijednosti",font=("Arial",20),fg="White",bg="midnightblue")
 
l2 = tk.Label(window,text="Plata:",font=("Arial",10),fg="midnightblue",bg="White")
e1 = tk.Entry(window,font=("Arial",11),textvariable=v1)
 
l3 = tk.Label(window,text="Putovanje:",font=("Arial",10),fg="White",bg="midnightblue")
e2 = tk.Entry(window,font=("Arial",11),textvariable=v2)
 
l4 = tk.Label(window,text="Hrana:",font=("Arial",10),fg="midnightblue",bg="White")
e3 = tk.Entry(window,font=("Arial",11),textvariable=v3)
 
l5 = tk.Label(window,text="Ostalo:",font=("Arial",10),fg="White",bg="midnightblue")
e4 = tk.Entry(window,font=("Arial",11),textvariable=v4)
 
b1 = tk.Button(window,text="Izračunaj",font=("Arial",15),fg="midnightblue",bg="White",command=cal_savings)
 
l6 = tk.Label(window,text="Ušteđevina:",font=("Arial",10),fg="White",bg="midnightblue")
e5 = tk.Entry(window,font=("Arial",11),state='disabled',textvariable=v5)
 
b2 = tk.Button(window,text="Očisti",font=("Arial",15),fg="midnightblue",bg="White",command=clear_all)
b3 = tk.Button(window,text="Izađi",font=("Arial",15),fg="White",bg="midnightblue",command=exit)
 
l1.place(x=50,y=20)
l2.place(x=20,y=70)
e1.place(x=120,y=70)
l3.place(x=20,y=100)
e2.place(x=120,y=100)
l4.place(x=20,y=130)
e3.place(x=120,y=130)
l5.place(x=20,y=160)
e4.place(x=120,y=160)
b1.place(x=60,y=200)
l6.place(x=20,y=260)
e5.place(x=120,y=260)
b2.place(x=70,y=300)
b3.place(x=60,y=350)
 
 
window.mainloop()
