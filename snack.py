import tkinter as tk
from tkinter import ttk



menu_items = {
    "Pizza": 40.00,
    "Tacos": 49.00,
    "Sandwich": 30.00,
    "Burger": 32.00,
    "Frites": 15.00,
    "Nuggets": 35.00,
    "Soda": 15.00,
    "Limonade": 18.00
}



def ajoute_demond(item):
    demond[item] = demond.get(item, 0) + 1
    update_domend_affiche()
    update_total()



def supprimer_demond(item):
    if item in demond and demond[item] > 0:
        demond[item] -= 1
        if demond[item] == 0:
            del demond[item]
    update_domend_affiche()
    update_total()


def update_domend_affiche():
    demond_text.delete(1.0, tk.END)
    for item, quantite in demond.items():
        demond_text.insert(tk.END, f"{item} x{quantite} - {menu_items[item] * quantite:.2f} Dh\n")


def update_total():
    total_amount = sum(menu_items[item] * quantite for item, quantite in demond.items())
    total_label.config(text=f"Total : {total_amount:.2f} Dh")



def clear_demond():
    global demond
    demond = {}
    update_domend_affiche()
    update_total()



root = tk.Tk()
root.title("Snack de Ahmed Oukhchine")
root.geometry("800x800")
root.configure(bg="#eee")



menu_frame = ttk.Frame(root)
menu_frame.pack(pady=10)



menu_title = ttk.Label(menu_frame, text="Menu", font=("Helvetica", 16, "bold"))
menu_title.pack()



for item, price in menu_items.items():
    button = ttk.Button(menu_frame, text=f"{item} - {price} Dh")
    button.config(command=lambda i=item: ajoute_demond(i))
    button.pack(pady=5, ipadx=5)



demond_frame = ttk.Frame(root)
demond_frame.pack(pady=10)



demond_label = ttk.Label(demond_frame, text="Votre Panier", font=("Ariel", 16, "bold"))
demond_label.pack()


demond_text = tk.Text(demond_frame, height=10, width=40, state='normal')
demond_text.pack()



button_frame = ttk.Frame(root)
button_frame.pack(pady=10)



clear_button = ttk.Button(button_frame, text="Vider le panier")
clear_button.config(command=clear_demond)
clear_button.grid(row=0, column=0, padx=10)




total_label = ttk.Label(root, text="Total : 0.00 Dh", font=("Ariel", 14, "bold"))
total_label.pack(pady=10)



demond = {}



root.mainloop()
