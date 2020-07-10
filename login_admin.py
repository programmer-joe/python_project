import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk,Image
import qrcode


def generate_code():
    global img
    if len(product_label_text.get()) != 0:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('Some data')
        qr.make(fit=True)
        try:
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(file_name_text.get() + '.png')
            messagebox.showinfo("Sucess",file_name_text.get().title() + ' Is Saved Successfully ')
        except:
            pass
    else:

        messagebox.showwarning("Error","Enter File Name")
root = tk.Tk()
root.title("Login System")
root.geometry("1600x1200")
root.configure(bg='peach puff3')
Canvas = tk.Canvas(root, height=1200, width=1600)
filename = ImageTk.PhotoImage(Image.open("qr_code.gif"))
Canvas.create_image(0, 0, anchor="nw", image=filename)
product_label_text = tk.StringVar()
file_name_text = tk.StringVar()
title = tk.Label(Canvas, text="QR Code Generator", font=("times new roman", 40, "bold"), bg="steel blue", fg="black",
                     bd=10, relief="groove")
title.place(x=0, y=0, relwidth=1)
Canvas.pack(expand="yes", fill='both')

product_label = tk.Label(root, text="Enter Product Name Here", compound="left",
                       font=("timesnew romans", 20, "bold"), bg="white").place(x=620, y=100)

file_name = tk.Label(root, text="Enter File Name Here", compound="left",
                       font=("timesnew romans", 20, "bold"), bg="white").place(x=620, y=350)

product_label_entry = (tk.Entry(root, textvariable =product_label_text, bd=5, relief="groove", font=("", 15))).place(x= 650, y=200)

file_name_entry = (tk.Entry(root, textvariable =file_name_text, bd=5, relief="groove", font=("", 15))).place(x= 650, y=450)

btn_login = tk.Button(root,command = generate_code, text="Login", font=("times new roman", 14, "bold"), bg="steel blue", fg="black")
btn_login.place(x=680, y=550)
btn_img = tk.PhotoImage(file="button (8).png")
btn_login.configure(image=btn_img)




root.mainloop()
