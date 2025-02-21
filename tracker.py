import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import json

root=tk.Tk()
root.title('Password Manager')
root.geometry('600x400')

def insert_in_listbox():
    username=user_entry.get()
    password=pass_entry.get()
    list_box_username.insert(tk.END, username)
    list_box_pass.insert(tk.END, password)
 
def read_json():
    try:
        list_box_username.delete(0,"end")
        list_box_pass.delete(0,"end")
        with open('data.json', 'r') as file:
            data_read = json.load(file)
            
        keys=list(data_read.keys())
        values=list(data_read.values())
        for key in keys:
            list_box_username.insert(tk.END, key)
        for value in values:
            list_box_pass.insert(tk.END, value)
            
    except:
        messagebox.showerror('Error','Ensure Data.JSON is in same folder as program')
        
def delete_entry():
    for selected_user in list_box_username.curselection():
        list_box_username.delete(selected_user)
        
    for selected_pass in list_box_pass.curselection():
        list_box_pass.delete(selected_pass)
               

def save_json():
        user_list=[]
        password_list=[]
                    
        for user in list_box_username.get(0, "end"):
            user_list.append(user)
                        
        for password in list_box_pass.get(0, "end"):
            password_list.append(password)
            
        file_path = filedialog.asksaveasfilename(defaultextension=json, filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    dict={}
                    for key, value in zip(user_list, password_list):
                        dict[key] = value
                    file.write(json.dumps(dict, indent=4))
                messagebox.showinfo('File Saved to:', file_path)
            except Exception as e:
                messagebox.showerror('Error', 'An error has occured while saving.')
                

user_label=tk.Label(root, text='Enter Username:', font = ('Arial',10,'normal'))
user_label.place(relx=0.2, rely=0.2, anchor='center')
user_entry=tk.Entry(root, font = ('Arial',10,'normal'))
user_entry.place(relx=0.2, rely=0.3, anchor='center')

pass_label=tk.Label(root, text='Enter Password:', font = ('Arial',10,'normal'))
pass_label.place(relx=0.2, rely=0.4, anchor='center')
pass_entry=tk.Entry(root, font = ('Arial',10,'normal'))
pass_entry.place(relx=0.2, rely=0.5, anchor='center')

list_box_username=tk.Listbox(root, font = ('Arial',10,'normal'))
list_box_username.place(relx=0.6, rely=0.45, anchor='center', height=250, width=100)
list_box_username.configure(background='skyblue4', foreground='white', font=('Arial', 10))

user_text_label=tk.Label(root, text='Usernames:', font = ('Arial',12,'bold'))
user_text_label.place(relx=0.6, rely=0.1, anchor='center')

pass_text_label=tk.Label(root, text='Passwords:', font = ('Arial',12,'bold'))
pass_text_label.place(relx=0.8, rely=0.1, anchor='center')

list_box_pass=tk.Listbox(root, font = ('Arial',10,'normal'))
list_box_pass.place(relx=0.8, rely=0.45, anchor='center', height=250, width=100)
list_box_pass.configure(background='skyblue4', foreground='white', font=('Arial', 10))

submit=tk.Button(root, text='Add Credentials', command=insert_in_listbox)
submit.place(relx=0.2, rely=0.62, anchor='center')

load_data=tk.Button(root, text='Reload Data', command=read_json)
load_data.place(relx=0.2, rely=0.72, anchor='center')

save_data=tk.Button(root, text='Save Data', command=save_json)
save_data.place(relx=0.2, rely=0.82, anchor='center')

delete_data=tk.Button(root, text='Delete Selection', command=delete_entry)
delete_data.place(relx=0.7, rely=0.85, anchor='center')

root.mainloop()
