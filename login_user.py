import shutil
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk,Image
import os
from tkinter import filedialog
import db_config
import pymysql
form = tk.Tk()
form.title('Database Form')
form.geometry('1200x600')


def on_tab_selected(event):
    global blank_text_boxes_tab_two
    global image_selected


    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab,'text')

    if tab_text == "All Records":
        print("All record tabs selected")
        if (blank_text_boxes_tab_two is False) and (image_selected is True):
            load_database_results()

    if tab_text == "Add New Record":
        print("Add new record tab selected")
        blank_text_boxes_tab_two = True
        image_selected = False

def connection_obj():
    return pymysql.connect(host=db_config.DB_SERVER,
                           user=db_config.DB_USER,
                           password=db_config.DB_PASS,
                           database=db_config.DB)


def database_error(err):
    messagebox.showinfo("Error", err)
    return False


def load_database_results():
    global rows
    global num_of_rows
    try:
        con = connection_obj()
        sql = "SELECT * FROM tbl_supermarket"
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        num_of_rows = cursor.rowcount
        cursor.close()
        con.close()
        has_loaded_successfully = True
        messagebox.showinfo("Connected to Database!")
    except pymysql.InternalError as e:
        has_loaded_successfully = database_error(e)
    except pymysql.OperationalError as e:
        has_loaded_successfully = database_error(e)
    except pymysql.ProgrammingError as e:
        has_loaded_successfully = database_error(e)
    except pymysql.DataError as e :
        has_loaded_successfully = database_error(e)
    except pymysql.IntegrityError as e:
        has_loaded_successfully = database_error(e)
    except pymysql.NotSupportedError as e:
        has_loaded_successfully = database_error(e)
    return has_loaded_successfully


def scroll_forward():
    global row_counter
    global num_of_rows

    if row_counter>=(num_of_rows-1):
        messagebox.showinfo("Database Error","End of database")
    else:
        row_counter = row_counter + 1
        scroll_data()
def scroll_back():
    global row_counter
    if row_counter is 0:
        messagebox.showinfo("Database Error","Start of Database")
    else:
        row_counter = row_counter -1
        scroll_data()


def image_path(file_path):

    return ImageTk.PhotoImage(Image.open(file_path))

def load_photo_tab_one(file_path):
    image = image_path(file_path)
    imgLabelTabOne.configure(image = image)
    imgLabelTabOne.image = image


def scroll_data():
    product_tabone.set(rows[row_counter][1])
    quantity_tabone.set(rows[row_counter][2])
    price_tabone.set(rows[row_counter][3])
    section_tabone.set(rows[row_counter][4])
    try:
        ph_path = db_config.PHOTO_DIRECTORY + rows[row_counter][5]

        load_photo_tab_one(ph_path)
    except FileNotFoundError:
        load_photo_tab_one(db_config.PHOTO_DIRECTORY + file_name)


def select_image():
    global image_selected
    global image_file_name
    global file_new_home
    global file_to_copy

    path_to_image = filedialog.askopenfilename(initialdir ="/",
                                               title = "Open File",
                                               filetypes = (("PNGs","*.png"),("GIFs","*.gifs"),
                                                            ("All Files","*.*")))
    try:
        if path_to_image:
            image_file_name = os.path.basename(path_to_image)
            file_new_home = db_config.PHOTO_DIRECTORY + image_file_name
            file_to_copy = path_to_image
            image_selected = True
            load_photo_tab_two(file_to_copy)
    except IOError as err:
        image_selected = False
        messagebox.showinfo("File Error",err)



def load_photo_tab_two(file_path):
    image = image_path(file_path)
    imageLabelTabTwo.configure(image = image)
    imageLabelTabTwo.image = image

