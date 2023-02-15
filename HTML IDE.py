from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import webbrowser
from tkinter import messagebox

root = Tk()

root.title("HTML IDE")
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("Open.png"))
save_img = ImageTk.PhotoImage(Image.open("Save.png"))
run_img = ImageTk.PhotoImage(Image.open("run.png"))

file_name = Label(root, text = "File Name")
file_name.place(relx = 0.28, rely = 0.03, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.46, rely = 0.03, anchor = CENTER)

text_area = Text(root, width = 80, height = 40)
text_area.place(relx = 0.5, rely = 0.55, anchor = CENTER)
name = ""

def open_file():
    global name
    input_file_name.delete(0, END)
    text_area.delete(1.0, END)
    
    html_file = filedialog.askopenfilename(title = "Selcect File", filetypes = (("HTML Files", "*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    format_name = name.split('.')[0]
    input_file_name.insert(END, format_name)
    root.title(format_name)
    html_file = open(name,'r')
    para = html_file.read()
    text_area.insert(END, para)
    text_file.close()
    
def save_file():
    file_name = input_file_name.get()
    file = open(file_name + ".html", "w")
    data = text_area.get("1.0",END)
    file.write(data)
    input_file_name.delete(0, END)
    text_area.delete("1.0", END)
    messagebox.showinfo("File Saved","File Saved Successfully")
    
def run_file():
    global name
    webbrowser.open(name)




open_btn = Button(root, image = open_img, command = open_file)
open_btn.place(relx = 0.05, rely = 0.03, anchor = CENTER)

save_btn = Button(root, image = save_img, command = save_file)
save_btn.place(relx = 0.12, rely = 0.03, anchor = CENTER)

run_btn = Button(root, image = run_img, command = run_file)
run_btn.place(relx = 0.19, rely = 0.03, anchor = CENTER)


root.mainloop()