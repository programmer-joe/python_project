import tkinter as tk
from tkinter import ttk
form = tk.Tk()
form.title('Database Form')
form.geometry('1600x1200')

tab_parent = ttk.Notebook(form)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)

#tab_parent.bind("<<NotebookTabChanged>>",on_tab_selected)#Event listeners

tab_parent.add(tab1,text = 'All Records')
tab_parent.add(tab2,text = 'Add New Record')
tab_parent.add(tab3, text = "Search")


######################ADD WIDGET TABONE###########################################
ProductLabelTabOne = tk.Label(tab1,text = 'Product name:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 100)#whats in the bracket is tab1 beacuse it has to be shown on the tab not the form
QuantityLabelTabOne = tk.Label(tab1,text = 'Quantity:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 200)
PriceLabelTabOne = tk.Label(tab1, text = 'Price:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 300)

ProductEntryTabOne = tk.Entry(tab1,textvariable = '',bd=5, relief="groove", font=("", 15)).place(x= 850, y = 100)
QuantityEntryTabOne = tk.Entry(tab1,textvariable = '',bd=5, relief="groove", font=("", 15)).place(x= 850, y = 200)
PriceEntryTabOne = tk.Entry(tab1,textvariable = '',bd=5, relief="groove", font=("", 15)).place(x= 850, y = 300)

btn_forward = tk.Button(tab1, text="Login", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",command = '')
btn_forward.place(x=850, y=500)
btn_forward_image = tk.PhotoImage(file="button (10).png")
btn_forward.configure(image=btn_forward_image)

btn_backward = tk.Button(tab1, text="Login", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",
                       command='')
btn_backward.place(x=430, y=500)
btn_backward_image = tk.PhotoImage(file="button (11).png")
btn_backward.configure(image=btn_backward_image)

#imgTabOne = image_path(path)
#imgLabelTabOne = tk.Label(tab1, image =imgTabOne).place(x = 1050,y = 500)

##############################ADD WIDGET IN TAB TWO######################
ProductLabelTabTwo = tk.Label(tab2,text = 'Product name:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 100)#whats in the bracket is tab1 beacuse it has to be shown on the tab not the form
QuantityLabelTabTwo = tk.Label(tab2,text = 'Quantity:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 200)
PriceLabelTabTwo = tk.Label(tab2, text = 'Price:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 300)

ProductEntryTabTwo = tk.Entry(tab2,textvariable = '',bd=5, relief="groove", font=("", 15)).place(x= 850, y = 100)
QuantityEntryTabTwo = tk.Entry(tab2,textvariable = '',bd=5, relief="groove", font=("", 15)).place(x= 850, y = 200)
PriceEntryTabTwo = tk.Entry(tab2,textvariable = '',bd=5, relief="groove", font=("", 15)).place(x= 850, y = 300)

add_record_btn = tk.Button(tab2, text="Add Record", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",command = '')
add_record_btn.place(x=430, y=500)
add_record_image = tk.PhotoImage(file="button (14).png")
add_record_btn.configure(image=add_record_image)

add_image_btn = tk.Button(tab2, text="Save Image", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",
                       command='')
add_image_btn.place(x=850, y=500)
add_image_image = tk.PhotoImage(file="button (13).png")
add_image_btn.configure(image=add_image_image)

################################ADD WIDGET TO TAB THREE################################################

tab_parent.pack(expand =1,fill = 'both')

form.mainloop()