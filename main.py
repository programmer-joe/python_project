import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

import qrcode

def home_return():
    root.destroy()
    main_menu()
    pass

def login_admin():
    global admin_user_text
    global admin_pass_text
    global root
    if admin_user_text.get() == 'Admin' and admin_pass_text.get() == '1234':
        messagebox.showinfo("Success",'Welcome Admin')
        root.destroy()
        from login_admin import generate_code

    elif admin_user_text.get() == '' or admin_pass_text.get() == '':
        messagebox.showinfo('Error',"All fields are required")
    elif admin_user_text.get() != 'admin' or admin_pass_text.get() != '1234':
        messagebox.showinfo('Error', "Incorrect")
    else:
        messagebox.showwarning("Error","Check Case Sensitivity")
def login_user():
    global root
    global user_user_text
    global user_pass_text
    if user_user_text.get() == 'user' and user_pass_text.get() == '4567':
        messagebox.showinfo("Success",'Welcome User')
        root.destroy()
        import login_user
    elif user_user_text.get() == '' or user_pass_text.get() == '':
        messagebox.showinfo('Error',"All fields are required")
    elif user_user_text.get() != 'user' or user_pass_text.get() != '4567':
        messagebox.showinfo('Error', "Incorrect")

def admin_form():
    global admin_user_text
    global admin_pass_text

    global root
    form.destroy()
    root = tk.Tk()
    root.title("Login System")
    root.geometry("1600x1200")
    root.configure(bg='peach puff3')
    Canvas = tk.Canvas(root, height=1200, width=1600)
    filename = ImageTk.PhotoImage(Image.open("pile 3.gif"))
    Canvas.create_image(0, 0, anchor="nw", image=filename)
    admin_user_text = tk.StringVar()
    admin_pass_text = tk.StringVar()

    Canvas.pack(expand="yes", fill='both')

    admin_user_text = tk.StringVar()
    admin_pass_text = tk.StringVar()

    title = tk.Label(Canvas, text="Login System Admin", font=("times new roman", 40, "bold"), bg="steel blue", fg="black",
                     bd=10, relief="groove")
    title.place(x=0, y=0, relwidth=1)
    user_icon = tk.PhotoImage(file="businessman-png-icon-1.png")
    password_icon = tk.PhotoImage(file="password.png")
    lbluser = tk.Label(root, text="Username", image=user_icon, compound="left",
                       font=("timesnew romans", 20, "bold"), bg="white").place(x=620, y=100)
    lblpass = tk.Label(root, text="Password", image=password_icon, compound="left",
                       font=("timesnew romans", 20, "bold"), bg="white").place(x=620, y=300)

    # lbluser = tk.Label(root, text="Username",  compound="left",
    #                    font=("timesnew romans", 20, "bold"), bg="white").place(x=650,y=100)

    text_user = (tk.Entry(root,textvariable =admin_user_text, bd=5, relief="groove", font=("", 15))).place(x= 600,y=200)
    # lblpass = tk.Label(root, text="Password", compound="left",
    #                    font=("timesnew romans", 20, "bold"), bg="white").place(x=650,y=300)
    text_pass = tk.Entry(root, bd=5,textvariable = admin_pass_text, relief="groove", font=("", 15),show = "*").place(x= 600,y=400)

    # btn_login = tk.Button(root, text="Login", font=("times new roman", 14, "bold"), bg="steel blue", fg="black")
    # btn_login.place(x=680, y=500)
    btn_login = tk.Button(root,command = login_admin, text="Login", font=("times new roman", 14, "bold"), bg="steel blue", fg="black")
    btn_login.place(x=620, y=500)
    btn_img = tk.PhotoImage(file="button (6).png")
    btn_login.configure(image=btn_img)

    home_login = tk.Button(root, text="Home", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",command =home_return)
    home_login.place(x=630, y=600)
    home_img = tk.PhotoImage(file="button (7).png")
    home_login.configure(image=home_img)

    root.mainloop()
def user_form():
    global user_user_text
    global user_pass_text
    global root
    form.destroy()
    root = tk.Tk()
    root.title("Login System")
    root.geometry("1600x1200")
    root.configure(bg='royal blue3')
    Canvas = tk.Canvas(root, height=1200, width=1600)
    title = tk.Label(Canvas, text="Login System User", font=("times new roman", 40, "bold"), bg="dark slate grey", fg="black",
                     bd=10, relief="groove")
    title.place(x=0, y=0, relwidth=1)
    user_icon = tk.PhotoImage(file="businessman-png-icon-1.png")

    user_user_text = tk.StringVar()
    user_pass_text = tk.StringVar()

    # Login_frame = tk.Frame(root, bg="black")
    # bg_image = tk.PhotoImage(file="pile1.gif")
    # x = tk.Label(image=bg_image)
    # x.place(x=500,y=150)
    #Login_frame.place(x=500, y=150)

    filename = ImageTk.PhotoImage(Image.open("output-onlinepngtools (4).png"))
    Canvas.create_image(0, 0, anchor="nw", image=filename)

    Canvas.pack(expand="yes", fill='both')
    user_icon = tk.PhotoImage(file="businessman-png-icon-1.png")
    password_icon = tk.PhotoImage(file="password.png")
    lbluser = tk.Label(root, text="Username", image=user_icon, compound="left",
                       font=("timesnew romans", 20, "bold"), bg="white").place(x=620,y=100)
    lblpass = tk.Label(root, text="Password", image=password_icon, compound="left",
                       font=("timesnew romans", 20, "bold"), bg="white").place(x=620,y=300)
    # lbluser = tk.Label(root, text="Username",  compound="left",
    #                    font=("timesnew romans", 20, "bold"), bg="white").place(x=650,y=100)

    text_user = (tk.Entry(root,textvariable=user_user_text, bd=5, relief="groove", font=("", 15))).place(x= 600,y=200)
    # lblpass = tk.Label(root, text="Password", compound="left",
    #                    font=("timesnew romans", 20, "bold"), bg="white").place(x=650,y=300)
    text_pass = tk.Entry(root,textvariable =user_pass_text, bd=5, relief="groove", font=("", 15),show = "*").place(x= 600,y=400)

    btn_login = tk.Button(root, text="Login", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",command = login_user)
    btn_login.place(x=620, y=500)
    btn_img = tk.PhotoImage(file="button (6).png")
    btn_login.configure(image=btn_img)

    home_login = tk.Button(root, text="Login", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",
                           command=home_return)
    home_login.place(x=630, y=600)
    home_img = tk.PhotoImage(file="button (7).png")
    home_login.configure(image=home_img)

    root.mainloop()

def main_menu_exit():
    messagebox.showinfo("Thank You", "Patronize Us Later")
    form.destroy()

def main_menu():
    global form
    form = tk.Tk()
    #
    l_title = tk.Message(text="WELCOME TO PARTNERS\n SUPERMARKET", relief="raised", width=2000, padx=600, pady=0,
                         fg="black",
                         bg="steel blue", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")

    Canvas = tk.Canvas(form, height=1200, width=1600)
    filename = ImageTk.PhotoImage(Image.open("output-onlinepngtools (1).png"))
    Canvas.create_image(0, 0, anchor="nw", image=filename)

    Canvas.pack(expand="yes", fill='both')
    # empty = tk.Label(Canvas,text = "Click To Sign In").pack()
    admin_button = tk.Button(Canvas, text="Plane", relief="flat", command=admin_form)
    admin_button.place(x=650, y=50)

    img = tk.PhotoImage(file="button (2).png")
    admin_button.configure(image=img)

    user_button = tk.Button(Canvas, text="Plane", relief="flat", command=user_form)
    user_button.place(x=650, y=230)
    img_user = tk.PhotoImage(file="button (3).png")
    user_button.configure(image=img_user)

    exit_button = tk.Button(Canvas, text="Plane", relief="flat", command=main_menu_exit)
    exit_button.place(x=650, y=410)
    img_exit = tk.PhotoImage(file="button (4).png")
    exit_button.configure(image=img_exit)

    form.mainloop()
main_menu()