def insert_into_database(product_name_field, quantity_field, price_field,section_field, photo_name):
    try:
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)
        sql = "INSERT INTO tbl_supermarket(Product_name,Quantity,Price,Section,Photo)" \
              "Values(%s,%s,%s,%s,%s) "
        vals = (product_name_field,quantity_field,price_field,section_field,photo_name)
        cursor = con.cursor()
        cursor.execute(sql,vals)
        con.commit()
        cursor.close()
        con.close()

        messagebox.showinfo("Success!","Record added to database")
    except pymysql.InternalError as e:
        database_error(e)
    except pymysql.OperationalError as e:
        database_error(e)
    except pymysql.ProgrammingError as e:
        database_error(e)
    except pymysql.DataError as e:
        database_error(e)
    except pymysql.IntegrityError as e:
        database_error(e)
    except pymysql.NotSupportedError as e:
        database_error(e)
def add_new_record():
    global blank_text_boxes_tab_two
    global file_new_home
    global file_to_copy

    blank_text_box_count = 0
    if product_tabtwo.get() is "":
        blank_text_box_count += 1
    if quantity_tabtwo.get() is "":
        blank_text_box_count +=1
    if price_tabtwo.get() is "":
        blank_text_box_count += 1
    if section_tabtwo.get() is "":
        blank_text_box_count += 1

    if blank_text_box_count > 0:
        blank_text_boxes_tab_two = True
        messagebox.showinfo("Entry Error","Blank Text boxes")
    elif blank_text_box_count is 0:
        blank_text_boxes_tab_two = False

        if image_selected:
            try:
                shutil.copy(file_to_copy,file_new_home)#src dst source and destination
            except shutil.SameFileError:
                pass
            insert_into_database(product_tabtwo.get(), quantity_tabtwo.get(),price_tabtwo.get(),section_tabtwo.get(),image_file_name)
        else:
                messagebox.showinfo("File Error","Please Select an Image")

def search_records():
    con = connection_obj()
    sql_query = "SELECT * FROM tbl_supermarket WHERE Section = %s AND Product_name = %s "
    vals = (options_var.get(),search_text_var.get())
    cursor = con.cursor()
    cursor.execute(sql_query,vals)
    my_rows = cursor.fetchall()
    total_rows = cursor.rowcount
    cursor.close()
    con.close()
    print(my_rows)
    print("TOTAL FOUND",total_rows)
    messagebox.showinfo("Results Found",my_rows)
    

file_name = 'default.png'#a path is complete with a file name
path = db_config.PHOTO_DIRECTORY + file_name
rows = None
num_of_rows = None
row_counter = 0
image_selected = False
image_file_name = None
file_to_copy = None
file_new_home = None
blank_text_boxes_tab_two = False

tab_parent = ttk.Notebook(form)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)

#tab_parent.bind("<<NotebookTabChanged>>",on_tab_selected)#Event listeners

tab_parent.add(tab1,text = 'All Records')
tab_parent.add(tab2,text = 'Add New Record')
tab_parent.add(tab3, text = "Search")


######################ADD WIDGET TABONE###########################################
product_tabone =tk.StringVar()
quantity_tabone = tk.StringVar()
price_tabone =tk.StringVar()
section_tabone = tk.StringVar()

product_tabtwo =tk.StringVar()
quantity_tabtwo = tk.StringVar()
price_tabtwo =tk.StringVar()
section_tabtwo = tk.StringVar()

