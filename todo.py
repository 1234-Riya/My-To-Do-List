import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random
from tkinter import messagebox
import os
root = tk.Tk()
root.geometry('275x325')
root.title('My To-Do List')
root.configure(background ="white")

#create empty list
tasks = []

#for testing purpose use default list
# tasks=["call","burger","pizza"]

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")

#crete function for add task button
def add_task():
    task = input_box.get()
    if task!="":
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning","You need to enter a task.")
    input_box.delete(0,"end")

#craete function for delete all button
def delete_all():
    #since we are changing the list.
    confirmed = messagebox.askyesno("Please Confirm","Do you really want to delete all?")
    if confirmed == True:
        global tasks
        tasks = []
        update_listbox()

#craete function for delete button
def delete():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    # else:
    #     input_box["text"] = "No task present in the list"
    update_listbox()

#create function for sorting in asc
def sort_asc():
    tasks.sort()
    update_listbox()

#create function for sorting in dsc
def sort_dsc():
    tasks.sort(reverse=True)
    update_listbox()

#create function for choose random
def ch_ran():
    task = random.choice(tasks)
    lbl_display["text"] = task

#craete function for no of task
def no_task():
    number_of_tasks = len(tasks)
    msg = "No of tasks : %s" %number_of_tasks
    lbl_display["text"] = msg

#craete exit button
def ext():
    exit()

#create label
f = ("Helvetica",12,"bold")
lbl_name = tk.Label(root,text='My To-Do App',font=f,bg='white',fg='black')
lbl_name.grid(row=0,column=0,sticky='ns')

# create display label
lbl_display = tk.Label(root,text='',font=f,bg='white')
lbl_display.grid(row=0,column=1)

#create input_box
input_box = tk.Entry(root,width=18,justify=CENTER,font = ('Helvetica', 8, 'bold'))
input_box.grid(row=1,column=1,padx=4,pady=8)

#create add task button
add_btn = tk.Button(root,text='Add Task',bg='#000000',fg='red',
                relief='flat',width=12,command=add_task)
add_btn.grid(row=1,column=0)

#create delete all button
delete_all_btn = tk.Button(root,text='Delete All',bg='#000000',fg='red',
                relief='flat',width=12,command=delete_all)
delete_all_btn.grid(row=2,column=0,sticky='n')

#create delete button
delete_btn = tk.Button(root,text='Delete',bg='#000000',fg='red',
                relief='flat',width=12,command=delete)
delete_btn.grid(row=3,column=0,sticky='n')

#create btn for sort in asc
sort_asc_btn = tk.Button(root,text='Sort (ASC)',bg='#000000',fg='red',
                relief='flat',width=12,command=sort_asc)
sort_asc_btn.grid(row=4,column=0,sticky='n')

#create btn for sort in dsc
sort_dsc_btn = tk.Button(root,text='Sort (DSC)',bg='#000000',fg='red',
                relief='flat',width=12,command=sort_dsc)
sort_dsc_btn.grid(row=5,column=0,sticky='n')

#create btn for choose random
choose_ran = tk.Button(root,text='Choose Random',bg='#000000',fg='red',
                relief='flat',width=12,command=ch_ran)
choose_ran.grid(row=6,column=0,sticky='n')

#craete btn for no of task
no_task_btn = tk.Button(root,text='No of Tasks',bg='#000000',fg='red',
                relief='flat',width=12,command=no_task)
no_task_btn.grid(row=7,column=0,sticky='n')

#create exit btn
exit_btn = tk.Button(root,text='Exit',bg='#000000',fg='red',
                relief='flat',width=12,command=ext)
exit_btn.grid(row=8,column=0,sticky='n')

#create empty box
lb_tasks = tk.Listbox(root,height=12,bg = "black",fg='red',activestyle = 'dotbox')
lb_tasks.grid(row=2,column=1,rowspan=7,columnspan=7,padx=5,pady=10,sticky='s')

root.mainloop()
