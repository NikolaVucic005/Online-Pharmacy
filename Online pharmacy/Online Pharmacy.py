from tkinter import *
from tkinter import messagebox

cart = []
show_cart = None

def Add_to_cart():
    try:
        selected_index = List.curselection()
        if not selected_index:
            raise Exception("You need to select the medicine!")

        get_from_list = List.get(selected_index)

        parts = get_from_list.split('Price:')
        medicine_info = parts[0].strip()
        price = parts[1].strip() if len(parts) > 1 else "Price is not available"

        cart.append((medicine_info, price))

        Show_cart()

        messagebox.showinfo("Medicine successfully added to cart!!", f"You sucessfully added the medicine: {get_from_list} to cart!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def Show_cart():
    global show_cart
    if show_cart and show_cart.winfo_exists():
        show_cart.destroy()

    show_cart = Toplevel()
    show_cart.title("Your cart")
    show_cart.geometry("500x400")

    cart_list = Listbox(show_cart)
    cart_list.pack(fill=BOTH, expand=True)
    cart_list.config(width=40, height=20)

    for medicine, price in cart:
        cart_list.insert(END, f"{medicine} - Price: {price}")
    total_price_button = Button(show_cart, text="Calculate total price", command=Calculate_total_price)
    total_price_button.pack()

def Calculate_total_price():
    total_price = 0
    for _, price in cart:
        try:
            total_price += float(price.replace("RSD", "").replace(",", ".").strip())
        except ValueError:
            pass
    messagebox.showinfo("Total price", f"Total price of medicine in cart: {total_price:.2f} RSD")


def Medicine_list():
    with open("medicine.txt", encoding="utf-8") as file:
        for i in file:
            List.insert(END, i)

def Indications():
    with open("medicine_indications.txt", encoding="utf-8") as file:
        top4 = Toplevel()
        top4.title("Medicine indications")
        top4.geometry("1000x500")
        List2 = Listbox(top4)
        Label_top4 = Label(top4, text="Indications of all medicines are")
        Label_top4.pack()
        List2.pack()
        List2.config(width=100, height=50)
        for i in file:
            List2.insert(END, i)

def Find_medicine():
    medicine_name = entry_field.get().strip().lower()

    if not medicine_name:
        messagebox.showerror("Error", "You need to insert medicine name!")
        return
    try:
        with open("medicine.txt", encoding="utf-8") as file:
            medicine = file.readlines()
        for i, medicine in enumerate(medicine):
            if medicine_name in medicine.strip().lower():
                top = Toplevel()
                top.title("Medicine info")
                top.geometry("600x300")
                parts = medicine.split('Price:')
                medicine_info = parts[0].strip()
                price = parts[1].strip() if len(parts) > 1 else "Price is not available"
                Label(top, text=f"Medicine info:\n{medicine_info}\nPrice: {price}", font=("Arial", 14)).pack(pady=10)
                return

        messagebox.showerror("Error", "Medicine not found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "Medicine file not found!")

def Contraindications():
    with open("medicine_contraindications.txt", encoding="utf-8") as file:
        top5 = Toplevel()
        top5.title("Medicine contraindications")
        top5.geometry("1000x500")
        label_for_top5 = Label(top5, text="Contraindications of all medicines are")
        List3 = Listbox(top5)
        label_for_top5.pack()
        List3.pack()
        List3.config(width=105, height=50)
        for i in file:
            List3.insert(END, i)

def Dosage_and_route():
    with open("dosage.txt", encoding="utf-8") as file:
        top6 = Toplevel()
        top6.geometry("1000x500")
        top6.title("Dosage and route of administration")
        List4 = Listbox(top6)
        label_for_top6 = Label(top6, text="Dosage and route of administration of all medicines")
        label_for_top6.pack()
        List4.pack()
        List4.config(width=121, height=50)
        for i in file:
            List4.insert(END, i)

root = Tk()
root.title("Online pharmacy")
root.geometry("1000x500")
first_label = Label(root, text="Insert fabric/generic name of the medicine")
entry_field = Entry(root)
find_medicine_button = Button(root, text="Find medicine", command=Find_medicine)
all_medicines_list = Button(root, text="List of all medicines", command=Medicine_list)
indications_button = Button(root, text="Medicines indications", command=Indications)
contraindications_button = Button(root, text="Medicines contraindications", command=Contraindications)
dosage_button = Button(root, text=" Dosage and route of administration", command=Dosage_and_route)
add_to_cart_button = Button(root, text="Add medicine to cart", command=Add_to_cart)
List = Listbox(root)
List.config(width=73, height=20)
cart_listbox = Listbox(root)
cart_listbox.config(width=73, height=10)
first_label.pack()
entry_field.pack()
find_medicine_button.pack()
all_medicines_list.pack()
indications_button.pack()
contraindications_button.pack()
dosage_button.pack()
add_to_cart_button.pack()
List.pack()
cart_listbox.pack()
mainloop()