ProductLabelTabOne = tk.Label(tab1,text = 'Product name:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 100)#whats in the bracket is tab1 beacuse it has to be shown on the tab not the form
QuantityLabelTabOne = tk.Label(tab1,text = 'Quantity:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 200)
PriceLabelTabOne = tk.Label(tab1, text = 'Price:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 300)
SectionLabelTabOne = tk.Label(tab1, text = 'Section:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 400)


ProductEntryTabOne = tk.Entry(tab1,textvariable = product_tabone,bd=5, relief="groove", font=("", 15)).place(x= 850, y = 100)
QuantityEntryTabOne = tk.Entry(tab1,textvariable = quantity_tabone,bd=5, relief="groove", font=("", 15)).place(x= 850, y = 200)
PriceEntryTabOne = tk.Entry(tab1,textvariable = price_tabone,bd=5, relief="groove", font=("", 15)).place(x= 850, y = 300)

SectionEntryTabOne = tk.Entry(tab1,textvariable = section_tabone,bd=5, relief="groove", font=("", 15)).place(x= 850, y = 400)


btn_forward = tk.Button(tab1, text="Login", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",command = scroll_forward)
btn_forward.place(x=850, y=500)
btn_forward_image = tk.PhotoImage(file="button (10).png")
btn_forward.configure(image=btn_forward_image)

btn_backward = tk.Button(tab1, text="Login", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",
                       command=scroll_back)
btn_backward.place(x=430, y=500)
btn_backward_image = tk.PhotoImage(file="button (11).png")
btn_backward.configure(image=btn_backward_image)

imgTabOne = image_path(path)
imgLabelTabOne = tk.Label(tab1, image =imgTabOne)
imgLabelTabOne.grid(row = 0,column =3 , rowspan = 3,pady = 15)

##############################ADD WIDGET IN TAB TWO######################
ProductLabelTabTwo = tk.Label(tab2,text = 'Product name:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 100)#whats in the bracket is tab1 beacuse it has to be shown on the tab not the form
QuantityLabelTabTwo = tk.Label(tab2,text = 'Quantity:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 200)
PriceLabelTabTwo = tk.Label(tab2, text = 'Price:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 300)
SectionLabelTabTwo = tk.Label(tab2, text = 'Section:',compound="left",
                       font=("timesnew romans", 20, "bold")).place(x= 430, y = 400)




ProductEntryTabTwo = tk.Entry(tab2,textvariable = product_tabtwo,bd=5, relief="groove", font=("", 15)).place(x= 850, y = 100)
QuantityEntryTabTwo = tk.Entry(tab2,textvariable = quantity_tabtwo,bd=5, relief="groove", font=("", 15)).place(x= 850, y = 200)
PriceEntryTabTwo = tk.Entry(tab2,textvariable = price_tabtwo,bd=5, relief="groove", font=("", 15)).place(x= 850, y = 300)
SectionEntryTabTwo = tk.Entry(tab2,textvariable = section_tabtwo,bd=5, relief="groove", font=("", 15)).place(x= 850, y = 400)

imageTabTwo = image_path(path)
imageLabelTabTwo = tk.Label(tab2,image = imageTabTwo)
imageLabelTabTwo.grid(row = 0,column = 2, padx =15,pady = 15, rowspan = 3)

add_record_btn = tk.Button(tab2, text="Add Record", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",command = add_new_record)
add_record_btn.place(x=430, y=500)
add_record_image = tk.PhotoImage(file="button (14).png")
add_record_btn.configure(image=add_record_image)

add_image_btn = tk.Button(tab2, text="Save Image", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",
                       command=select_image)
add_image_btn.place(x=850, y=500)
add_image_image = tk.PhotoImage(file="button (13).png")
add_image_btn.configure(image=add_image_image)

################################ADD WIDGET TO TAB THREE################################################

search_text_var = tk.StringVar()
search_Family = tk.Entry(tab3,bd=5, relief="groove", font=("", 15), textvariable = search_text_var).place(x=200,y=100)

contents = {"Food Stuff","Beverages","Stationaries","Miscellaneous","Gadget"}

options_var = tk.StringVar()
options_var.set("Select Product Section")

drop_down = tk.OptionMenu(tab3,options_var,*contents).place (x=600,y=100)
search_btn = tk.Button(tab3, text="Save Image", font=("times new roman", 14, "bold"), bg="steel blue", fg="black",
                       command=search_records)
search_btn.place(x=450, y=200)
search_image = tk.PhotoImage(file="button (16).png")
search_btn.configure(image=search_image)


success = load_database_results()
if success:
    product_tabone.set(rows[0][1])
    quantity_tabone.set(rows[0][2])
    price_tabone.set(rows[0][3])
    section_tabone.set(rows[0][4])
    photo_path = db_config.PHOTO_DIRECTORY+rows[0][5]
    load_photo_tab_one(photo_path)

tab_parent.pack(expand =1,fill = 'both')

form.mainloop()