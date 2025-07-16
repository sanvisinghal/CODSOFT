import tkinter 
import tkinter.messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def clear_tasks():
    if tkinter.messagebox.askyesno("CLEAR ALL"," ARE YOU SURE YOU WANT TO DELETE ALL TASK?"):
        listbox_tasks.delete(0,tkinter.END)

def save_tasks():
    tasks=listbox_tasks.get(0,listbox_tasks.size())
    print("SAVED TASKS: ", tasks)

def edit_task():
    try:
        index=listbox_tasks.curselection()[0]
        selected_tasks=listbox_tasks.get(index)
        entry_task.delete(0,tkinter.END)
        entry_task.insert(0,selected_tasks)
    except :
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task to edit.")

def update_task():
    try:
        index=listbox_tasks.curselection()[0]
        new_task=entry_task.get()
        if new_task.strip():
            listbox_tasks.delete(index)
            listbox_tasks.insert(index,new_task.strip())
            entry_task.delete(0,tkinter.END)
        else:
            tkinter.messagebox.showwarning(title="Warning!", message="Please enter a task to update.")
    except:
         tkinter.messagebox.showwarning(title="Warning!", message="You must select a task to update.")


root=tkinter.Tk()
root.title("TO-DO LIST")
root.geometry("400x400")

font_style=("Helvetica", 12)
btn_color="#af4c4c"
btn_fg="white"

frame=tkinter.Frame(root)
frame.pack(pady=10)

listbox_tasks = tkinter.Listbox(frame, height=10, width=40)
listbox_tasks.pack()

entry_task = tkinter.Entry(frame,width=30,font=font_style)
entry_task.pack()

button_add_task = tkinter.Button(frame, text="ADD TASK", width=30,font=font_style,bg=btn_color,fg=btn_fg,command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(frame, text="DELETE TASK", width=30,font=font_style,bg=btn_color,fg=btn_fg,command=delete_task)
button_delete_task.pack()

button_clear_task = tkinter.Button(frame, text="CLEAR TASK", width=30,font=font_style,bg=btn_color,fg=btn_fg,command=clear_tasks)
button_clear_task.pack()

button_save_tasks = tkinter.Button(frame, text="SAVE TASKS", width=30,font=font_style,bg=btn_color,fg=btn_fg,command=save_tasks)
button_save_tasks.pack()

button_edit_task = tkinter.Button(frame, text="EDIT TASK", width=30,font=font_style,bg=btn_color,fg=btn_fg,command=edit_task)
button_edit_task.pack()

button_update_task = tkinter.Button(frame, text="UPDATE TASK", width=30,font=font_style,bg=btn_color,fg=btn_fg,command=update_task)
button_update_task.pack()

root.mainloop()