from tkinter import*

window =Tk()
window.geometry("400x300")
window.title("MY CALCULATOR")

def solve():
    try:
        n1=float(entry1.get())
        n2=float(entry2.get())
    except ValueError:
        label.config(text="Invalid numbers.")
        return
    
    expression = expression_var.get()
    if expression == "+":
        result = n1 + n2
    elif expression == "-":
        result = n1 - n2
    elif expression == "*":
        result = n1 * n2
    elif expression == "/":
        if n2 == 0:
            label.config(text="Number can't be divide.",fg="red")
            return
        result=n1/n2
    else:
        label.config(text="Select operation",fg="red")
        return
    label.config(text=f"Result: {result}",fg="green")

def reset():
    entry1.delete(0,END)
    entry2.delete(0,END)
    expression_var.set("+")
    label.config(text="Result: ")

Label(window, text="Enter First Number: ",font=("Arial",10)).grid(row=0,column=0,padx=10,pady=10)
entry1 = Entry(window,font=("Arial",10))
entry1.grid(row=0,column=1)

Label(window,text="Enter Second Number: ",font=("Arial",10)).grid(row=1,column=0,padx=10,pady=10)
entry2 = Entry(window,font=("Arial",10))
entry2.grid(row=1,column=1)

expression_var=StringVar()
expression_var.set("+")
Label(window,text="Operation: ",font=("Arial",10)).grid(row=2,column=0,padx=10,pady=10)

frame=Frame(window)
frame.grid(row=2,column=1)

Radiobutton(frame,text="+",variable=expression_var,value="+").pack(side=LEFT)
Radiobutton(frame,text="-",variable=expression_var,value="-").pack(side=LEFT)
Radiobutton(frame,text="*",variable=expression_var,value="*").pack(side=LEFT)
Radiobutton(frame,text="/",variable=expression_var,value="/").pack(side=LEFT)

Button(window,text="Calculate",command=solve,font=("Arial",10)).grid(row=3,column=0,pady=15)
Button(window,text="Reset",command=reset,font=("Arial",10)).grid(row=3,column=1)

label=Label(window,text="Result: ",font=("Arial",12,"bold"))
label.grid(row=4,column=0,columnspan=2,pady=15)

window.mainloop()