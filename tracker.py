import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import PhotoImage
import json 
import secrets

root=tk.Tk()
root.title('Password Manager')
root.geometry('600x400')

image=tk.PhotoImage(file='key.png')
root.iconphoto(True, image)

def insert_in_listbox():
    if len(user_entry.get())==0 or len(pass_entry.get())==0 or len(pass_entry.get())==0:
        messagebox.showerror('Error','Field is empty')
    else:    
        username=user_entry.get()
        password=pass_entry.get()
        website=website_entry.get()
        list_box_web.insert(tk.END, website)
        list_box_username.insert(tk.END, username)
        list_box_pass.insert(tk.END, password)
    
def read_json():
    try:
        list_box_username.delete(0,"end")
        list_box_pass.delete(0,"end")
        list_box_web.delete(0,"end")
        with open('data.json', 'r') as file:
            data_read = json.load(file)
            
        keys=list(data_read.keys())
        values=list(data_read.values())
        for key in keys:
            list_box_username.insert(tk.END, key)
        for i in range(len(values)):
            list_box_pass.insert(tk.END, values[i][0])
        for i in range(len(values)):
            list_box_web.insert(tk.END, values[i][1])           
    except:
        messagebox.showerror('Error','Ensure Data.JSON is in same folder as program')
        
def delete_entry():
    for selected in list_box_username.curselection():
        list_box_username.delete(selected)
        list_box_pass.delete(selected)
        list_box_web.delete(selected)
               
def save_json():
    user_list=[]
    password_list=[]
    website_list=[]
                    
    for user in list_box_username.get(0, "end"):
        user_list.append(user)
                        
    for password in list_box_pass.get(0, "end"):
        password_list.append(password)
    
    for webs in list_box_web.get(0, "end"):
        website_list.append(webs)
            
    file_path = filedialog.asksaveasfilename(defaultextension=json, filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                dict={}
                for key, value, j in zip(user_list, password_list, website_list):
                    dict[key] = value, j
                file.write(json.dumps(dict, indent=4))
            messagebox.showinfo('File Saved to:', file_path)
        except Exception as e:
            messagebox.showerror('Error', 'An error has occured while saving.')
            
def generate_pass():
    secure_pass=secrets.token_urlsafe(16)
    pass_text.set(secure_pass)

website_label=tk.Label(root, text='Enter Website:', font = ('Arial',10,'normal'))
website_label.place(relx=0.2, rely=0.07, anchor='center')
website_entry=tk.Entry(root, font = ('Arial',10,'normal'))
website_entry.place(relx=0.2, rely=0.13, anchor='center')                

user_label=tk.Label(root, text='Enter Username:', font = ('Arial',10,'normal'))
user_label.place(relx=0.2, rely=0.25, anchor='center')
user_entry=tk.Entry(root, font = ('Arial',10,'normal'))
user_entry.place(relx=0.2, rely=0.33, anchor='center')

pass_label=tk.Label(root, text='Enter Password:', font = ('Arial',10,'normal'))
pass_label.place(relx=0.2, rely=0.45, anchor='center')
pass_text=tk.StringVar()
pass_entry=tk.Entry(root, font = ('Arial',10,'normal'), textvariable=pass_text)
pass_entry.place(relx=0.2, rely=0.53, anchor='center')

list_box_username=tk.Listbox(root, font = ('Arial',10,'normal'))
list_box_username.place(relx=0.45, rely=0.45, anchor='center', height=250, width=100)
list_box_username.configure(background='skyblue4', foreground='white', font=('Arial', 10))

user_text_label=tk.Label(root, text='Usernames:', font = ('Arial',12,'bold'))
user_text_label.place(relx=0.45, rely=0.1, anchor='center')

pass_text_label=tk.Label(root, text='Passwords:', font = ('Arial',12,'bold'))
pass_text_label.place(relx=0.65, rely=0.1, anchor='center')

web_text_label=tk.Label(root, text='Websites:', font = ('Arial',12,'bold'))
web_text_label.place(relx=0.85, rely=0.1, anchor='center')

list_box_pass=tk.Listbox(root, font = ('Arial',10,'normal'))
list_box_pass.place(relx=0.65, rely=0.45, anchor='center', height=250, width=100)
list_box_pass.configure(background='skyblue4', foreground='white', font=('Arial', 10))

list_box_web=tk.Listbox(root, font = ('Arial',10,'normal'))
list_box_web.place(relx=0.85, rely=0.45, anchor='center', height=250, width=100)
list_box_web.configure(background='skyblue4', foreground='white', font=('Arial', 10))

submit=tk.Button(root, text='Add Credentials', command=insert_in_listbox)
submit.place(relx=0.2, rely=0.65, anchor='center')

load_data=tk.Button(root, text='Load Data', command=read_json)
load_data.place(relx=0.2, rely=0.75, anchor='center')

save_data=tk.Button(root, text='Save Data', command=save_json)
save_data.place(relx=0.2, rely=0.85, anchor='center')

delete_data=tk.Button(root, text='Delete Selection', command=delete_entry)
delete_data.place(relx=0.7, rely=0.85, anchor='center')

generate_pass_button=tk.Button(root, text='Generate Password', command=generate_pass)
generate_pass_button.place(relx=0.5, rely=0.85, anchor='center')

root.mainloop()
